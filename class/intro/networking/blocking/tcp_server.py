# networking/blocking/tcp_server.py

from operator import add
import socket


def main():
    host = "172.16.12.41"
    port = 5000

    # creat a new socket
    s = socket.socket()

    # create a tuple for host an port
    network_host = (host, port)

    # tell socket to use host and port
    s.bind(network_host)

    # start listening for requests
    s.listen()

    # accept incoming connections
    conn, addr = s.accept()
    print(f"Accepted connection from {addr}")

    # We're a server. We never stop listening
    # Were also not providing a graceful way to exit
    while True:
        # receive BINARY data
        data = conn.recv(1024)
        if not data:
            break

        # convert BINARY data into string
        data = data.decode()
        print(f"From connection: {data}")
        data = data.upper()
        # return data to client
        print(f"Sending back to client: {data}")
        conn.send(data.encode())
    conn.close()


if __name__ == "__main__":
    main()
