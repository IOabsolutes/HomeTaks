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
                params_checker(params, 2, func_name=func.__name__)

                name, *phone = params

                if not re.match(r'^[a-zA-z/s-]+$', name):
                    raise ValueError("Name contain unacceptable charters ")

                if len(phone) > 1:
                    phone_checker(phone[1])
                else:
                    phone_checker(phone[0])

                key_error_checker(name, book, func_name=func.__name__)

            elif func.__name__ in ["show_phone"]:
                params_checker(params, 1, func_name=func.__name__)

                name = params[0]

                key_error_checker(name, book, func.__name__)

            elif func.__name__ in ["add_birthday", "show_birthday"]:

                if len(params) < 2:
                    name = params[0]
                else:
                    name, *_ = params

                key_error_checker(name, book, func.__name__)

            return func(params, book)
        except (IndexError, ValueError, KeyError, TypeError) as e:
            print(e)

    return inner
