import socket
import threading
import selectors
from tkinter.tix import MAX
from tracemalloc import start

TIMEOUT = 60
MAX_CONNECTIONS = 10


def main():
    host = "127.0.0.1"
    port = "5004"
    network_host = (host, port)
    s = socket.socket()
    s.bind(network_host)
    s.listen(MAX_CONNECTIONS)

    # create a selector. This is the object that listens
    # for new events

    selector = selectors.DefaultSelector()
    # register some object that can create events
    # Parameters are:
    #   the object that orginiates the event
    #   the type of event to listen for
    #   the function/method to call when that event is detected
    selector.register(s, selectors.EVENT_READ, accept)

    print("Server has started...")

    # create a loop that handles events
    while True:
        for key, mask in selector.select():
            handler = key.data
            handler(selector, key.fileobj)


def accept(selector: selectors.DefaultSelector, s: socket.socket):
    conn, addr = s.accept()
    conn.setblocking(False)
    conn.settimeout(TIMEOUT)

    print(f"Connection form {addr}")

    selector.register(conn, selectors.EVENT_READ, start_thread)


def read_from_socket(selector, conn):
    try:
        data = conn.recv(1024)
        if not data:
            unregister(selector, conn)
        data = data = data.decode()
        prompt = (f"Received {data}: ").ljust(40)
        print(f"{prompt}: {data}")
        data = data.upper()
        conn.send(data.encode())
    except socket.timeout as err:
        print(f"Socket timed out")
        print(err)
        unregister(selector, conn)
    except IOError as err:
        print(f"IOError from socket")
        print(err)
        unregister(selector, conn)


def start_thread(selector, conn):
    thread = threading.Thread(target=read_from_socket, args=(selector, conn))
    thread.start()


def unregister(selector, fileobj):
    try:
        selector.unregister(fileobj)
    except KeyError:
        pass
    except ValueError:
        pass
    finally:
        fileobj.close()


if __name__ == "__main__":
    main()
