from adressbook import AddressBook
import re


# class
def phone_checker(phone: str) -> None:
    if not re.match(r'^[0-9]+$', phone):
        raise ValueError("Invalid phone number")


def params_checker(params: list[str], min_len: int, func_name: str) -> None:
    if len(params) < min_len:
        raise TypeError(
            "Lack of provided values please provide name and phone" if func_name in ["add_contact",
                                                                                     "change_contact"] else "Please "
                                                                                                            "provide "
                                                                                                            "name")


def key_error_checker(name: str, book: AddressBook, func_name: str) -> None:
    if func_name in ["change_contact", "show_phone", "add_birthday", "show_birthday"]:
        if not book.find(name):
            raise ValueError("Contact name doesn't exist")


def input_error(func):
    def inner(params: list[str], book: AddressBook) -> None:
        try:
            if func.__name__ in ["add_contact", "change_contact"]:
                name = params[0]
                phone = params[1:] if len(params) > 1 else None

                if not re.match(r'^[a-zA-z/s-]+$', name):
                    raise ValueError("Name contain unacceptable charters ")

                if phone:
                    if len(phone) > 1:
                        phone_checker(phone[1])
                    else:
                        phone_checker(phone[0])

                key_error_checker(name, book, func_name=func.__name__)

            elif func.__name__ in ["add_birthday", "show_birthday", "show_phone"]:
                name = params[0]

                key_error_checker(name, book, func.__name__)

            return func(params, book)

        except (IndexError, ValueError, KeyError, TypeError) as e:
            print(e)

    return inner
