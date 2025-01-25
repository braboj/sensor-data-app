import random
from abc import abstractmethod, ABC


class SensorAbc(ABC):
    """Abstract base class for sensors."""

    @property
    @abstractmethod
    def tag(self):
        """The tag name of the sensor."""
        raise NotImplementedError

    @property
    @abstractmethod
    def low_limit(self):
        """The low limit of the sensor."""
        raise NotImplementedError

    @property
    @abstractmethod
    def high_limit(self):
        """The high limit of the sensor."""
        raise NotImplementedError

    @abstractmethod
    def read(self):
        """Read the sensor data.

        Returns:
            int | float: The sensor data.
        """
        raise NotImplementedError


class SensorBase(object):
    """Base class for field sensors handling."""

    def __init__(self, tag, low_limit, high_limit):
        """Initialize the sensor with a tag name.

        The low and high limits are used to generate random data within the
        specified range for the sensor.

        Example:

            # Position sensor with 3 states (-1, 0, 1)
            position = SensorBase('ZSS1R01A', low_limit=-1, high_limit=1)

            # Temperature sensor with a range of 0 to 100 degC
            temperature = SensorBase('TIS1P01A', low_limit=0, high_limit=100)

        Args:
            tag (str)                  : The tag name of the sensor.
            low_limit (int | float)    : The low limit of the sensor.
            high_limit (int | float)   : The high limit of the sensor.
        """

        self._tag = tag
        self._low_limit = low_limit
        self._high_limit = high_limit

    @property
    def tag(self):
        """The tag name of the sensor."""
        return self._tag

    @property
    def low_limit(self):
        """The low limit of the sensor."""
        return self._low_limit

    @property
    def high_limit(self):
        """The high limit of the sensor."""
        return self._high_limit


class DiscreteSensor(SensorBase, SensorAbc):
    """Discete sensors to generate random binary data."""

    def read(self):
        """Read the discrete sensor data."""
        return random.randint(self.low_limit, self.high_limit)


class AnalogSensor(SensorBase, SensorAbc):
    """Analog sensors to generate random float data."""

    def read(self):
        """Read the analog sensor data."""
        return random.uniform(self.low_limit, self.high_limit)


def demo():

    import time

    # Create the sensor objects
    position = DiscreteSensor('ZSS1R01A', low_limit=-1, high_limit=1)
    temperature = AnalogSensor('TIS1P01A', low_limit=0, high_limit=100)

    # Sample the sensor data
    for _ in range(10):
        print(position.read())
        print(temperature.read())
        time.sleep(1)

if __name__ == '__main__':
    demo()
