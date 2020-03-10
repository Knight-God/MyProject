import socket;
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1);#端口强制释放。
phone.bind(("127.0.0.1",8888));
phone.listen(5);
print("准备中...");
conn,client_addr= phone.accept();
print(conn,client_addr);

while True:
    try:
        data=conn.recv(1024);
        print("客户端数据",data);
        conn.send(input("信息:").encode('utf-8'));
    except ConnectionResetError:
        break;
conn.close();

phone.close();