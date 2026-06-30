""" What is DSA?

Think of Data Structures and Algorithms (DSA) like organizing a kitchen:

Data Structure: 

                How you store and organize your ingredients (e.g., in jars, boxes, or shelves) so they are easy to find.

Algorithm: 
            The step-by-step recipe you follow to cook a meal using those ingredients.

In short: 
            Data Structures hold the data, and Algorithms solve the problem.

1. Data Structures in Python

Python has built-in ways to store data. Here are the four most common ones:

Lists []
An ordered collection of items that you can change. Like a grocery list."""

fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Adds to the end

"""Tuples ()
Just like a list, but you cannot change it after creation. Like your birthdate."""

coordinates = (10, 20)

"""Dictionaries {}
Stores data in Key : Value pairs. Like a real dictionary where you look up a word (Key) to find its meaning (Value)."""

user = {"name": "Kamran", "role": "Developer"}
print(user["name"])  # Outputs: Kamran

"""Sets {}
A collection of unique items with no duplicates."""

unique_numbers = {1, 2, 2, 3}  # Automatically becomes {1, 2, 3}

"""2. What makes an Algorithm "Good"? 
(Big O Notation)When writing code to solve a problem, you want it to be fast and use less memory. We measure this using Big O Notation. It tells us how the execution time grows as our data gets bigger.$O(1)$ 

Constant Time (Fastest): 
                        The code takes the same time no matter how much data you have. (Example: Looking up an item in a dictionary).$O(N)$ - Linear Time (Fair): The time grows directly with the size of the data. (Example: Using a for loop to look through a list of $N$ items).$O(N^2)$ 

Quadratic Time (Slow): 
                        The time grows very fast. (Example: A loop inside another loop).3. Two Simple Algorithms Everyone Learns FirstLinear Search ($O(N)$)Looking for an item by checking every single element from start to finish."""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found it!
    return -1  # Not found

"""Bubble Sort ($O(N^2)$)A simple sorting algorithm that steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. It repeats this until the list is sorted.

Why learn DSA?Writing code that works is easy, but writing code that runs fast and efficiently requires DSA. It changes how you think about solving problems!"""