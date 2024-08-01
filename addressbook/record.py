from .phone import Phone
from .name import Name
from .birthday import Birthday
from .upcomming import get_congratulation_date

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    def __str__(self):
        str = f"Name: {self.name.value}, Phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday:
            str += f", Birthday: {self.birthday.value.date()}, Congratulation: {self.congratulation_date}"
        return str
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    def remove_phone(self, phone_str):
        phone = self.find_phone(phone_str)
        if phone:
            self.phones.remove(phone)
    def edit_phone(self, old_phone_str, new_phone_str):
        phone = self.find_phone(old_phone_str)
        if phone:
            phone.update_value(new_phone_str)
    def find_phone(self, phone_str):
        return next(iter([p for p in self.phones if p.value == phone_str]), None)
    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)
        self.congratulation_date = get_congratulation_date(self.birthday.value)
    
    