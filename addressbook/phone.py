from .exceptions import PhoneNumberException
from .field import Field

class Phone(Field):
    def __init__(self, value):
        self.__validate_number__(value)
        super().__init__(value)
    def __validate_number__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise PhoneNumberException()
    def update_value(self, value):
        self.__validate_number__(value)
        self.value = value