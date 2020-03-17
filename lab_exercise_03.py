# START LAB EXERCISE 03
print('Lab Exercise 03 \n')

# Lab 3 Setup (DO NOT CHANGE)
lunar_year = ""

# PROBLEM 1 (5 points)
# This week is the begining of the Chinese New Year and
# the Spring Festival. Let's learn more!
# We are writing a function with two positional arguments here. 
# (Learn about python functions: https://www.w3schools.com/python/python_functions.asp)

# BEGIN PROBLEM 1 SOLUTION
# Write a function named 'lunar_new_year'. Pass two positional arguments:
# <year>(data type: integer) and <year_animal>(data type: string) in this exact order. 
# sample input to function: lunar_new_year(2020, "rat") 
# sample output: returns the formatted string "2020 is the yar of rat." 
# lunar_year = "{} is the year of {}.\n".format(year,animal)

def lunar_new_year(year,year_animal):
    return "{} is the year of {}.\n".format(year,year_animal)
# <-- put your code before this comment!
# Within the function, indent!
# Then concatenate the arguments passed in the same order to a string
# using str.format() and and set it to a variable named <lunar_year>
# This is your global variable that can be reached from anywhere in the program.
# Use this format "{} is the year of {}.\n" and set your arguments.

# <-- put your code before this comment!
# return <lunar_year>
    
# <-- put your code before this comment!

# END PROBLEM 1 SOLUTION

# You have created your first python function!
# Let's go further

# PROBLEM 2 (10 points)
# Let's learn how to set default values for argument and
# return a value. When default values for the arguments are set, 
# the function can be called without passing arguments.

# We will write a function that provides information on the new
# year festivities

# BEGIN PROBLEM 2 SOLUTION
# Write a function named 'festivities_info' with two arguments:
# <date_start>(data type: string) and <message>(data type: string). 
# Assign "8-Feb" to <date_start> and "Lantern festival." to <message> using '=' .
# Make sure you have the arguments in this order.
# sample input to function: festivities_info(date_start = "February 8", message = "Lantern Festival")
# sample output: returns the formated string message "February 8 is the day of Lantern Festival." 
def festivities_info(date_start = "8-Feb", message = "Lantern Festival"):
    new_message = f"{date_start} is the day of {message}.\n"
    return new_message
# <-- put your code before this comment!
# Make sure you indent first! 
# Now concatenate <date_start> and <message> using f-string and assign this to a new
# variable called <new_message>. This is your local variable.
# Use this formatting "{<your argument here>} is the day of {<your argument here'}.\n" 

# <-- put your code before this comment!
# Return <new_message> 

# <-- put your code before this comment!
# END PROBLEM 2 SOLUTION

# Great! We have two function, now let's call them.

# LAB 3 SETUP (DO NOT CHANGE)
# This is the main function that will be called when the program runs.
def main(): 

# PROBLEM 3 (5 points)
# We will be calling 'lunar_new_year' and 'festivities_info' functions

# BEGIN PROBLEM 3 SOLUTION
# Call 'lunar_new_year' and pass "2020 " and "rat" in this exact order.
# Include the function call within a print statement.
# Leave an indetation as this is within the 'main' function.
# comment out the following code after your write your code.
#     pass
    print(lunar_new_year(2020,"rat"))
# <-- put your code before this comment!
#  Since we are returning a value from the 'festivities_info', lets include the function
#  call within a print statment. Pass "February 8" as an argument, we will use the default
#  value for the second argument. 
# Leave an indetation as this is within  the 'main' function.
    print(festivities_info(date_start="February 8"))
# <-- put your code before this comment!

# LAB 3 SETUP (DO NOT CHANGE)
if __name__== "__main__":
  main()

# END LAB EXERCISE
