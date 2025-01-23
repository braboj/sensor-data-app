import random


class SensorBase(object):

    def __init__(self, tag):
        self._tag = tag
        self._sample_time = 1
        self._low_limit = 0
        self._high_limit = 1

    @property
    def tag(self):
        return self._tag

    def set_low_limit(self, low_limit):
        self._low_limit = low_limit
        return self

    def set_high_limit(self, high_limit):
        self._high_limit = high_limit
        return self

    def set_sample_time(self, sample_time):
        self._sample_time = sample_time
        return self


class DiscreteSensor(SensorBase):
    """Discete sensors to generate random binary data."""

    def read(self):
        return random.randint(self._low_limit, self._high_limit)


class AnalogSensor(SensorBase):
    """Analog sensors to generate random float data."""

    def read(self):
        return random.uniform(self._low_limit, self._high_limit)


def demo():

    import time

    sensor = DiscreteSensor('temperature')

    for _ in range(5):
        print(sensor.read())
        time.sleep(1)


    sensor = AnalogSensor('temperature')

    for _ in range(5):
        print(sensor.read())
        time.sleep(1)

if __name__ == '__main__':
    demo()
