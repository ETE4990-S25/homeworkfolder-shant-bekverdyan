# %% [markdown]
# # Lab 3 - Files and Functions
# 

# %% [markdown]
# ## Warm-up 
# 
# Part 1:
# Write a python file that can be imported.

# %%
# Code goes here

def greet(name):
        return f"Hello, {name}!"

if __name__ == "__main__":
    print("Hello, Bronco!")




# %% [markdown]
# 
# Part 2: 
# Using the following as a starting point create a python file that will take in a a name and
# a list of names and tell you if that name is in the list.

# %%
# Code goes here

def name_check(name, name_list):
    return name in name_list

if __name__ == "__main__":

    name_list = ["Mr. Powers", "Billy Bot", "Shant"]
    search = input("Search name from list: ")

    if name_check(search, name_list):
        print(f"{search} is included in the list.")
    else:
        print(f"{search} is not included in the list.")
    

# %% [markdown]
# # Main Lab
# 
# Take time to begin working with your partner on your project. Begin to plan out how you would like your game to feel. Remember this is a text-based game. This can be any game you would like 
# 
#     Please stay away from games or software like poker or 21 as these tend to be boring to code and hard to add more to later on, and obviously games that may get you reported by the university.
# 
# 
# ## Part 1:
# 
# Divide up your code and begin writing the code.
# 
# Keep in mind that when you write your code you will need to be interfacing with your partners code, loading in your player, tools/items/etc, interfacing with the world, monsters and so on. So plan accordingly.
# 
# 
# While we have not gotten to classes take some time to try and code some simple classes. 
# Here is an example:
# ```python 
# 
# #Good
# class Sharps(object):
#     """Create a sharp weapon"""
#     def __init__(self, name, length, age=1, damage=0):
#         """ Initialize name, age, and length damage attributes."""
#         self.name = name
#         self.age = age
#         self.length = length
#         self.damage = damage
#     def do_damage(self, target):
#         target = target - self.damage
# 
# class dager(Sharps):
#     """ makes a dager"""
#     def __init__(self, name, length, age=1, damage=0):
#         """sets up a dagger"""
#         super().__init__(self, name, length, age, damage))
#         self.poision = True
# ```
# 

# %%
#inventory display
import json

with open('ItemData.json') as f:
    items = json.load (f)

print(json.dumps(items, indent=2))


# %% [markdown]
# 

# %% [markdown]
# 


