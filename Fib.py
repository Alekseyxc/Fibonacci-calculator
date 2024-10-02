def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Приклад використання
n = 10
fib_sequence = list(fibonacci_generator(n))
print(f"Перші {n} чисел Фібоначчі: {fib_sequence}")