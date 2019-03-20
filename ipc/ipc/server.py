"""Common server"""

import zmq
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Server(object):
    """Publish server"""

    def __init__(self, port, server_name):
        assert " " not in server_name
        self.port = port
        self.name = server_name

        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.bind("tcp://*:{}".format(self.port))
        logger.info("Publish server [{}] ready at port {}".format(
            self.name, self.port))

    def publish(self, data):
        """Publish a message

        Args:
            data (dict): Data dictionary to publish
        """
        payload = "{} {}".format(self.name, json.dumps(data))
        logger.debug("Sending payload: {}".format(data))
        self.socket.send(payload)
