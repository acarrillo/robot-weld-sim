"""Example demonstrating client and server"""

import argparse
import logging

from ipc import (
    Client,
    Server,
    Rate
)

logger = logging.getLogger(__name__)


def do_server():
    server = Server(10020, "example_server")
    rate = Rate(1)

    while True:
        server.publish({"msg": "Hello World!"})
        rate.sleep()


def do_client():
    client = Client(10020, "example_server")

    while True:
        print client.recv()


def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser(description="Demonstrates client or server as an example")
    parser.add_argument('--server', dest='server', action='store_true', help='Demonstrate server')
    parser.add_argument('--client', dest='client', action='store_true', help='Demonstrate client')

    args = parser.parse_args()

    if args.server and not args.client:
        do_server()
    elif args.client and not args.server:
        do_client()
    else:
        raise ValueError("Couldn't satisfy the provided arguments!")


if __name__ == '__main__':
    main()
