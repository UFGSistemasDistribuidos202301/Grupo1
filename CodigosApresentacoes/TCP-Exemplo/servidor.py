import socket

def calcular_salario(cargo,salario):
    # Lógica para calcular o salário com base no terceiro input
    if (cargo == "operador" or cargo == "Operador"):
        salario = 0.2 * float(salario) + float(salario)
    if (cargo == "programador" or cargo == "Operador"):
        salario = 0.18 * float(salario) + float(salario)
    return salario

# Configurações do servidor
HOST = 'localhost'  # Endereço IP do servidor
PORT = 50000  # Porta de comunicação

# Criação do socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(1)

print('Aguardando conexão do cliente...')

# Aceitando a conexão do cliente
conexao, endereco = servidor.accept()
print('Cliente conectado:', endereco)

# Recebendo os três inputs do cliente
nome = conexao.recv(1024).decode()
cargo = conexao.recv(1024).decode()
salario = conexao.recv(1024).decode()

print('Inputs recebidos do cliente: Nome: {}, Cargo: {}, Salario: {}'.format(nome, cargo, salario))

# Calculando o salário usando o terceiro input
salario = calcular_salario(cargo,salario)

print('Inputs gerados apos calculo do salario do cliente: Nome: {}, Cargo: {}, Salario: {}'.format(nome, cargo, salario))
# Enviando o salário calculado de volta para o cliente
conexao.send(str(salario).encode())

# Fechando a conexão
conexao.close()
servidor.close()