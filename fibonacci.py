# Числа Фибоначчи — последовательность, в которой первые два числа равны единице,
# а все последующие — сумме двух предыдущих.


def fib(n):
    if n == 1 or n == 2:  # условие выхода
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # рекурсивный вызов


index = int(input('Введите номер числа Фибоначчи: '))
print(fib(index))
