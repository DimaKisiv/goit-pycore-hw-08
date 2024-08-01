from .addressbook import AddressBook
from .record import Record

def seed_book(book: AddressBook):
    rec1 = Record("User1")
    rec1.add_phone("1234567890")
    rec1.add_phone("5555555555")
    rec1.add_birthday("26.07.1985")
    book.add_record(rec1)

    rec2 = Record("User2")
    rec2.add_phone("9876543210")
    rec2.add_birthday("27.07.1985")
    book.add_record(rec2)

    rec3 = Record("User3")
    rec3.add_phone("9876543210")
    rec3.add_birthday("28.07.1985")
    book.add_record(rec3)

    rec4 = Record("User4")
    rec4.add_phone("9876543210")
    rec4.add_birthday("29.07.1985")
    book.add_record(rec4)

    rec5 = Record("User5")
    rec5.add_phone("9876543210")
    rec5.add_birthday("30.07.1985")
    book.add_record(rec5)

    rec6 = Record("User6")
    rec6.add_phone("9876543210")
    rec6.add_birthday("31.07.1985")
    book.add_record(rec6)
    
    rec7 = Record("User7")
    rec7.add_phone("9876543210")
    rec7.add_birthday("01.08.2023")
    book.add_record(rec7)

    rec8 = Record("User8")
    rec8.add_phone("9876543210")
    rec8.add_phone("5328563751")
    rec8.add_birthday("01.08.1985")
    book.add_record(rec8)