import calendar as pycal
from .calendar import CalendarABC


class GroupCalendar(CalendarABC):

    def __init__(self, name, users, events=None):
        super(CalendarABC, self).__init__()
        self.calendar = pycal.Calendar()
        self.name = name
        self.users = users
        self.events = events
