import socket

# 创建socket对象
socket_server = socket.socket()

# 绑定socket_server到指定的IP地址
# socket_server.bind(host, port)
socket_server.bind("localhost", 8888)

# 服务端开始监听端口
# socket_server.listen(backlog)
# backlog为int整数，表示允许的连接数量，超出的会等待，可以不填，不填会自动设置一个合理值
socket_server.listen(1)

# 接收客户端连接，获得连接对象
conn, address = socket_server.accept()
print(f"接收客户端连接，连接来自：{address}")
# accept方法是阻塞方法，如果没有连接，会卡在当前这一行不向下执行代码
# accept返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素

# 客户端连接后，通过recv放啊，接收客户端发送的消息
while True:
    data = conn.recv(1024).decode("UTF-8")  # 接收客户端发送的消息，参数为接收的最大字节数
    # recv方法的返回值是字节数组(Bytes)，可以通过decode使用UTF-8解码成字符串
    # recv方法的传参是buffsize，缓冲区大小，一般设置为1024即可
    if not data:  # 如果没有数据，说明客户端断开连接了
        break
    print(f"接收到客户端发送的消息：{data.decode}")
    # 可以通过while True无限循环来持续和客户端进行数据交互
    # 可以通过判定客户端发来的特殊标记，如exit，来退出无限循环

    # 通过conn（客户端档次连接对象），调用send方法可以回复消息
    conn.send("服务端已收到消息".encode("UTF-8"))

# conn（客户端档次连接对象）和socket_server对象调用close方法，关闭连接
conn.close()
socket_server.close()

















