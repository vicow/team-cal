from .calendar import CalendarABC
import calendar as pycal


class PrivateCalendar(CalendarABC):

    def __init__(self, user, events):
        super(CalendarABC, self).__init__()
        self.calendar = pycal.Calendar()
        self.events = events
        self.user = user