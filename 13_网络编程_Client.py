

import socket

udp_socket =socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
server_ip = "127.0.0.1"
server_port = 8888


while True:
    udp_socket.sendto(input("对服务器说").encode("utf-8"),(server_ip,server_port))    
    recv_data,server_info = udp_socket.recvfrom(1024)
    print(f"服务器说:{recv_data.decode('utf-8')}")
udp_socket.close()