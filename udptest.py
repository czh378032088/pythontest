import socket


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('0.0.0.0',5010))

print('Bind UDP on 5010 ...')

while True:
    data,addr = s.recvfrom(1024)
    print(data)
