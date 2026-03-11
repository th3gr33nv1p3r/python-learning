"""
variables_practice.py

This file contains exercises focused on mastering Python variables.
Topics covered:
- Variable creation
- Data types
- Arithmetic operations
- String formatting
- Basic real-world calculations

Goal:
Build a strong Python foundation for Data Analysis and Data Science.
"""

# Exercise 1 - Basic Variables

name = "Mohamed"
age = 25
career_goal = "Data Analyst"
study_hours_per_day = 2

# print(f"My name is {name}. I am {age} years old.")
# print(f"My goal is to become a {career_goal}.")
# print(f"I study Python {study_hours_per_day} hours per day.")

# Exercise 2 - Swapping Values

x = 10
y = 20

# print(f"Before swap: x = {x}, y = {y}")

# Swap values
x, y = y, x

# print(f"After swap: x = {x}, y = {y}")

# Exercise 3 - User Profile Variables

username = "elitecoder12"
country = "China"
favorite_number = 10
is_learning_python = True

# print("User Profile")
# print("------------")
# print(f"Username: {username}")
# print(f"Country: {country}")
# print(f"Favorite Number: {favorite_number}")
# print(f"Learning Python: {is_learning_python}")

# Exercise 4 - Simple Finance Calculator

monthly_income = 2100
monthly_rent = 500
monthly_food_budget = 100
monthly_transportation = 120

total_expenses = monthly_rent + monthly_food_budget + monthly_transportation
remaining_money = monthly_income - total_expenses

# print(f"Income: ${monthly_income}")
# print(f"Expenses: ${total_expenses}")
# print(f"Remaining Money: ${remaining_money}")

# Exercise 5 - Temperature Converter

celsius = 25
fahrenheit = (celsius * 9/5) + 32

# print(f"Temperature: {celsius}°C")
# print(f"Temperature: {fahrenheit}°F")

# Exercise 6 - Identify Data Types

name = "Alice"
# print(type(name))

age = 30
# print(type(age))

height = 5.7
# print(type(height))

is_programmer = True
# print(type(is_programmer))

# Exercise 7 - String Formatting

product_name = "Tv remote"
price = 30
quantity = 340

total = price * quantity

# print("Receipt")
# print("------------")
# print(f"Product: {product_name}")
# print(f"Price: ${price}")
# print(f"Quantity: {quantity}")
# print(f"Total: ${total}")

# Exercise 8 - Mini Project: Order System

customer_name = "Michael"
item_name = "bag of bagels"
item_price = 4
quantity = 10
tax_rate = 0.08 # 8% tax

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Order Summary")
print("------------")
print(f"Customer: {customer_name}")
print(f"Item: {item_name}")
print(f"Price: ${item_price}")
print(f"Quantity: {quantity}")
print("------------")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: {total}")