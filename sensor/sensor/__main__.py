"""Sensor process main entrypoint"""

import logging
from sensor import Sensor

def main():
    logging.basicConfig()
    sensor = Sensor()

    while True:
        sensor.dispatch()


if __name__ == '__main__':
    main()
