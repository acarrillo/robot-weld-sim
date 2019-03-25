"""Robot main"""

import logging
from welder import Welder


def main():
    """Main entrypoint for welder process"""
    logging.basicConfig()

    welder = Welder()
    while True:
        welder.dispatch()


if __name__ == '__main__':
    main()
