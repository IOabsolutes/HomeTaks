from collections import UserDict


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

        if not value.isalpha():
            raise TypeError("Name couldn't contain numbers")

        super().__init__(value)

    def __str__(self):
        return self.value


class Phone(Field):
    def __init__(self, value):
        if len(value) < 10:
            raise ValueError('Number should be 10 chars')

        if not value.isnumeric():
            raise ValueError("Number should contain only numbers")

        super().__init__(value)

    def __str__(self):
        return self.value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __find_index(self, phone):
        phones = [phone.__str__() for phone in self.phones]
        if phone not in phones:
            raise IndexError("Phone doesn't exist")
        phone_index = phones.index(phone)
        return phone_index, phones

    # реалізація класу
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        phone_index, _ = self.__find_index(phone)
        self.phones.remove(phone_index)

    def edit_phone(self, phone: str, new_phone: str):
        phone_index, _ = self.__find_index(phone)
        self.phones[phone_index] = Phone(new_phone)

    def find_phone(self, phone: str):
        phone_index, phones = self.__find_index(phone)
        return phones[phone_index]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def __init__(self, initial_data=None):
        super().__init__(initial_data)

    def add_record(self, user: Record):
        user_name = user.name.__str__()
        if user_name in self.data:
            raise ValueError('Contact already exists')
        self.data[user_name] = user
        return self.data

    def find(self, name: str):
        if name not in self.data:
            raise ValueError('Contact not found')
        return self.data.get(name)

    def delete(self, name: str):
        if name not in self.data:
            raise IndexError("Element does not exist")
        self.data.pop(name)

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(f'All contacts from AdressBook {book}')

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(f"Johns contact info {john}")  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

print(f'Final AddressBook state {book}')
