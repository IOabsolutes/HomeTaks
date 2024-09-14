from utils import input_error
from adressbook import AddressBook, Record


@input_error
def add_contact(params, book: AddressBook) -> None:
    name = params[0]
    phone = params[1] if len(params) > 1 else None
    record = book.find(name)
    message = 'Contact updated.'
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    print(message)


@input_error
def change_contact(params, book: AddressBook) -> None:
    name, old_phone, new_phone = params
    user = book.find(name)
    user.edit_phone(old_phone, new_phone)
    print("Contact updated.")


@input_error
def show_phone(params, book: AddressBook) -> None:
    user = params[0]
    record = book.find(user)
    print(f"The phone number --> {[phone.__str__() for phone in record.phones]}")


def show_all(book: AddressBook) -> None:
    print("The list of the contacts")
    print("------------------------")
    print(f"{book}")
    print("------------------------")


def show_commands() -> None:
    print(
        """
    The available commands
    |----------------------------------------------------------------------------------------------------|
    1) add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером, або телефонний номер к контакту який вже існує.
    2) change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.
    3) phone [ім'я]: Показати телефонні номери для вказаного контакту.
    4) all: Показати всі контакти в адресній книзі.
    5) add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
    6) show-birthday [ім'я]: Показати дату народження для вказаного контакту.
    7) birthdays: Показати дні народження на найближчі 7 днів з датами, коли їх треба привітати.
    8) hello: Отримати вітання від бота.
    9) close або exit: Закрити програму.
    |----------------------------------------------------------------------------------------------------|
     """
    )


@input_error
def add_birthday(params, book: AddressBook):
    name, birthday = params
    record = book.find(name)
    record.add_birthday(birthday)
    print("Birthday added.")


@input_error
def show_birthday(params, book: AddressBook):
    name = params[0]
    record = book.find(name)
    print(f"The birthday --> {record.birthday}")


def birthdays(book: AddressBook) -> None:
    for user in book.get_upcoming_birthdays():
        print(f"{user['name']}: {user['congratulation_date']}")
