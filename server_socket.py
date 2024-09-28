import socket

with socket.socket() as s :
    addr = ("0.0.0.0",80) #443 web
    s.bind(addr)
    s.listen()
    print("start server..")

    conn, addr = s.accept()
    print("accept {}:{}".format(addr[0],addr[1]))
    data = conn.recv(1024) 
    conn.send("Hi This is Web".encode())
    
