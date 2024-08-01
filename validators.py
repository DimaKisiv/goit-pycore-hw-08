from constants import Commands, Messages

def validate_input(command, args):
    if command not in vars(Commands).values():
        raise KeyError #with no message inside of error
    if command in [Commands.ALL, Commands.HELLO, Commands.BIRTHDAYS] and len(args) != 0:
        return Messages.WrongParameters
    elif command in [Commands.PHONE, Commands.SHOW_BIRTHDAY] and len(args) != 1:
        raise IndexError(Messages.EnterUserName) #with message inside of error
    elif command in [Commands.ADD, Commands.ADD_BIRTHDAY] and len(args) != 2:
        raise ValueError(Messages.WrongParameters) #with no message inside of error
    elif command == Commands.CHANGE and len(args) != 3:
        raise ValueError(Messages.GiveNameWithOldAndNewPhones)
    return None