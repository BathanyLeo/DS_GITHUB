# -*- coding: utf-8 -*-

import socket #importer le module socket

UDP_IP = "192.168.0.202" #Adresse IP du serveur UDP
UDP_PORT = 5005 #Port du serveur UDP 

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0) #Délai d'attente d'une seconde 

sock.connect((UDP_IP,UDP_PORT)) #connection au serveur UDP
sock.send("cinema") #envoie du message "cinema" au serveur

trameReponse, addr = sock.recvfrom(1024) #ligne de décodage des trames.


print "Réception de la trame de réponse", trameReponse.encode("hex") #Affichage de la trame réponse en hexa

b3=ord(trameReponse[3])<<24 #decalage de bit
b2=ord(trameReponse[2])<<16 #decalage de bit
b1=ord(trameReponse[1])<<8 #decalage de bit
b0=ord(trameReponse[0])<<0 #decalage de bit

code = b0|b1|b2|b3 #addition des trame de réponse pour former le code

print code #Afficher le code 

