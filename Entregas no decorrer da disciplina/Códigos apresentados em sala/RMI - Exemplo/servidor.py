import Pyro4

@Pyro4.expose
class Servidor:
    def ajustaSalario(self, input2, input3):
        if input2 == "programador":
            input3 *= 1.8
        elif input2 == "operador":
            input3 *= 2
        return input3

daemon = Pyro4.Daemon()
uri = daemon.register(Servidor())

print("URI do servidor:", uri)
daemon.requestLoop()