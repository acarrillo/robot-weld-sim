"""Robot base"""

import json
import random

from common.constants import (
    WELDER_PORT,
    CONTROLLER_PORT,
    MAX_Y_ERROR
)

from ipc import (
    Client,
    Server
)


class Welder(object):
    """Welder model"""

    def __init__(self):
        self.server = Server(WELDER_PORT, 'welder')
        self.controller = Client(CONTROLLER_PORT, 'controller')

        self.x = 0
        self.y = 0

    def dispatch(self):
        """Runs a single cycle of the welder process"""

        # Grab the latest move command
        move_cmd = self.controller.recv()

        # Apply it
        self.drive(move_cmd)

        # Publish state
        self.publish()

    def drive(self, move_cmd):
        """Takes a drive command and applies it"""
        delta_x = move_cmd['delta_x']
        delta_y = move_cmd['delta_y'] + (random.random() * MAX_Y_ERROR)

        self.x += delta_x
        self.y += delta_y

    @property
    def state(self):
        """Returns the current state in a serializable
        format"""
        return {
            'x': self.x,
            'y': self.y,
        }

    def publish(self):
        """Publish a welder state update"""
        self.server.publish(self.state)
