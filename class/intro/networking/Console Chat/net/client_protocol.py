from abc import ABC, abstractmethod
import asyncio
from typing import Coroutine, Coroutine
from json import loads, dumps
from xml.sax import parseString

from urllib3 import connection_from_url
ENCODING = "utf8"


def _async(coro: Coroutine):
    async def _run(coro: Coroutine):
        return await coro

    loop = asyncio.get_event_loop()
    return loop.create_task(_run(coro))


class AbstractMessageHandler(ABC):
    @abstractmethod
    async def on_message_recieved(self, message: str) -> None:
        raise NotImplementedError

    async def on_connection_lost(self) -> None:
        return None

    async def on_close(self) -> None:
        return None


class AbstractChatClientProtocol(ABC):
    _is_connected: bool = False
    _host: str
    _port: int
    _message_handler: AbstractMessageHandler = None

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    @property
    def message_handler(self) -> AbstractMessageHandler:
        return self._message_handler

    @message_handler.setter
    def message_handler(self, handler: AbstractMessageHandler) -> None:
        self._message_handler = handler

    @abstractmethod
    async def connect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def send(self, data: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def close(self) -> None:
        raise NotImplementedError


class ChatClientProtocol(AbstractChatClientProtocol, asyncio.Protocol):
    _transport: asyncio.Transport

    async def connect(self) -> None:
        loop = asyncio.get_event_loop()
        await loop.create_connection(lambda: self, self._host, self._port)

    async def send(self, data: str) -> None:
        if data:
            package = data.encode(ENCODING)
            self._transport.write(package)

    async def close(self) -> None:
        self._transport.close()
        self._is_connected = False
        if self.message_handler:
            await self._message_handler.on_close()

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        self._transport = transport
        self._is_connected = True

    def connection_lost(self, exc: Exception) -> None:
        self._is_connected = False
        if self.message_handler:
            _async(self.message_handler.on_connection_lost())

    def data_received(self, data: bytes) -> None:
        message = data.decode(ENCODING)
        if self.message_handler:
            _async(self.message_handler.on_message_recieved(message))


class TestProtocol(AbstractChatClientProtocol):

    delay: float = 0.5

    def __init__(self, *, delay: int = 0.5):
        self.delay = delay

    async def connect(self):
        self._is_connected = True

    async def send(self, data: str):
        await asyncio.sleep(self.delay)
        if data and self._is_connected and self.message_handler:
            await self.message_handler.on_message_recieved(data)

    async def close(self):
        self._is_connected = False
        if self.message_handler:
            await self.message_handler.on_close()
