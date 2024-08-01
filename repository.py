import pickle
from addressbook import AddressBook, Record, seed_book

class Repository:
    ADDRBOOK_FILENAME="addressbook.pkl"
    book = AddressBook()

    @staticmethod
    def save_data():
        with open(Repository.ADDRBOOK_FILENAME, "wb") as f:
            pickle.dump(Repository.book, f)
    
    def load_data():
        try:
            with open(Repository.ADDRBOOK_FILENAME, "rb") as f:
                Repository.book = pickle.load(f)
        except FileNotFoundError:
            Repository.seed_data()
            return Repository.book

    @staticmethod
    def seed_data():
        seed_book(Repository.book)

    @staticmethod
    def add_contact(name, phone):
        contact = Record(name)
        contact.add_phone(phone)
        Repository.book.add_record(contact)

    @staticmethod
    def add_phone(name, phone):
        contact = Repository.book.find(name) 
        if contact:
            contact.add_phone(phone)

    @staticmethod
    def get_by_name(name):
        return Repository.book.find(name)

    @staticmethod
    def delete_contact(name):
        Repository.book.delete(name)
    
    @staticmethod 
    def get_all():
        return Repository.book.get_all()
    
    @staticmethod
    def add_birthday(name, birthday):
        contact = Repository.book.find(name)
        if contact:
            contact.add_birthday(birthday)
    
    @staticmethod
    def birthdays():
        return Repository.book.get_next_week_celebrate_users()