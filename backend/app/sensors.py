import random
from abc import abstractmethod, ABC


class _SensorAbc(ABC):
    """Abstract class for sensors."""

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


class _SensorBase(object):
    """Base class for field sensors handling."""

    def __init__(self, tag, low_limit, high_limit):
        """Initialize the sensor with a tag name."""

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


class DiscreteSensor(_SensorBase, _SensorAbc):
    """Discete sensors to generate random binary data."""

    def __init__(self, tag, low_limit=0, high_limit=1):
        """Initialize the discrete sensor with a tag name.

        Args:
            tag (str)                  : The tag name of the sensor.
            low_limit (int)            : The low limit of the sensor.
            high_limit (int)           : The high limit of the sensor.

        Example:
            # Position sensor with 3 states (-1: left, 0: center, 1: right)
            sensor = DiscreteSensor('ZSS1R01A', low_limit=-1, high_limit=1)

            # Vibration sensor with 2 states (0: off, 1: on)
            sensor = DiscreteSensor('VSS1R01A', low_limit=0, high_limit=1)
        """

        super(DiscreteSensor, self).__init__(tag, low_limit, high_limit)

    def read(self):
        """Read the discrete sensor data."""
        return random.randint(self.low_limit, self.high_limit)


class AnalogSensor(_SensorBase, _SensorAbc):
    """Analog sensors to generate random float data.

    Args:
        tag (str)                  : The tag name of the sensor.
        low_limit (float)          : The low limit of the sensor.
        high_limit (float)         : The high limit of the sensor.

    Example:
        # Temperature sensor with a range of 0-100 degrees
        sensor = AnalogSensor('TIS1P01A', low_limit=0, high_limit=100)

        # Pressure sensor with a range of 0-10 bar
        sensor = AnalogSensor('PIS1P01A', low_limit=0, high_limit=10)
    """

    def __init__(self, tag, low_limit=0.0, high_limit=100.0):
        """Initialize the analog sensor with a tag name.

        Args:
            tag (str)            : The tag name of the sensor.
            low_limit  (float)   : The low limit of the sensor.
            high_limit (float)   : The high limit of the sensor.
        """
        super(AnalogSensor, self).__init__(tag, low_limit, high_limit)

    def read(self):
        """Read the analog sensor data."""
        return random.uniform(self.low_limit, self.high_limit)


__all__ = ['DiscreteSensor', 'AnalogSensor']


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
