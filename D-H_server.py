from socket import *

p, g = 101, 2


def f(g, x, p):
    return pow(g, x) % p


if __name__ == '__main__':
    privateKey = input("输入你的私钥：")
    privateKey = int(privateKey)
    publicKey = f(g, privateKey, p)

    # 启动服务端
    server_socket = socket(AF_INET, SOCK_STREAM)
    host = gethostbyname(gethostname())
    print(host)
    server_socket.bind((host, 12345))
    server_socket.listen(1)
    print('等待连接...')
    conn, addr = server_socket.accept()
    print('连接来自：', addr)

    # 发送公钥给客户端
    print(f"发送公钥：{publicKey}")
    conn.send(str(publicKey).encode())

    # 接收客户端消息并打印
    counter_publicKey = conn.recv(1024)
    print(f"对方公钥: {int(counter_publicKey.decode())}")

    Ks = f(int(counter_publicKey), privateKey, p)
    print(f"会话密钥：{Ks}")
