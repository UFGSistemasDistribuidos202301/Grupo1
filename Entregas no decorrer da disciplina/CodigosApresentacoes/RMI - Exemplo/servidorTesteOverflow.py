import Pyro4
import threading

@Pyro4.expose
class Servidor:
    clientes_conectados = 0
    lock = threading.Lock()

    def ajustaSalario(self, input2, input3):
        with Servidor.lock:
            Servidor.clientes_conectados += 1
            print("Clientes conectados:", Servidor.clientes_conectados)

        if input2 == "programador":
            input3 *= 1.2
        elif input2 == "operador":
            input3 *= 2
        return input3

    def desconectarCliente(self):
        with Servidor.lock:
            Servidor.clientes_conectados -= 1
            print("Clientes conectados:", Servidor.clientes_conectados)

def desconectarCliente():
    Servidor.desconectarCliente()

Pyro4.Daemon.disconnect = desconectarCliente

daemon = Pyro4.Daemon()
uri = daemon.register(Servidor())

print("URI do servidor:", uri)

try:
    daemon.requestLoop()
except Pyro4.errors.ConnectionClosedError:
    print("Cliente desconectado.")
    Servidor.desconectarCliente()