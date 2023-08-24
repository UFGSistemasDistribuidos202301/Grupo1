import requests
import json
from config import IPFS_BASE_URL

def add(file) -> str:
    # Faz uma solicitação POST para adicionar um arquivo ao IPFS
    response = requests.post(f"{IPFS_BASE_URL}/add", files={"file": file}, params={'cid-version': 1})

    # Verifica se a resposta do IPFS foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro ao obter arquivo do IPFS: {response.content}")
        return

    # Analisa os dados JSON retornados pela resposta
    data = json.loads(response.content)

    # Retorna o hash do CID (Content Identifier) do arquivo adicionado ao IPFS
    return data["Hash"]

def get(cid: str) -> dict:
    # Parâmetros para a solicitação GET no IPFS
    params = {'arg': cid, 'archive': True, 'compress': True}

    # Faz uma solicitação POST para obter um arquivo do IPFS
    response = requests.post(f"{IPFS_BASE_URL}/get", params=params)

    # Verifica se a resposta do IPFS foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro ao obter arquivo do IPFS: {response.content}")
        return

    try:
        # Importa as bibliotecas necessárias para manipulação de arquivos tar e io
        import tarfile, io

        # Abre o arquivo tar recebido como resposta e lê o seu conteúdo
        with tarfile.open(fileobj=io.BytesIO(response.content), mode='r:gz') as tar:
            filename = tar.getnames()[0]
            file = tar.extractfile(filename)
            content: bytes = file.read()

        # Converte o conteúdo lido (bytes) para um dicionário usando JSON
        return json.loads(content)
    except tarfile.BadGzipFile:
        print("Erro ao obter arquivo do IPFS: Não foi possível realizar leitura do arquivo - Arquivo não é Gzip")
    except KeyError:
        print(f"Erro ao obter arquivo do IPFS: Não foi possível extrair arquivo {filename} - Arquivo não existe")

def write(cid: str, path: str) -> None:
    # Definindo os parâmetros para a solicitação GET no IPFS
    params = {'arg': cid, 'archive': True, 'compress': True}

    # Fazendo uma solicitação POST para obter um arquivo do IPFS
    response = requests.post(f"{IPFS_BASE_URL}/get", params=params)

    # Verificando se a resposta do IPFS foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro ao obter arquivo do IPFS: {response.content}")
        return

    # Gravando o conteúdo da resposta em um arquivo local
    with open(f"{path}/output.tar.gz", 'wb') as file:
        file.write(response.content)
       
def main():
    file_path = "./examples/record.txt"
    with open(file_path, "rb") as file:
        cid = add(file)
        content = get(cid)
        print(content)
    hash = add(json.dumps({"nome": "Lucas"}))
    print(hash)
    content = get(hash)
    print(content)
if __name__ == "__main__":
    main()