from datetime import datetime
import re


def get_days_from_today(date_str: str) -> int:

    if not isinstance(date_str, str):
        raise TypeError("Input must be a string")

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        raise ValueError("Invalid format should be YYYY-MM-DD")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        cur_date = datetime.today().date()
        return (cur_date - date).days

    except ValueError as e:
        print(f"Invalid value {e}")

    except TypeError:
        print("Invalid Type should be string")


import random


def get_numbers_ticket(min, max, quantity):

    if (min < 1 or max > 1000) or (quantity < min or quantity > max):
        return []

    num_set = set()

    for num in range(quantity):
        random_num = random.randint(min, max)
        num_set.add(random_num)
    list_num = list(num_set)

    return sorted(list_num)


lottery_numbers = get_numbers_ticket(1, 49, 6)


import re


def normalize_phone(phone: str) -> list[str]:

    pattern = r"[a-zA-Z;,\-:!\.\/\\()]"
    replacment = ""
    cleared_number = re.sub(pattern, replacment, phone).replace(" ", "")
    if re.match(r"^\+380", cleared_number):
        return cleared_number
    elif re.match(r"^(380)", cleared_number):
        return "+" + cleared_number
    else:
        return "+38" + cleared_number
