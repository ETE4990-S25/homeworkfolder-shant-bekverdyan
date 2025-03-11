# %% [markdown]
# Your name goes here Pleaese

# %% [markdown]
# ## Objective:
# The objective of this assignment is to practice using Functional Programing.
# 
# ## Instructions:
# 
# Using everything we learned to day about Functional Programing, lambda and itters create one of each of the following:
# -  Basic Lambda Function
#     - Create a lambda function that takes one arguments and returns even or odd.
# - Advanced lambda Function
#     - Create a lambda function that takes a list and returns their sum 
# - Sorting with Lambda
# - Filtering with Lambda - `filter()` 
# - Mapping with Lambda - `map()`
# - Reducing with Lambda -  `reduce()` 
# - Enumerate with or without Lambda - `enumerate()`
# - zip with or without lambda (may combine enumerate like in class) - `zip()`
# 
# Submit the file as a .py 
# 
# 
# 

# %% [markdown]
# 

# %%
from functools import reduce

"""basic lambda function, determines if number is even or odd"""
even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(f"67 is {even_odd}")
print(f"80 is {even_odd}")

"""advanced lambda function, adding"""
add_numbers = lambda numbers: sum(numbers)
numbers_list = [10, 14, 63, 121] #208
print(f"Sum of {numbers_list} is {add_numbers(numbers_list)}")

"""sorting, sorts Top Gear crew from youngest to oldest"""
people = [("Jeremy Clarkson", 64), ("The Stig", 26),  ("James May", 62), ("Richard Hammond", 55)]
sort_age = sorted(people, key=lambda person: person[1])
print (f"Top Gear crew sorted by age: {sort_age}")

"""filter, filter and displays numbers divisible by 3 from list"""
numbers = [34, 78, 99, 101, 10403, 21, 6, 9]
divisible_numbers = list(filter(lambda num: num % 3 == 0, numbers))
print(f"Odd numbers: {divisible_numbers}")

"""mapping, squares all numbers in list"""
sq_num = [2, 9, 10, 12, 15]
square_numbers = list(map(lambda x: x**2, sq_num))
print(f"Squared numbers: {square_numbers}")

"""reducing, gives product (uses same numbers from mapping)"""
product = reduce(lambda x, y: x * y, sq_num)
print(f"Product: {product}")

"""enumerate, counts item in list"""
cars = ["2001 BMW M5", "1991 BMW 318i", "2014 Volkswagon Touareg TDI"]
for index, vehicles in enumerate(cars):
    print(f"Index {index}: {vehicles}")

"""zip, combines two lists (cars and people)"""
combined = list(zip(cars, people))
print(f"Combined lists: {combined}")



