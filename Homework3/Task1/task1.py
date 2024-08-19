def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        # if n in cache just pull out it return
        if n in cache:
            return cache.get(n)
        if n < 0:
            return 0
        elif n == 1:
            return n
        # add new n value to the cache and return it
        else:
            cache.update({n: fibonacci(n - 1) + fibonacci(n - 2)})
            return cache.get(n)

    return fibonacci


fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(9))
print(fib(25))
print(fib(100))
