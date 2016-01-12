from abc import ABCMeta, abstractmethod

class CalendarABC:
    """
    Abstract class representing a calendar.

    :param  data_dir:    Base data directory
    :type   data_dir:    str
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def example(self):
        """
        Example of abstract method.
        """
        pass