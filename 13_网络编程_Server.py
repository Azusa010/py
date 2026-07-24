# import socket

# # AF_INET 用于 Internet 进程间通信；SOCK_STREAM 流式套接字，TCP
# tcp_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# # AF_INET 用于 Internet 进程间通信；SOCK_DGRAM 数据报套接字，TCP
# udp_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

# tcp_socket.send()

import socket

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_socket.bind(("127.0.0.1", 8888))

while True:
    recv_data, client_info = udp_socket.recvfrom(1024)
    client_ip = client_info[0]
    client_port = client_info[1]
    print(f"客户端{client_ip}:{client_port}说:{recv_data.decode('utf-8')}")
    udp_socket.sendto("你好，消息已收到".encode("utf-8"),client_info)
    
udp_socket.close()