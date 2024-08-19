from actions import show_commands, show_all, show_phone, add_contact, change_contact

storage = {}


def parser_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *params = user_input.split()
    cmd.strip().lower()
    return cmd, *params


def action(command: str, *params: list[str]) -> None:
    match command:
        case "add":
            add_contact(storage, params)

        case "phone":
            show_phone(storage, params)

        case "change":
            change_contact(storage, params)

        case "all":
            show_all(storage)

        case "help":
            show_commands()

        case "close" | "exit":
            print("Good bye!")
            exit()

        case "hello":
            print("How can I help you?")

        case _:
            print("Invalid command")


def main():
    print("Welcome to the assistant bot!")

    while True:
        command = input("Enter a command: ")
        cmd, *params = parser_input(command)
        action(cmd, *params)


if __name__ == "__main__":
    main()
