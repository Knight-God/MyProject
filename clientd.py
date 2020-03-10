import socket; #导入socket模块
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM); #设置步骤，设置为AF_INET及STREAM
phone.connect(("127.0.0.1",8888)); #连接地址127.0.0.1及8888端口

while True: #死循环 —— 用于不断接收信息
    msg = input("信息:");
    phone.send(msg.strip().encode('utf-8')); #信息以utf-8形式发送
    if not msg: continue; #若发送信息为空则返回重新输入
    infos= phone.recv(1024); #接收外部信息
    print("服务器",infos.decode('utf-8')); #解码外部信息
phone.close();
