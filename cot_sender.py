import asyncio

import pytak


class CotSender:
    def __init__(self, writer: pytak.TXWorker):
        self.writer = writer

    async def send_message(self, cot_event: str):
        binary = bytes(cot_event, encoding="utf-8")
        await self.writer.send_data(binary)
        await self.writer.send_data(binary)


def configure_sender(cot_server_url: str) -> CotSender:
    config = {"COT_URL": cot_server_url}
    _, writer = asyncio.run(pytak.protocol_factory(config))
    write_worker = pytak.TXWorker(None, config, writer)
    return CotSender(write_worker)
