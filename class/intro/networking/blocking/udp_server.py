import socket


def main():
    host = "127.0.0.1"
    port = 5004

    s = socket.socket(type=socket.SOCK_DGRAM)
    network_host = (host, port)
    s.bind(network_host)
    print("server started...")

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print(f"Recieved from {addr}: {data}")
        data = data.upper()
        print(f"Sending to {addr}: {data}")
        s.sendto(data.encode(), addr)
    s.close


if __name__ == "__main__":
    main()
