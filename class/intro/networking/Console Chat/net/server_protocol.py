import asyncio
from typing import List

ENCODING = "utf8"


class ChatServerProtocol(asyncio.Protocol):

    def __init__(self, transportPool: List[asyncio.BaseTransport]) -> None:
        super().__init__()
        self._transport = None
        self._transportPool = transportPool

    # Called when we accept a new connection
    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        peerName = transport.get_extra_info('peername')
        print(f"Connection from {peerName}")
        self._transport = transport
        self._transportPool.append(transport)

    # Called when new data is incoming
    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        print(f"Data received: {message}")
        self.broadcast_message(message)

    def broadcast_message(self, message: str):
        for transport in self._transportPool:
            if transport != self._transport:
                transport.write(message.encode(ENCODING))

    # Called when a connection is closed or there is an error
    def connection_lost(self, exc: Exception) -> None:
        peerName = self._transport.get_extra_info("peername")
        print(f"Lost connection from {peerName}")
        self._transportPool.remove(self._transport)
        return super().connection_lost(exc)


def run_server(host: str = "127.0.0.1", port: int = 5001):
    async def _run_server(host: str, port: int):
        loop = asyncio.get_event_loop()
        transports: List[asyncio.BaseTransport] = []
        server = await loop.create_server(
            lambda: ChatServerProtocol(transports), host, port
        )
        async with server:
            await server.serve_forever()
    asyncio.run(_run_server(host=host, port=port))


if __name__ == "__main__":
    run_server()
