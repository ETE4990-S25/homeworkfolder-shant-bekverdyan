import time
import math
import sys
time_limit = 20

"""checks if a number is a prime number"""
def prime(n):

    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False
        
    return True

"""finds largest prime number in the given time limit"""
def find_largest(time_limit):

    start_time = time.time()
    end_time = start_time + time_limit
    largest_prime = 0
    number = 0

    while time.time() < end_time:

        if prime(number):
            largest_prime = number
        number += 1

    return largest_prime

"""calculates the nth Fibonacci number"""
def fibonacci(n):

    if n <= 1:
        return n
    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

"""factorial function"""
def factorial(n):

    if n == 0:
        return 1
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

largest_prime = find_largest(time_limit)
print("Largest prime number in 1 minute =", largest_prime)

#got help for this last part :'(
if largest_prime > 0:

    try:
        fibonacci_start_time = time.time()
        fibonacci_end_time = fibonacci_start_time + time_limit
        fibonacci_result = fibonacci(largest_prime)
        fibonacci_elapsed_time = time.time() - fibonacci_start_time
        print("Fibonacci number found. Number too large to display :(") #kept getting error code when trying to display the number
        print("Fibonacci time:", fibonacci_elapsed_time)

    except OverflowError:

        print("Fibonacci too large")

    factorial_start_time = time.time()
    factorial_end_time = factorial_start_time + time_limit
    factorial_result = factorial(4)
    factorial_elapsed_time = time.time() - factorial_start_time
    print("Factorial:", factorial_result)
    print("Factorial time:", factorial_elapsed_time)
else:

    print("No prime number found.")

print("Done")