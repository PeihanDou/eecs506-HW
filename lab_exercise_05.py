print('Lab Exercise 05')
# LAB EXERCISE 05

# The following 4 problems will introduce you to working with dictionaries.
# If a problem
# includes a setup section: Do not modify, delete or otherwise ignore the setup
# code.

# You will save lists and dictionaries to required variables. These variables will be graded by autograder after your submission.
# Print statements have been provided for you to debug the code. You can uncomment them to see the results

# PROBLEM 1 (5 Points)

# In this problem you will demonstrate your understanding to

# 1) Work with dictionaries
# 2) Work with lists
# 3) Manipulating data using dictionaries
# 4) Converting the values of dictionaries to lists

# Problem 01 SETUP - We provide you with a dictionary to start the lab problems

fruits = {'apple': 10, 'banana': 20, 'strawberry': 6, 'orange' : 9}

# Problem 01 END SETUP

# BEGIN PROBLEM 1 SOLUTION

# Save the values of the dictionary fruits into a list 'num_fruits'
# The desired answer is [10, 20, 6, 9]
# Hint: You can do this by calling the values of the dictionary

num_fruits = []
for i in fruits:
    num_fruits.append(fruits[i])

# END PROBLEM 1 SOLUTION

print(f"\nProblem 1: num_fruits = {num_fruits}")


# PROBLEM 2 (5 Points)
# In this problem, you will demonstrate your undestanding in
# 1) Iterating through the dictionary
# 2) Adding the values of each pair
# 3) Saving tha value to a variable

# Problem 02 SETUP - We provide you with a variable to start the problem

sum_fruits = 0

# Problem 02 END SETUP

# BEGIN PROBLEM 2 SOLUTION

# Find the sum of the values of the fruits dictionary. Do not use the list num_fruits. Save to the variable sum_fruits
# Iterate through each key-value pair in the dictionary and add the numbers
# Save the sum of the numbers to the variable sum_fruits

for i in fruits:
    sum_fruits += fruits[i]

# END PROBLEM 2 SOLUTION

print(f"\nProblem 2: sum_fruits = {sum_fruits}")

# PROBLEM 3 (5 Points)

# In this problem you will demonstrate your understanding of
# 1) Working with dictionary
# 2) Working with the values
# 3) Finding the largest value

# Problem 03 SETUP - We provide you with a variable to start the problem

max_fruits = 0

# Problem 03 END SETUP

# BEGIN PROBLEM 3 SOLUTION

# Find the largest value in the fruits dictionary. Do not use the list num_fruits and then save to the variable max_fruits

# Hint : You can use some parts of problem 2

# Iterate through each key-value pair in the dictionary named fruits
# Work with values
# Save to a variable

for i in fruits:
    max_fruits = max(max_fruits, fruits[i])

# END PROBLEM 3 SOLUTION

print(f"\nProblem 3: max_fruits = {max_fruits}")

# PROBLEM 4 (5 Points)
# In this problem you will demonstrate your understanding of
# 1) Creating a new dictionary using an existing one
# 2) Iterating through a dictionary
# 3) Working with values
# 4) Connecting the keys based on value

# Problem 04 SETUP - We provide you with a variable to start the problem

new_dict = {}

# Problem 04 END SETUP

# BEGIN PROBLEM 4 SOLUTION

# Create a new dictionary using the fruits dictionary. Save the key value pairs which has a value of more than 6 to the new dictionary named 'new_dict'

# Iterate through the dictionary fruits
# Use if statement to check if the value is greater than 6
# Add the pair to the new dictionary
for i in fruits:
    if fruits[i] > 6:
        new_dict[i] = fruits[i]

# END PROBLEM 4 SOLUTION

print(f"\nProblem 4: new_dict = {new_dict}\n")

# END LAB EXERCISE