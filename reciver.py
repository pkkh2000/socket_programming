import socket


#AF_INET for IPV4
#AF_INET6 for IPV6
#SOCK_DGRAM for UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 127.0.0.1 is used to use socket internally also called Loopback/Localhost
# 9999 is port (use free port) 
s.bind(("127.0.0.1",9999))

while True:
    data_recv=s.recvfrom(100)
    print(data_recv)
    # sending response 
    rply="thanks for connecting.."
    s.sendto(rply.encode('ascii'), data_recv[1])