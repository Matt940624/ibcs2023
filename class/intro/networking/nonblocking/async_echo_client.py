
import asyncio

import asyncio

ENCODING = "utf8"


class EchoClientProtocol(asyncio.Protocol):

    def __init__(self, on_conn_lost, loop):
        # we need the loop later so we can execute some
        # extra code on the loop
        self._loop = loop

        # future that we will use to inform amin that we have quit
        self.on_conn_lost = on_conn_lost
        self.is_connected = True
        self._transport = None

    def connection_made(self, transport: asyncio.BaseTransport):
        self._transport = transport
        self.is_connected = True
        peername = transport.get_extra_info('peername')
        print(f"COnnected to {peername}")

    def connection_lost(self, exc: Exception):
        self.is_connected = False
        print("Connection has been closed")
        self.on_conn_lost.set_result(True)
        return super().connection_lost(exc)

    def data_received(self, data: bytes):
        message = data.decode(ENCODING)
        print(f"Message received: {message}")

    def send(self, data: str):
        if data:
            message = data.encode(ENCODING)
            self._transport.write(message)

    async def get_message(self, loop: asyncio.BaseEventLoop):
        while self.is_connected:
            message = await loop.run_in_executor(None, input, '')
            message = message.strip()
            if message == 'q':
                self.is_connected = False
                self._transport.close()
            else:
                self.send(message)


async def main():
    # get a reference to the event loop since we are using
    # low level apis
    loop = asyncio.get_running_loop()
    host = "127.0.0.1"
    port = 5000

    # create a future to listen to later so we can
    # detect the closing of the lcient
    on_conn_lost = loop.create_future()

    # create an instance of the echoclientprotocol
    echo_client_protocol = EchoClientProtocol(on_conn_lost, loop)

    # create connection
    transport, protocol = await loop.create_connection(
        lambda: echo_client_protocol,
        host,
        port
    )

    # start even loop that listens for input messages
    await echo_client_protocol.get_message(loop)

    # handle cleanup when client close
    try:
        await on_conn_lost
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())
