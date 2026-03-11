"""
operators_practice.py

This file contains exercises and mini problems demonstrating Python operators.
Topics covered:
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Identity Operators
- Membership Operators

The exercises use small data-analysis style scenarios to simulate
real-world situations such as revenue tracking, dataset validation,
and conversion rate analysis.
"""

# 1. Arithmetic Operators

# Exercise 1

a = 15
b = 4

# Find the sum of a and b
print("Sum:", a + b)
# Find the modulus
print("Modulus:", a %b )
# Find the integer division result
print("Floor Division:", a // b)
# Raise a to the power of b
print("Power:", a ** b)

# Exercise 2: a data analyst tracks daily website visits

monday = 120
tuesday = 135
wednesday = 98

# 1. Calculate the total visits.
print("Sum:", monday + tuesday + wednesday)

# 2. Calculate the average visits.
print("Average:", (monday + tuesday + wednesday) / 3)

# 3. Calculate how many more visits Tuesday had than Wednesday.
print("Difference:", tuesday - wednesday)


# Exercise 3: You have 245 data records and want to divide them into batches of 20.

# How many full batches can you create?
print("Floor Division:", 245 // 20)
# How many records remain?
print("Modulus:", 245 % 20)

# 2. Comparison Operators

# Exercise 4

sales_today = 540
sales_yesterday = 600

# 1. Check if today's sales are greater than yesterday's.
print(sales_today > sales_yesterday)
# 2. Check if they are equal.
print(sales_today == sales_yesterday)
# 3. Check if today's sales are less than or equal to yesterday's.
print(sales_today <= sales_yesterday)

# Exercise 5: A data set requires at least 1000 rows for analysis.
rows = 850

# Write a comparison that checks if the dataset is large enough.
print(rows >= 1000)


# 3. Logical Operators

# Exercise 6 

# A dataset is valid if: 
# (1) It has more than 500 rows 
# (2) It has less than 50 missing values
rows = 650
missing_values = 42

# Check if the dataset is valid.
if rows > 500 and missing_values < 50:
    print("Dataset is valid")
else:
    print("Dataset needs cleaning")

# Exercise 7

# A user qualifies for a premium account if: 
# (1) They are over 18 
# (2) OR they have parental permission
age = 16
parent_permission = True

# Check if the user qualifies.
if age > 18 or parent_permission:
    print("User qualifies for a premium account")
else:
    print("User does not qualify")


# 4. Assignment Operators

# Exercise 8
score = 50
# Add 10
score += 10 
# Multiply by 2
score *= 2
# Subtract 15
score -= 15
print(score)

# Exercise 9: You track total revenue
revenue = 1000

# Apply the following updates:
# 1. Add 250
revenue += 250
# 2. Multiply by 1.10(10% growth)
revenue *= 1.10
# 3. Subtract 100
revenue -= 100
print(revenue)


# 5. Identity Operators

# Exercise 10
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Check if a is the same object as b
print(a is b)
# Check if a is the same object as c
print(a is c)


# 6. Membership Operators

# Exercise 11
columns = ["name", "age", "salary", "Department"]

# Check if "salary" is in the list.
print("salary" in columns)
# Check if "email" is in the list.
print("email" in columns)

# Exercise 12
categories = ["electronics", "clothing", "home", "sports"]

# Check if "toys" is not in the list.
print("toys" not in categories)


# 7. Mini Data Analyst Problems (Realistic)

# Exercise 13: Revenue Growth
last_month = 42000
this_month = 47000

# Calculate the increase in revenue.
print(this_month - last_month)
# Check if the growth is greater than $4000.
if this_month - last_month > 4000:
    print("Substantial growth")

# Exercise 14: Conversion Rate
visitors = 1200
purchases = 75

# Calculate the conversion rate.
conversion_rate = (purchases / visitors) * 100
print(conversion_rate) 
# Check if conversion rate is greater than 5%
if conversion_rate > 5:
    print("Conversion rate is greater than 5%")

# Exercise 15
missing_values = 12
duplicates = 3

# Dataset is acceptable if: 
# (1) Missing values < 20
# (2) AND duplicates < 5
if missing_values < 20 and duplicates < 5:
    print("Dataset passes quality check")
else:
    print("Dataset needs cleaning")