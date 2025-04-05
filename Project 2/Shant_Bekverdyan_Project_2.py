import time
import threading
import asyncio
import concurrent.futures

time_limit = 180

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

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

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a+ b
    return b

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

async def async_fibonacci(n):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, fibonacci, n)

async def async_factorial(n):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, factorial, n)

def threaded_calculations(largest_prime):
    print("Threaded Calculations:")
    if largest_prime > 0:
        try:
            fibonacci_start_time = time.time()
            fibonacci_result = fibonacci(largest_prime)
            fibonacci_time = time.time() - fibonacci_start_time
            print("Fibonacci number found. (Threaded) Number too large to display :(")
            print("Fibonacci time (Threaded):", fibonacci_time)

        except OverflowError:
            print("Fibonacci too large (Threaded)")

        factorial_start_time = time.time()
        factorial_result = factorial(4)
        factorial_time = time.time() - factorial_start_time
        print("Factorial (Threaded):", factorial_result)
        print("Factorial time (Threaded):", factorial_time)
    else:
        print("No prime number found (Threaded).")

async def async_calculations(largest_prime):
    print("\nAsync Calculations:")
    if largest_prime > 0:
        try:
            fibonacci_start_time = time.time()
            fibonacci_result = await async_fibonacci(largest_prime)
            fibonacci_elapsed_time = time.time() - fibonacci_start_time
            print("Fibonacci number found. Number too large to display :(")
            print("Fibonacci time (Async):", fibonacci_elapsed_time)

        except OverflowError:
            print("Fibonacci too large (Async)")

        factorial_start_time = time.time()
        factorial_result = await async_factorial(4)
        factorial_elapsed_time = time.time() - factorial_start_time
        print("Factorial (Async):", factorial_result)
        print("Factorial time (Async):", factorial_elapsed_time)
    else:
        print("No prime number found (Async).")

def single_threaded_calculations(largest_prime):
    print("\nSingle-Threaded Calculations:")
    if largest_prime > 0:
        try:
            fibonacci_start_time = time.time()
            fibonacci_result = fibonacci(largest_prime)
            fibonacci_time = time.time() - fibonacci_start_time
            print("Fibonacci number found. (Single-Threaded) Number too large to display :(")
            print("Fibonacci time (Single-Threaded):", fibonacci_time)

        except OverflowError:
            print("Fibonacci too large (Single-Threaded)")

        factorial_start_time = time.time()
        factorial_result = factorial(4)
        factorial_time = time.time() - factorial_start_time
        print("Factorial (Single-Threaded):", factorial_result)
        print("Factorial time (Single-Threaded):", factorial_time)
    else:
        print("No prime number found (Single-Threaded).")

async def main():
    largest_prime = find_largest(time_limit)
    print("Largest prime number in", time_limit, "seconds =", largest_prime)

    thread = threading.Thread(target=threaded_calculations, args=(largest_prime,))
    thread.start()
    thread.join()

    await async_calculations(largest_prime)

    single_threaded_calculations(largest_prime)

    print("\nDone")

if __name__ == "__main__":
    asyncio.run(main())