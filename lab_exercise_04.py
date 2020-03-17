## START LAB EXERCISE 4
print('Lab Exercise 04 \n')

# BACKGROUND - 
# The mission of CAPS to foster the psychological development and
# emotional well-being of students. If you or someone you know is feeling
# overwhelmed, depressed, and/or in need of support, services are available.
# For help, contact Counseling and Psychological Services (CAPS) at
# (734) 764-8312 and https://caps.umich.edu/ during and after hours,
# on weekends and holidays. 

# We provide you with a select list of
# Counseling And Psychological Services (CAPS) embedded staff members at
# different schools across the University of Michigan. In the future, 
# the teaching team will provided you such data in a file
# which you will read into Python with some useful functions.
# However, for today, the teaching team has provided this list for you.

# Data Description:

# Each item in the caps_staff list is a string containing the name,
# the degree, the school, and email address of each CAPS staff member.
# Each data point relating to the staff member is separated by a
# pipe ('|') delimiter.

caps_staff = ["Nidaa Shaikh|Psychologist|College of Engineering|nfkazi@umich.edu",
                "Laura Monschau|Psychologist|Rackham Gradate School|lauralm@umich.edu",
                "Meaghan Narula|Social Worker|School of Public Health|mbnarula@umich.edu",
                "Julie Kaplan|Social Worker|Ross School of Business|jrkaplan@umich.edu",
                "Alejandro Rojas|Social Worker|School of Social Work|aroja@umich.edu"]

# END SETUP



# PROBLEM 1
# Extract the first item in caps_staff using its index value 
# and assign it to a new variable named <nfkazi>.

# BEGIN PROBLEM 1 SOLUTION

nfkazi = caps_staff[0]

# END PROBLEM 1 SOLUTION

# PROBLEM 2
# Extract the last element in caps_staff using its index value 
# and assign it to a new variable named <aroja>.

# BEGIN PROBLEM 2 SOLUTION

aroja = caps_staff[-1]

# END PROBLEM 2 SOLUTION


# PROBLEM 3
# Use list slicing to extract the 3rd, 4th and 5th items from the list caps_staff 
# and save the items to a new list called <social_workers>. 

# BEGIN PROBLEM 3 SOLUTION

social_workers= caps_staff[2:]

# END PROBLEM 3 SOLUTION

# PROBLEM 4
# Extract each CAPS staff member's name from the caps_staff list 
# and append the extracted names to the list named <names_of_staff>.
# Hint : You can use loops, split() and list slicing to craft your solution. 
# Use print() statements to debug.

# BEGIN PROBLEM 4 SOLUTION

names_of_staff= []
for i in caps_staff:
    part = i.split('|')
    names_of_staff.append(part[0])

# END PROBLEM 4 SOLUTION

# PROBLEM 5 
# Let's put everything you have learned about functions and lists together.
# HINT: using for loops and an f-string will be helpful here. 

# BEGIN PROBLEM 5 SOLUTION

def thank_you_caps_staff():
    '''This function will loop through a list (ie. <names_of_staff>)
    and returns an appreciative statement for each item in the list
    (ie. thank you, {name_of_staff_member}).

    PARAMETERS
    -----------
    names_of_staff: a list

    RETURNS
    -------
    prints out "Thank you, <name>" to each staff member.'''
    for i in names_of_staff:
        print("Thank you, "+i)


# END PROBLEM 5 SOLUTION
## END LAB EXERCISE 04