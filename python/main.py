import asyncio
import logging
import os
import sys
from typing import Union

import grpc
from grpc_health.v1 import health, health_pb2_grpc
from grpc_reflection.v1alpha import reflection

from handler import HandlerServicer

from dotenv import load_dotenv

load_dotenv()

server: Union[grpc.aio.Server, None] = None
uds_path: Union[str, None] = None


async def main():
    oak = os.environ.get("OPENAI_API_KEY")
    if oak is None or oak == "":
        logging.error("OPENAI_API_KEY is not set")
        sys.exit(1)

    svc = HandlerServicer()
    server = grpc.aio.server()
    svc.attach_to_server(server)
    health_pb2_grpc.add_HealthServicer_to_server(health.HealthServicer(), server)

    reflection.enable_server_reflection((
        svc.full_name(),
        reflection.SERVICE_NAME,
        health.SERVICE_NAME
    ), server)

    global uds_path

    uds_path = f'/tmp/wa-python-handler.sock'
    if os.path.exists(uds_path):
        logging.warning(f'Removing existing UDS path: {uds_path}')
        os.remove(uds_path)

    server.add_insecure_port(f'unix://{uds_path}')
    logging.info(f'Starting server on {uds_path}')
    await server.start()
    await server.wait_for_termination()


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace('\n', '')
        return result


handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
root.addHandler(handler)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logging.error('Terminated by user: Shutting down')
        if server is not None:
            server.stop(5)
        if uds_path is not None:
            os.remove(uds_path)
        sys.exit(7)
    except Exception as e:
        logging.exception(e)
