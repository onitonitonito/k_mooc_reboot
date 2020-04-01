"""
# Windows socket client serveur en local erreur WinError 10061
# https://www.developpez.net/forums/d1801094/autres-langages/python/
# reseau-web/windows-socket-client-serveur-local-erreur-winerror-10061-a/
= https://bit.ly/2UBPHps
"""
# import socket
# params = ('127.0.0.1', 8808)
# BUFFER_SIZE = 1024
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(params)
# s.send("test")
# data = s.recv(BUFFER_SIZE)
# print('Datas : %s' % data)
# s.close


import socket

# params = ('127.0.0.1', 1025)
params = ('localhost', 1025)
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('Démarrer le serveur ...')
    s.bind(params)

    print('Ecoutez ...')
    s.listen(1)

    connect, address = s.accept()
    print('Connexion acceptée: %s' % str(address))

    with connect:
        while True:
            data = connect.recv(BUFFER_SIZE)
            if not data:
                break
            connect.send('Bonjour!');
    connect.close
    s.close
