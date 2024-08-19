from typing import Callable
from decimal import Decimal
import re

"""
def generator_numbers(text: str):
    first we need to define the patter
    After we need to create a store where will be all number
    yiled them after that
  
 def sum_profit(text: str, func: Callable):
    pass the text into func()
    pull out the result from function  
    sum() the result from func()
    return profit    
    
"""


def generator_numbers(string: str):
    for num in re.findall(r"\d+\.\d+|\d+", string):
        yield num


def sum_profit(string: str, func: Callable):
    filtered_nums = func(string)
    profit = 0
    for num in filtered_nums:
        profit += Decimal(num)
    return profit


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
