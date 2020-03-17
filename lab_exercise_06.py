print('Lab Exercise 06')
# LAB EXERCISE 06

# PART 1: MidTerm Practice
# The following two problems are to familiarize with the format of 
# the midterm. You will be asked to create a simple function and call it.
# This portion of the lab exercise will be timed. Please follow the intructions
# from your instructor.

# PROBLEM 1 (5 Points)

# In this problem you will implement a simple function that:
# 1) Has two arguments: a one of them is a default 
# 2) Uses a local variable
# 3) Iterates through a list 
# 4) Appends to a list
# 3) Returns a value

# BEGIN PROBLEM 1 SOLUTION

# You will create a function named <calculate_exponent> based on the docstring provided.
# Then, on problem 4 you will be calling this function. 

def calculate_exponent(nums, power=2):
    """
    This function calculated the power for a given list of integers. You will have
    to iterate through the list and apply the operation.
    
    Parameters:
        nums (list of int): list of num whose power has to be calculated.
        power (int): This default argument is the value raised
            to compute power. Its default value is 2 (power=2)

    returns:
        list: It returns list of integers whose exponents have been calculated 

    Use a local variable named <num_power> to calculate the result of raising
    the number to the exponent, <exponents> to store your exponents and then 
    return the <exponents> variable. 

    Hint : you can use the exponent operator(**) syntax: x**y to find x to the power of y
    
    """
    exponents = []
    for i in nums:
        exponents.append(i**power)
    return exponents



# END PROBLEM 1 SOLUTION

# PROBLEM 2 (5 Points)
# In this problem you will 
# 1) Call a function
# 2) Pass positional and keyword arguments
# 3) Work with lists

# Problem 02 SETUP - We provide you with a list of integers and two empty lists to start the problem

ints = [2, 4, 6, 8]

exponents_1 = []
exponents_2 = []

# Problem 02 END SETUP

# BEGIN PROBLEM 2 SOLUTION

# Problem 2 part 1:
# Call the function <calculate_exponent> that you created in problem 3 and pass <ints> as a positional argument.
# Store it into <exponents_1>

exponents_1 = calculate_exponent(ints)
exponents_2 = calculate_exponent(ints,3)
# Problem 2 part 2:
# Call the function <calculate_exponent> that you created in problem 3 and pass <ints> as a keyword argument and pass 3(three) as 
# a keyword argument.
# Store it into <exponents_2>


# END PROBLEM 2 SOLUTION

print(f"\nProblem 2: exponents_1 = {exponents_1}\n")
print(f"\nProblem 2: exponents_2 = {exponents_2}\n")

# PART 2: TUPLES
# The following 2 problems will introduce you to working with tuples.
# If a problem includes a setup section: Do not modify, delete or otherwise ignore the setup code.

# You will save lists and tuples to required variables. These variables will be graded by autograder after your submission.
# Print statements have been provided for you to debug the code. You can uncomment them to see the results

# PROBLEM 3 (5 Points)

# In this problem you will
# 1) Work with tuples
# 2) Differentiate between tuples and lists
# 3) Update tuples

# Problem 03 SETUP - We provide you with a tuple to start the lab problem
# Here is a tuple of all nut free candies

nut_free_candy = ('skittles', 'jolly rancher', 'twizzler', 'york')

# Problem 03 END SETUP

# Turns out we forgot to include 'hershey milk chocolate' and  'kisses'.
# Unlike lists, tuples are immutable and cannot be changed or appended once they are initialized.
# Using tuples instead of lists can give the programmer a hint that data should not be changed.
# However, we are able to take existing tuples and add them to create a new tuple.

# BEGIN PROBLEM 3 SOLUTION

# Create a new tuple, name it <extra_candy> and initialize it with 'hershey milk chocolate' and  'kisses'

extra_candy = ('hershey milk chocolate', 'kisses')
# create <updated_nut_free_candy> and concatenate the two tuples by <nut_free_candy> + <extra_candy> 
updated_nut_free_candy = nut_free_candy+extra_candy

# END PROBLEM 3 SOLUTION

print(f"\nProblem 3: updated_nut_free_candy = {updated_nut_free_candy}")


# PROBLEM 4 (5 Points)
# In this problem, you will
# 1) Use a tuple as a key in dictionaries
# 2) Work with dictionaries


# Lists and tuples have a lot of similar features except tuples are immutable and they use parentheses instead of brackets.
# Because of the immutable nature, tuples can also be used as keys in dictionaries

# BEGIN PROBLEM 4 SOLUTION
# Create a dictionary named <candy_dict>, this dictionary will have only one key-value pair
# Assign <updated_nut_free_candy> as key and 'nut-free' as value
# hint: follow this syntax <dict> = {<key>:<value>}
candy_dict = {}
candy_dict[updated_nut_free_candy] = 'nut-free'
# END PROBLEM 4 SOLUTION

print(f"\nProblem 4: candy_dict = {candy_dict}")
# END PART 2



# END LAB EXERCISE