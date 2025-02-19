#1

def square(num):
    return num ** 2
print(square(6))

#2
def sumup(numbers):
    return sum(numbers)
print(sumup([1, 2, 3, 4, 5, 6]))

#3

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(prime(9))
print(prime(3))