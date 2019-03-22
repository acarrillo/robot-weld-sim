"""Sensor process main entrypoint"""

from sensor import Sensor

def main():
    sensor = Sensor()

    while True:
        sensor.dispatch()


if __name__ == '__main__':
    main()
