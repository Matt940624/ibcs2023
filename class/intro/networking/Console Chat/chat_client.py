import asyncio
import json

from net import(
    ChatClientProtocol,
    AbstractChatClientProtocol,
    AbstractMessageHandler,
    TestProtocol
)

USERNAME = "username"
MESSAGE = "message"


class ChatApp(AbstractMessageHandler):

    _protocol: AbstractChatClientProtocol = None
    _username: str = None

    def __init__(self, protocol: AbstractChatClientProtocol) -> None:
        if protocol is None:
            raise ValueError("Can not continue without a chat protocol")

        self._protocol = protocol
        self._protocol.message_handler = self

    async def on_message_recieved(self, message: str) -> None:
        message = json.loads(message)
        uname: str = message.get(USERNAME)
        msg: str = message.get(MESSAGE)

        uname = f"[{uname}]".ljust(15)
        print(f"{uname}: {msg}")

    async def get_message(self):
        loop = asyncio.get_event_loop()
        while self._protocol.is_connected:
            message = None
            message = await loop.run_in_executor(None, input, ">>>")
            message = message.strip()
            if message == "q":
                await self._protocol.close()
            else:
                data = {USERNAME: self._username, MESSAGE: message}
                package = json.dumps(data)
                await self._protocol.send(package)

    async def prompt_username(self):
        valid = False
        while not valid:
            self._username = input("Type in a username: ").strip()
            valid = len(self._username) > 0

    async def run(self):
        await self.prompt_username()
        await self._protocol.connect()

        try:
            await self.get_message()
        except Exception as e:
            print(e)
        finally:
            if self._protocol.is_connected:
                await self._protocol.close()


def run_client(
    host: str = "127.0.0.1",
    port: int = 5001,
    *,
    test: bool = False
) -> None:
    async def _run_client(host, port):
        protocol: AbstractChatClientProtocol = None
        if test:
            protocol = TestProtocol()
        else:
            protocol = ChatClientProtocol(host, port)

        app = ChatApp(protocol=protocol)
        await app.run()

    asyncio.run(_run_client(host, port))
