"""Common client"""

import zmq
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Client(object):
    """Subscribe client"""

    def __init__(self, port, topic, timeout=None):
        """
        Args:
            port (int): Server port to connect to
            topic (str): Name of the topic to filter on
            timeout (float): Optional recv() timeout in seconds. If
                not provided, will block indefinitely.
        """
        self.port = port
        self.timeout = timeout

        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, topic)
        self.socket.setsockopt(zmq.RCVTIMEO, -1 if timeout is None else 1000 * timeout)
        self.socket.connect("tcp://localhost:{}".format(self.port))
        logger.info("Client connected at port {}".format(self.port))

        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)

    def recv(self):
        """Waits ``self.timeout`` seconds for a message, then returns
        the received messaged as a dict. If ``self.timeout`` is reached
        without a message, ``None`` is returned.,
        """

        try:
            raw = self.socket.recv()
        except zmq.error.Again:
            return None
        delimiter = raw.find(" ")
        raw_data = raw[delimiter:]
        return json.loads(raw_data)
