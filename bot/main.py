import os
from concurrent.futures import ThreadPoolExecutor
from time import sleep

import grpc
import promptlayer
from dotenv import load_dotenv
from loguru import logger

from src import start_bot

load_dotenv()
promptlayer.api_key = os.environ.get("PROMPTLAYER_API_KEY")


def run():
    executor = ThreadPoolExecutor()

    chat_mgr_grpc_url = 'unix:///tmp/chat-mgr.sock' if os.environ.get('CHAT_MGR_GRPC_URL') is None else os.environ.get(
        'CHAT_MGR_GRPC_URL')

    tries = 0
    while tries < 5:
        try:
            with grpc.insecure_channel(chat_mgr_grpc_url) as channel:
                future = executor.submit(start_bot, channel)
                future.result()
        except Exception as e:
            logger.exception(e)
            logger.info(f"Retrying in 5 seconds... ({tries + 1}/5)")
            tries += 1
            sleep(5)


if __name__ == '__main__':
    run()
