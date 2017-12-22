import select
import socket

HOST = '127.0.0.1'
PORT = 3000
timeout =500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置连接超时
s.settimeout(timeout)
s.connect((HOST, PORT))
s.sendall("aaa".encode(encoding='utf_8'))
# 恢复默认超时设置
#s.settimeout(None)
#s.connect((HOST, PORT))
#s.sendall('msg')