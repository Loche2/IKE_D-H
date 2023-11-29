from socket import *

p, g = 101, 2


def f(g, x, p):
    return pow(g, x) % p


if __name__ == '__main__':
    privateKey = input("Input your private key:")
    privateKey = int(privateKey)
    publicKey = f(g, privateKey, p)

    host = 'localhost'
    # 启动服务端
    conn = socket(AF_INET, SOCK_STREAM)
    conn.connect((host, 12345))
    print('连接到：', host)

    # 发送公钥给客户端
    print(f"发送公钥：{publicKey}")
    conn.send(str(publicKey).encode())

    # 接收客户端消息并打印
    counter_publicKey = conn.recv(1024)
    print(f"对方公钥: {counter_publicKey.decode()}")

    Ks = f(int(counter_publicKey), privateKey, p)
    print(f"会话密钥：{Ks}")
