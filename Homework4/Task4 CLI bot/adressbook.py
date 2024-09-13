from collections import UserDict
from datetime import datetime, timedelta, date
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    def __init__(self, value):
        if len(value) == 0:
            raise ValueError('name is required!')

        if len(value) <= 1:
            raise ValueError("Name couldn't be less then 2 chars")

        if not re.match(r'^[A-Za-z\s]+$', value):
            raise TypeError("Name couldn't contain numbers or special characters")

        super().__init__(value)

    def __str__(self):
        return self.value


class Phone(Field):
    def __init__(self, value):
        if len(value) < 9:
            raise ValueError('Number should be 10 chars')

        if not value.isnumeric():
            raise ValueError("Number should contain only numbers")

        super().__init__(value)

    def __str__(self):
        return self.value


class Birthday(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Birthday should be a string")

        try:
            if not re.match(r"^\d{2}.\d{2}.\d{4}$", value):
                raise ValueError

            self.birthday = self.string_to_date(value)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def prepare_user_list(self, user_data):
        prepared_list = []
        for user in user_data:
            prepared_list.append({"name": user["name"], "birthday": self.string_to_date(user["birthday"])})
        return prepared_list

    def string_to_date(self, date_string: str) -> date:
        return datetime.strptime(date_string, "%d.%m.%Y").date()

    def date_to_string(self, date: date) -> str:
        return date.strftime("%d.%m.%Y")

    def _find_next_weekday(self, start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self._find_next_weekday(birthday, 0)
        return birthday

    def get_user_birthday_as_date(self):
        return self.birthday

    def __str__(self):
        return self.date_to_string(self.birthday)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __find_index(self, phone):
        phones = [phone.__str__() for phone in self.phones]
        if phone not in phones:
            raise IndexError("Phone doesn't exist")
        phone_index = phones.index(phone)
        return phone_index, phones

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday.strip())

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        phone_index, _ = self.__find_index(phone)
        self.phones.pop(phone_index)

    def edit_phone(self, phone: str, new_phone: str):
        phone_index, _ = self.__find_index(phone)
        self.phones[phone_index] = Phone(new_phone)

    def find_phone(self, phone: str):
        phone_index, phones = self.__find_index(phone)
        return phones[phone_index]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"


class AddressBook(UserDict):
    def __init__(self, initial_data=None):
        super().__init__(initial_data)

    def add_record(self, user: Record):
        user_name = user.name.__str__()
        if user_name in self.data:
            raise ValueError('Contact already exists')
        self.data[user_name] = user
        return self.data

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name not in self.data:
            raise IndexError("Element does not exist")
        self.data.pop(name)

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for key, value in self.data.items():
            user_birthday = value.birthday.get_user_birthday_as_date()
            birthday_this_year = user_birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= days:
                congratulate_date = value.birthday.adjust_for_weekend(birthday_this_year)

                congratulation_date_str = value.birthday.date_to_string(congratulate_date)

                upcoming_birthdays.append({"name": key, "congratulation_date": congratulation_date_str})
        return upcoming_birthdays

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

