import Pyro4

uri = input("Digite o URI do servidor: ")

cliente = Pyro4.Proxy(uri)

input1 = input("Digite o nome do funcionario: ")
input2 = input("Digite o cargo do funcionario: ")
input3 = float(input("Digite o salario do funcionario: "))

resultado = cliente.ajustaSalario(input2, input3)
print("Resultado:", resultado)
input("Pressione Enter para sair...")