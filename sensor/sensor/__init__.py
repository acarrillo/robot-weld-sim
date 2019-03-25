"""End effector sensor"""


import logging
from ipc import (
    Client,
    Server
)

from common.constants import (
    WELDER_PORT,
    SENSOR_PORT
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Sensor(object):
    """Sensor model"""

    def __init__(self):
        self.server = Server(SENSOR_PORT, 'sensor')
        self.welder = Client(WELDER_PORT, 'welder', 1)

    def dispatch(self):
        """Execute a single cycle of the sensor process"""

        # Of course the sensor does not have direct knowledge
        # of the end effector's position. But to model the sensor's
        # behavior, it needs to be based on the truth of the
        # welder's actual position.
        welder_msg = self.welder.recv()
        if not welder_msg:
            return None
        self.publish({
            'x': welder_msg['x'],
            'y': welder_msg['y']
        })

    def publish(self, data):
        """Publish a sensor output message"""
        self.server.publish(data)
