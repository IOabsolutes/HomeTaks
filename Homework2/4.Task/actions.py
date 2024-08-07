storege = {}


def show_commands() -> None:
    print(
        """
    The avalible commands
    |--------------------|
     1) "hello"
     2) "add [ім'я] [номер телефону]"
     3) "change [ім'я] [новий номер телефону]"
     4) "phone [ім'я]"
     5)"all"
     6)"close"
     """
    )


def add_contact(params: list[str]) -> str:

    try:
        name, phone = params

        if not name or not phone:
            raise ValueError

        if storege.get(name):
            raise Exception

        storege[name] = phone
        return "Contact added."

    except ValueError:
        print("Name and Phone are required")
    except Exception:
        print("The contant with that name already exists")


def change_contact(params: list[str]) -> str:

    try:
        name, phone = params

        if not name or not phone:
            raise ValueError

        contact = storege.get(name)

        if contact:
            storege.update({name: phone})
            return "Contact updated."

        else:
            print("The contant doesn't exist")

    except ValueError:
        print("number is required!")


def show_phone(params: list[str]) -> str:
    try:
        phone = params

        if not phone:
            raise ValueError

        contact = storege.get(phone)

        if contact:
            return f"The phone number --> {storege.get(phone)}"

        else:
            print("The contant doesn't exist")

    except ValueError:
        print("phone couldn't be empty")


def show_all() -> None:
    print("The list of the contacts")
    print("------------------------")
    for name, phone in storege.items():
        print(f"Name: {name}; phone: {phone}")
    print("------------------------")
