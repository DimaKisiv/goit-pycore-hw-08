from constants import Messages, Commands
from parser import parse_input
from repository import Repository
import handlers

def main():
    Repository.load_data()
    print(Messages.Wellcome)
    while True:
        command, *args = parse_input(input(Messages.EnterACommand))
        if command == Commands.CLOSE or command == Commands.EXIT:
            Repository.save_data()
            print(Messages.GoodBye)
            break
        if command == Commands.BIRTHDAYS:
            print_birthdays(handlers.birthdays())
        else:
            print(handlers.handle(command, args))

def print_birthdays(celebrate_users_next_week):
    for date_key in celebrate_users_next_week:
            print(f"{date_key}:\n\t{"\n\t".join([i for i in celebrate_users_next_week[date_key]])}")
    
if __name__ == "__main__":
    main()