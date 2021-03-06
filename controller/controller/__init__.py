"""Controller"""

import logging

from ipc import (
    Client,
    Server,
    Rate
)

from common.constants import (
    CONTROLLER_PORT,
    SENSOR_PORT,
    X_DELTA
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Controller(object):
    """Controller model"""

    def __init__(self):
        self.server = Server(CONTROLLER_PORT, 'controller')
        self.sensor = Client(SENSOR_PORT, 'sensor', 1)
        self.rate = Rate(1)  # Hz

    def dispatch(self):
        """Runs a single cycle of the controller process"""

        sensor_msg = self.sensor.recv()
        if not sensor_msg:
            return None
        logger.info("Received sensor position: %s", sensor_msg)
        reported_y = sensor_msg['y']

        # The y axis is deliberately driven to zero,
        # so any reported y axis position is the error.
        error = reported_y
        self.publish({
            'delta_x': X_DELTA,
            'delta_y': -1 * error
        })

        # Sleep to achieve a 1Hz command rate
        self.rate.sleep()

    def publish(self, move_cmd):
        """Publish the move command"""
        self.server.publish(move_cmd)
