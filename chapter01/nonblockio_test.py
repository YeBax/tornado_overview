
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setblocking(False)
host = "www.baidu.com"
try:
    client.connect((host, 80))  # 阻塞IO， cpu空闲
except BlockingIOError as e:
    pass

while 1:
    try:
        client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format("/", host).encode("utf8"))
        print("send success")
        break
    except OSError as e:
        pass

data = b""
while True:
    try:
        d = client.recv(1024)
    except BlockingIOError as e:
        continue
    if d:
        data += d
    else:
        break

data = data.decode("utf-8")
print(data)
