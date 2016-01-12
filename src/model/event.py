
class Event:

    def __init__(self, name, start_date, stop_date,
                 attendees=None, description=None, location=None):
        self.name = name
        self.start_date = start_date
        self.stop_date = stop_date
        self.description = description
        self.location = location
        if attendees is None:
            self.attendees = []
        else:
            self.attendees = attendees

    def match_dates(self):
        pass