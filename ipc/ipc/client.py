"""Common client"""

import zmq
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Client(object):
    """Subscribe client"""

    def __init__(self, port, topic):
        """
        Args:
            port (int): Server port to connect to
            topic (str): Name of the topic to filter on
        """
        self.port = port

        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, topic)
        self.socket.connect("tcp://localhost:{}".format(self.port))
        logger.info("Client connected at port {}".format(self.port))

    def recv(self):
        raw = self.socket.recv()
        delimiter = raw.find(" ")
        topic = raw[0:delimiter]
        raw_data = raw[delimiter:]
        return json.loads(raw_data)
