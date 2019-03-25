"""Controller main entrypoint"""

import logging
from controller import Controller


def main():
    """Main entrypoint for controller process"""
    logging.basicConfig()
    controller = Controller()

    while True:
        controller.dispatch()


if __name__ == '__main__':
    main()
