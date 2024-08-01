from constants import Messages, Commands
from decorators import input_error
from validators import validate_input
from repository import Repository

def birthdays():
    return Repository.birthdays()

@input_error 
def handle(command, args):
    validate_input(command, args)
    match command:
        case Commands.HELLO:
            return Messages.HowCanIHelpYou
        case Commands.ADD:
            return _add_contact_(args)
        case Commands.CHANGE:
            return _change_contact_(args)
        case Commands.DELETE:
            return _delete_contact_(args)
        case Commands.PHONE:
            return _show_phone_(args)
        case Commands.ALL:
            return _show_all_()
        case Commands.ADD_BIRTHDAY:
            return _add_birthday_(args)
        case Commands.SHOW_BIRTHDAY:
            return _show_birthday_(args)

def _add_contact_(args):
    name, phone = args
    contact = Repository.get_by_name(name)
    if contact is not None:
        if contact.find_phone(phone):
            return Messages.PhoneAlreadyExists
        Repository.add_phone(name, phone)
        return Messages.PhoneAdded 
    else:
        Repository.add_contact(name, phone)
        return Messages.ContactAdded

def _change_contact_(args):
    name, old_phone, new_phone = args
    contact = Repository.get_by_name(name)
    if contact is None:
        return Messages.ContactDoesNotExist
    phone = contact.find_phone(old_phone)
    if phone is None:
        return Messages.ContactDoesNotExist
    if contact.find_phone(new_phone):
        return Messages.PhoneAlreadyExists
    contact.edit_phone(old_phone, new_phone)
    return Messages.ContactChanged

def _show_phone_(args):
    name = args[0]
    contact = Repository.get_by_name(name)
    if contact is None:
        raise KeyError(Messages.ContactDoesNotExist) #throwing error with message here
    return ",".join([p.value for p in contact.phones])

def _delete_contact_(args):
    name = args[0]
    if not Repository.get_by_name(name):
        return Messages.ContactDoesNotExist
    Repository.delete_contact(name)    
    return Messages.ContactDeleted

def _show_all_():
    return "\n".join([str(record) for record in Repository.get_all()])

def _add_birthday_(args):
    name, birthday = args
    contact = Repository.get_by_name(name)
    if not contact:
        return Messages.ContactDoesNotExist
    contact.add_birthday(birthday)
    return Messages.BirthdayAdded

def _show_birthday_(args):
    name = args[0]
    contact = Repository.get_by_name(name)
    if not contact:
        return Messages.ContactDoesNotExist
    if not contact.birthday:
        return Messages.ContactDoesNotHaveBirthdayValue
    return contact.birthday.value.date()