import socket
#Below, you would have to input your target ip and the specific port
target_ip = input(str("Enter web address or ip address: "))
target_port = int(input("Enter specific port: "))

MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MySocket.settimeout(1)
#connect_ex returns an integer to show the success of the conection and only returns 0 when the connection is successful.
Nettuple = (target_ip, target_port)
result = MySocket.connect_ex(Nettuple)

if result == 0:
    print ("OPEN")
else:
    print ("NOT OPEN")

MySocket.close

