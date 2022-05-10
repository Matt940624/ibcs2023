
import asyncio
from email import message

ENCODING = "utf-8"


class EchoServerProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self._transport = None

    # Called when we accept a new connection
    def connection_made(self, transport: asyncio.BaseTransport):
        peername = transport.get_extra_info("peername")
        print(f"connection from {peername}")
        self._transport = transport

    # Called when new data is incoming
    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        print(f"Data received: {message}")

        message = message.upper()
        self._transport.write(message.encode(ENCODING))

    # called when a connection is close or there is an error
    def connection_lost(self, exc: Exception):
        peername = self._transport.get_extra_info('peername')
        print(f"Lost connection from {peername}")
        return super().connection_lost(exc)


async def main():
    # get a reference to the event loop since we are using
    # low level APIs

    loop = asyncio.get_running_loop()
    host = '127.0.0.1'
    port = 5000

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        host,
        port
    )

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
