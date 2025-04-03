import time
import math

def is_prime(n):
    
    """checks if a number is a prime number"""

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime(time_limit):

    """finds largest prime number in the given time limit"""

    start_time = time.time()
    end_time = start_time + time_limit

    largest_prime = 0
    number = 0

    while time.time() < end_time:
        if is_prime(number):
            largest_prime = number
        number += 1

    return largest_prime

def fibonacci(n):
    
    """calculates the nth Fibonacci number."""

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
