from typing import Callable, Dict
from actions import show_commands, add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, \
    birthdays
from adressbook import AddressBook
from book_file_handler import save_data, load_data


def parser_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *params = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, params


class ActionHandler:
    def __init__(self, book: AddressBook):
        self.book = book
        self.actions: Dict[str, Callable] = {
            "add": add_contact,
            "change": change_contact,
            "phone": show_phone,
            "all": show_all,
            "help": show_commands,
            "hello": lambda: print("How can I help you?"),
            "add-birthday": add_birthday,
            "show-birthday": show_birthday,
            "birthdays": birthdays,
        }

    def command_handler(self, cmd: str, params: list[str]) -> None:

        if cmd in ['exit', 'close']:
            print('Good bye!')
            exit()

        action = self.actions.get(cmd)
        if action is None:
            print('Invalid command')
            return

        if cmd in {"hello", "help"}:
            action()
        elif cmd in {"all", "birthdays"}:
            action(self.book)
        elif cmd in {"exit", "close"}:
            print('Good bye!')
            exit()
        else:
            action(params, self.book)


def main():
    print("Welcome to the assistant bot!")

    book = load_data()
    action = ActionHandler(book)
    try:
        while True:
            command = input("Enter a command: ")
            try:
                cmd, params = parser_input(command)
            except (ValueError, TypeError):
                print('No command, try again')
            else:
                action.command_handler(cmd, params)
    finally:
        save_data(book)


if __name__ == "__main__":
    main()
