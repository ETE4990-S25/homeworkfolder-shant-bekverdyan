import time
import math
time_limit = 60

def prime(n):
    
    """checks if a number is a prime number"""

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest(time_limit):

    """finds largest prime number in the given time limit"""

    start_time = time.time()
    end_time = start_time + time_limit
    largest_prime = 0
    number = 0

    while time.time() < end_time:
        if prime(number):
            largest_prime = number
        number += 1
    return largest_prime

def fibonacci(n):
    
    """calculates the nth Fibonacci number"""

    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial(n):
    
    """factorial function"""

    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

largest_prime = find_largest(time_limit)
print("Largest prime number in one minute:", largest_prime)

#got help for this last part :'(
if largest_prime > 0:
    fibonacci_result = fibonacci(largest_prime)
    factorial_result = factorial(5)
    print("Fibonacci:", fibonacci_result)
    print("Factorial:", factorial_result)
else:
    print("No prime number found.")