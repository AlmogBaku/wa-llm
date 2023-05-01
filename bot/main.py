import os
from concurrent.futures import ThreadPoolExecutor
from time import sleep

import grpc
import promptlayer
from dotenv import load_dotenv
from loguru import logger

from src import start_bot

load_dotenv()
logger.add(".logs/file_{time}.log")
promptlayer.api_key = os.environ.get("PROMPTLAYER_API_KEY")


def run():
    executor = ThreadPoolExecutor()

    db_uri = os.environ.get('DB_URL', 'postgresql://user:password@localhost:5432/bot')

    chat_mgr_grpc_url = os.environ.get('CHAT_MGR_GRPC_URL', 'unix:///tmp/chat-mgr.sock')

    while True:
        try:
            with grpc.insecure_channel(chat_mgr_grpc_url) as channel:
                future = executor.submit(start_bot, channel, db_uri)
                future.result()
        except Exception as e:
            logger.exception(e)
            sleep(2)


if __name__ == '__main__':
    run()
