import socket

# Configurações do servidor
HOST = 'localhost'  # Endereço IP do servidor
PORT = 50000  # Porta de comunicação

# Criação do socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

# Enviando os três inputs para o servidor
nome = input("Digite o nome: ")
cliente.send(nome.encode())
cargo = input("Digite o cargo: ")
cliente.send(cargo.encode())
salario = input("Digite o salario: ")
cliente.send(salario.encode())

# Recebendo o salário calculado do servidor
salario = cliente.recv(1024).decode()

print('O salário de {} foi ajustado para {} pelo servidor.'.format(nome,salario))

# Fechando a conexão
cliente.close()