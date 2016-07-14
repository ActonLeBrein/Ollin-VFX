import socket
 
datos_servidor = ("localhost", 9999)
cliente = socket.socket()
cliente.connect(datos_servidor)
while True:
    mensaje = raw_input("Ingresa un mensaje:> ")
    cliente.send(mensaje)
    if mensaje == "salir":
        break
    recibido = cliente.recv(1024)
    print recibido
cliente.close()
print "Fin del programa."