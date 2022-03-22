import socket
import threading


def main():
    host = "127.0.0.1"
    port = 5004

    s = socket.socket()
    network_host = (host, port)
    s.bind(network_host)
    s.listen(10)
    print("server started...")

    while True:
        conn, addr = s.accept()
        # If there is no response in 5 seconds, close
        conn.settimeout(5)
        print(f"Connection from {addr}")

        # create a new threa
        # target = function/ method that will be called when the thread starts
        # args = arguments to pass to target function
        thread = threading.Thread(target=listen_to_client, args=(conn, addr))
        thread.start()


def listen_to_client(conn: socket.socket, addr: socket._RetAddress):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            data = data = data.decode()
            prompt = (f"Received from {addr}: ").ljust(40)
            print(f"{prompt}: {data}")
            data = data.upper()
            conn.send(data.encode())
        except socket.timeout as err:
            print(f"Socket from {addr} timed out")
            print(err)
            break
        except IOError as err:
            print(f"IOError from socket at {addr}")
            print(err)
            break
    conn.close()


if __name__ == "__main__":
    main()
