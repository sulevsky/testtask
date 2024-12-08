import logging
import os
from logging import config

from signalbot import Command, Context, SignalBot

import cot_seriliazer
import logging_config
from cot_sender import configure_sender, CotSender
from messages import ok_message, error_message
from parser import parse_message

config.dictConfig(logging_config.LOGGING_CONFIGURATION)

logger = logging.getLogger(__name__)


class CommandHandler(Command):
    def __init__(self, cot_sender: CotSender):
        self.cot_sender = cot_sender

    async def handle(self, c: Context):
        parse_result = parse_message(c.message.text)
        if isinstance(parse_result, str):
            response = error_message(parse_result)
        else:
            cot_message = cot_seriliazer.to_cot(parse_result)
            await self.cot_sender.send_message(cot_message)
            response = ok_message
        await c.send(response)


def main():
    cot_url = os.environ.get("COT_URL")
    if not cot_url:
        raise ValueError("Must set COT_URL environment variable")
    logger.info(f"Configured COT server: {cot_url}")
    signal_service_address = os.environ.get("SIGNAL_SERVICE_ADDRESS")
    if not signal_service_address:
        raise ValueError("Must set SIGNAL_SERVICE_ADDRESS environment variable")
    logger.info(f"Configured Signal server: {signal_service_address}")
    phone_number = os.environ.get("PHONE_NUMBER")
    if not phone_number:
        raise ValueError("Must set PHONE_NUMBER environment variable")
    logger.info(f"Configured Signal phone number: {phone_number}")

    bot = SignalBot(
        {"signal_service": signal_service_address, "phone_number": phone_number}
    )
    cot_sender = configure_sender(cot_url)
    handler = CommandHandler(cot_sender)
    bot.register(handler)
    bot.start()


if __name__ == "__main__":
    main()
