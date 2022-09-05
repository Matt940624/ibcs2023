import asyncio
import json
from typing import Dict, List
from matplotlib.pyplot import get
from numpy import place

import textual.events as events
from textual.app import App
from textual.layouts.grid import GridLayout
from textual.widgets import ScrollView
from textual_inputs import TextInput


from net import(
    ChatClientProtocol,
    AbstractChatClientProtocol,
    AbstractMessageHandler,
    TestProtocol
)

USERNAME = "username"
MESSAGE = "message"


class ChatApp(App, AbstractMessageHandler):

    _protocol: AbstractChatClientProtocol = None
    _username: str = "NoobMaster69"
    _messages: List[Dict] = []

    def __init__(self, protocol: AbstractChatClientProtocol) -> None:
        if protocol is None:
            raise ValueError("Can not continue without a chat protocol")

        self._protocol = protocol
        self._protocol.message_handler = self
        super().__init__(title="Chat App", log="log.log")

    async def on_load(self, event: events.Load):
        await self._protocol.connect()
        await self.bind("escape", "quit", "Quit")

    async def on_mount(self, event: events.Mount):
        grid: GridLayout = await self.view.dock_grid()

        grid.add_column(name="center", fraction=1)
        grid.add_row(name="top", fraction=1)
        grid.add_row(name="bottom", size=0)
        grid.add_areas(chat="center,top", message_input="center,bottom")

        self._chat_scrollview = ScrollView("", name="chat-view")
        self._message_input = TextInput(
            name="message_input", title="Message", placeholder="Type message here")
        grid.place(chat=self._chat_scrollview,
                   message_input=self._message_input)
        await self._message_input.focus()

    async def on_key(self, event: events.Key):
        if event.key == "enter":
            value = self._message_input.value
            self._message_input.value = ""
            value = value.strip()
            if len(value) == 0:
                return
            if self._protocol is None:
                return
            else:
                data = {USERNAME: self._username, MESSAGE: value}
                package = json.dumps(data)
                await self._protocol.send(package)

    async def on_shutdown_request(self, event: events.ShutdownRequest) -> None:
        await self._protocol.close()
        return await super().on_shutdown_request(event)

    async def on_message_recieved(self, message: str) -> None:
        message = json.loads(message)
        await self.add_message(message)

    async def add_message(self, message: Dict):
        self._messages.append(message)
        strings = [
            f"{message.get(USERNAME)}: {message.get(MESSAGE)}"
            for message in self._messages
        ]

        await self._chat_scrollview.update("\n\n".join(strings), False)


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
        await app.process_messages()

    asyncio.run(_run_client(host, port))
