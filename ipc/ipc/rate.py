"""Contains sleep utility for creating a stable publish rate"""

import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Rate(object):
    """Class for sleeping at stable periodic intervals"""

    def __init__(self, rate):
        """
        Args:
            rate (float): Sleep rate, in Hz
        """
        self.rate = rate
        self._period = 1 / rate  # Seconds
        self._last_sleep = None

    def sleep(self):
        """
        Sleep for the correct amount, based on ``rate``.
        """
        if self._last_sleep is None:
            self._last_sleep = time.time()
        sleep_delta = time.time() - self._last_sleep
        time_to_sleep = max(self._period - sleep_delta, 0)

        time.sleep(time_to_sleep)
        self._last_sleep = time.time()
