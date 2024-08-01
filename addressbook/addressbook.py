from collections import UserDict
from .record import Record
from .upcomming import get_next_week_dates, get_upcoming_birthdays_users

class AddressBook(UserDict):
    def get_all(self):
        return list(self.data.values())
    def add_record(self, record):
        self.data[record.name.value] = record
    def find(self, name) -> Record:
        record = self.data.get(name)
        return record
    def delete(self, name):
         if self.data.get(name):
            self.data.pop(name)
    def get_next_week_celebrate_users(self):
        upcoming_users = get_upcoming_birthdays_users(list(self.data.values()))
        next_week = get_next_week_dates()
        sorted_by_week_days = {}
        for week_day in next_week:
            sorted_by_week_days[week_day.strftime("%A")] = [str(user) for user in upcoming_users if user.congratulation_date == week_day.date()]
        return sorted_by_week_days