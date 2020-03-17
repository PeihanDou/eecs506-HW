# START PROBLEM SET 01
print('PROBLEM SET 01 \n')

# PROBLEM 01A (25 points)
# Uncomment the variable name and assigned value that adheres to the styling
# convention described in PEP 08 for function and variable names
# (see https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
# Choose wisely or you will trigger a syntax error.

# Hint: uncomment = remove hash symbol ('#') and any leading whitespace in front
# of the variable name.

# Guido van Rossum is the original author of Python and former
# Benevolent dictator for life (BDFL) of the project.

# BEGIN 01A SOLUTION
# 1st_bdfl = 'Guido van Rossum'
# benevolent_dictator_for_life! = 'Guido van Rossum'
# python author = 'Guido van Rossum'
python_author = 'Guido van Rossum'
# lambda = 'Guido van Rossum'

# SETUP - DO NOT MODIFY
languages = ['Java', 'C++', 'Javascript', 'Ruby', 'Python', 'Fortran']
# END SETUP

# Next, use list indexing of the <languages> list to assign the language that Guido von Rossum
# authored to the variable <guido_language>.

guido_language = languages[4]

# END 01A SOLUTION

# Note the below use of the f-string to incorporate a variable into a string in the print
# statement.
print(f'Guido van Rossum authored {guido_language}\n')



# PROBLEM 01B (25 points)
# Use the appropriate string operation to concatenate Guido's current position
# at the Python Software Foundation (see https://www.python.org/psf/members/#officers)
# to the value assigned to the variable you chose you in Problem 01A. Assign
# the concatenated value to the variable <python_foundation_officer>.

# Adopt the following format for the new string:

python_foundation_officer = f"{python_author}, President"

# Note the below use of the f-string to incorporate a variable into a string in the print
# statement.
print(f'python_foundation_officer={python_foundation_officer}\n')

# END 01B SOLUTION


# START PROBLEM 01C-E SETUP (do not modify)

# The Zen of Python, by Tim Peters (1999)

# Note the use of triple (""") quotes to denote a multi-line string.
zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(f'zen_of_python={zen_of_python}\n')
# END SETUP

# PROBLEM 01C (25 points)
# Count the number of characters in the string assigned to the
# variable zen_of_python and assign the value to the variable <num_chars>.

# BEGIN 01C SOLUTION

num_chars = len(zen_of_python)


print(f'num_chars={str(num_chars)}')
# END 01C SOLUTION


# PROBLEM 01D (25 points)
# Count the number of "words" separated by whitespace (word is used
# figuratively since not all the character chunks you will encounter are
# actually words) in the string assigned to the variable zen_of_python
# and assign the value to the variable <num_char_chunks>.

# BEGIN 01D SOLUTION

num_char_chunks = len(zen_of_python.split())
# Note use of the built-in str() function to format num_char_chunks as a string.

print(f'num_char_chunks={str(num_char_chunks)}\n')

# END 01D SOLUTION


# PROBLEM 01E (25 points)
# Use floor division to divide num_char_chunks by the number of lines
# in the Zen of Python (use readlines() to determine this). Return an integer
# rather than a floating point value.
# Assign the value to the variable <avg_num_chunks_per_line>.

# BEGIN 01E SOLUTION
avg_num_chunks_per_line = int(num_char_chunks/len(zen_of_python.split("\n")))

# Notice how we can also use the string method .join() to join all of the elements
# in a list by including that string in between each element.
print(''.join(['avg_num_chunks_per_line=', str(avg_num_chunks_per_line), '\n']))
# END 01E SOLUTION


# PROBLEM 01F (25 points)
# Substitute your U-M email address for all occurrences of the word "Dutch" using
# the appropriate built-in function in the zen_of_python string. Assign the modified
# Zen of Python string to a new variable named <zen_of_python_uniqname>.

# BEGIN 01F SOLUTION

zen_of_python_uniqname = zen_of_python.replace('Dutch','douph@umich.edu')

print(''.join(['zen_of_python_uniqname=', zen_of_python_uniqname, '\n']))
# END 01F SOLUTION

# END PROBLEM SET