import socket


def main():
    host = "172.24.0.62"
    port = 5005

    s = socket.socket(type=socket.SOCK_DGRAM)
    network_host = (host, port)

    data = socket.gethostbyname_ex("brentmparker.com")
    server_host = data[2][0]
    server = (server_host, 9001)
    s.bind(network_host)

    message = input(">>>")
    while message != "q":
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print(f"Received from server({addr}): {data}")
        message = input(">>>")
    s.close()


if __name__ == "__main__":
    main()
