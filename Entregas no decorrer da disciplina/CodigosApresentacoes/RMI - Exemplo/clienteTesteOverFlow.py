import Pyro4

uri = "PYRO:obj_d731a6459e2840d196199bee75abe677@localhost:61100"

cliente = Pyro4.Proxy(uri)

input2 = "operador"
input3 = 100

resultado = cliente.ajustaSalario(input2, input3)
print("Resultado:", resultado)

input("Pressione Enter para sair...")