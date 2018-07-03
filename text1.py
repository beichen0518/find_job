# 服务器

from socket import socket, AF_INET, SOCK_STREAM # 导入套接字模块
# 基于tcp协议
import datetime


def main():
    # 创建一个 基于TCP协议的套接字对象
    # 因为我们做的应用级的产品或服务所以可以利用现有的传输服务实现数据传输
    server = socket(AF_INET, SOCK_STREAM) # 创建服务器端的套接字(为了让别人连接)
    # 把服务绑定ip地址（网络主机的身份标识）和端口（用来区分不同服务的IP地址的扩展）（端口是一个标识可以唯一确定一个服务）
    server.bind(('10.7.189.133', 6700))
    server.listen(512) # 监听等别人来连你，512是队列的大小，如果前面有人正连接你的服务，后面的人就排队等待
    # 开始监听客服端的连接
    print('服务器已经启动正在监听...')
    while True:
        # 通过accept方法接受客服端的连接
        # accept方法是一个阻塞式的方法 如果没有客户端连上来
        # 那么accept就会让代码阻塞，直到有client连接成功才返回
        # accept方法返回一个元组，元组中的第一个值表示客服对象
        # 第二个值又是一个元组，包含client的ip端口
        client, addr = server.accept()
        print(addr, '连接成功')
        print(client)
        client.send(input().encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print(data)
        # client.close()


if __name__ == '__main__':
    main()


