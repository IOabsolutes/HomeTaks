from utils import input_error


def show_commands() -> None:
    print(
        """
    The available commands
    |--------------------|
     1) "hello"
     2) "add [ім'я] [номер телефону]"
     3) "change [ім'я] [новий номер телефону]"
     4) "phone [ім'я]"
     5)"all"
     6)"close"
     """
    )


@input_error
def add_contact(storage: dict, params: list[str]) -> None:
    name, phone = params
    storage[name] = phone
    print("Contact added.")


@input_error
def change_contact(storage: dict, params: list[str]) -> None:
    name, phone = params
    storage.update({name: phone})
    print("Contact updated.")


@input_error
def show_phone(storage: dict, params: list[str]) -> str:
    user = params
    print(f"The phone number --> {storage.get(user)}")


def show_all(storage: dict) -> None:
    print("The list of the contacts")
    print("------------------------")
    for name, phone in storage.items():
        print(f"Name: {name}; phone: {phone}")
    print("------------------------")
