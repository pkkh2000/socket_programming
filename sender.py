import socket


#AF_INET for IPV4
#AF_INET6 for IPV6
#SOCK_DGRAM for UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

rec_data=("127.0.0.1",9999)
user_data=input("Enter the msg:- ")
new=user_data.encode('ascii')
s.sendto(new,rec_data)
print("Ho gya Kamm sahab Ji")