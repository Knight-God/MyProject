import socket;
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
phone.connect(("127.0.0.1",8888));

while True:
    msg = input("信息:");
    phone.send(msg.strip().encode('utf-8'));
    if not msg: continue;
    infos= phone.recv(1024);
    print("服务器",infos.decode('utf-8'));
phone.close();