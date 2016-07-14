import socket
from thread import *
 
#192.168.100.38
datos_servidor = ("localhost", 9999)
servidor = socket.socket()
servidor.bind(datos_servidor)
print "Servidor enlazado\n"
servidor.listen(5)
 
def mi_hilo(cliente):
    while True:
        recibido = cliente.recv(1024)
        if recibido == "salir":
            break
        print "Cliente: %s" %recibido
        cliente.send("Servidor: Ya escuche [%s]" %recibido)
    cliente.close()
while True:
    (cliente, addr) = servidor.accept()
    start_new_thread(mi_hilo, (cliente,))
servidor.close()
print "Fin del programa."