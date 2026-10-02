import socket
socket_client = socket.socket()

socket_client.bind("localhost", 8888)

while True:     # 可以勇敢无限循环来确保持续的发送消息给服务端
    send_msg = input("请输入要发送的消息")
    if send_msg == 'exit':
        # 通过特殊标记来确保可以退出无限循环
        break
    socket_client.send(send_msg.encode("UTF-8"))    # 消息需要编码为字节数组（UTF-8编码）


# 接收返回消息
while True:
    send_msg = input("请输入要发送的消息").encode("UTF-8")
    socket_client.send(send_msg)

    recv_data = socket_client.recv(1024)
    print(f"服务端回复消息为：", recv_data.decode("UTF-8"))
# 关闭连接
socket_client.close()
