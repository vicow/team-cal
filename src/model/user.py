
class User:

    def __init__(self, email, first_name, last_name,
                 private_calendar=None, group_calendars=None, events=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.private_calendar = private_calendar
        self.group_calendars = group_calendars
        self.events = events

    def create_group_calendar(self):
        pass

    def create_event(self, **kwargs ):
        pass

    def add_availabilities(self, event, availabilities):
        pass