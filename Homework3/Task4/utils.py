import re


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


def key_error_checker(name: str, storage: dict, func_name: str) -> None:
    if func_name == "add_contact":
        if storage.get(name):
            raise KeyError("Contact name already exists")
    elif func_name in ["change_contact", "show_phone"]:
        if not storage.get(name):
            raise KeyError("Contact name doesn't exist")


def input_error(func):
    def inner(storage: dict, params: list[str]):
        try:
            if func.__name__ in ["add_contact", "change_contact"]:
                params_checker(params, 2, func_name=func.__name__)

                name, phone = params

                if not re.match(r'^[a-zA-z/s-]+$', name):
                    raise ValueError("Name contain unacceptable charters ")

                phone_checker(phone)

                key_error_checker(name, storage, func_name=func.__name__)

            elif func.__name__ in ["show_phone"]:
                params_checker(params, 1, func_name=func.__name__)

                name = params[0]

                key_error_checker(name, storage, func.__name__)

            return func(storage, params)
        except (IndexError, ValueError, KeyError, TypeError) as e:
            print(e)

    return inner
