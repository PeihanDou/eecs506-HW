# START LAB EXERCISE 02
print('Lab Exercise 02 \n')

# PROBLEM 1 (10 points)
# Uncomment the variable name and assigned value that adheres to the styling
# convention described in PEP 08 for function and variable names
# (see https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
# Choose wisely or you will trigger a syntax error.

# Hint: uncomment means removing the hash symbol ('#') and any leading whitespace in front
# of the variable name.

# BEGIN PROBLEM 1 SOLUTION

# class = 'SI 506'
# course name = 'SI 506'
# $course_name = 'SI 506'
course_name = 'SI 506'

# Next, concatenate the text ": Programming I" to the value of the variable
# selected above using the appropriate operator. Write code on next line.
course_name = course_name+': Programming I'
# <-- put your code before this comment!

# Next write a print() statement that prints the variable value to the
# screen. Write code on next line.
print(course_name)
# <-- put your code before this comment!

# Next determine the number of characters of your new string value using
# the appropriate builtin function. Assign the value to the variable
# <num_chars> (replace default value of -999):

num_chars = len(course_name)
# <-- put your code before this comment!

# Note use of the f-string notation to include a variable in the string that
# is printed below.
print(f'num_chars = {str(num_chars)}\n')

# END PROBLEM 1 SOLUTION

# PROBLEM 2 (10 points)

# SETUP

# The multi-line string <i_have_a_dream> is an excerpt from the eponymous speech given
# by Dr. Martin Luther King, Jr., on the steps of the Lincoln Memorial in Washington, D.C.,
# on August 28, 1963.

i_have_a_dream = """
I have a dream that one day this nation will rise up
and live out the true meaning of its creed:
"We hold these truths to be self-evident, that all men are created equal."

I have a dream that one day on the red hills of Georgia,
the sons of former slaves and the sons of former slave owners
will be able to sit down together at the table of brotherhood.

I have a dream that one day even the state of Mississippi,
a state sweltering with the heat of injustice,
sweltering with the heat of oppression,
will be transformed into an oasis of freedom and justice.

I have a dream that my four little children will one day live in a nation where they will
not be judged by the color of their skin but by the content of their character.

I have a dream today!

I have a dream that one day, down in Alabama, with its vicious racists,
with its governor having his lips dripping with the words of "interposition" and "nullification"
-- one day right there in Alabama little black boys and black girls will be able to join hands
with little white boys and white girls as sisters and brothers.

I have a dream today!

I have a dream that one day every valley shall be exalted,
and every hill and mountain shall be made low,
the rough places will be made plain,
and the crooked places will be made straight;
"and the glory of the Lord shall be revealed and all flesh shall see it together."
"""

# END SETUP

# Determine the number of words in <i_have_a_dream>, and assign that number to
# the variable <number_words>. Then, determine the number of lines in <i_have_a_dream>,
# and assign that number to <number_lines>.

# BEGIN PROBLEM 2 SOLUTION

number_words = len(i_have_a_dream.split())
number_lines = len(i_have_a_dream.split("\n"))-1 #To ignore the last '\n' cause it doesn't count as a line

# Note use of the built-in str() function to format num_char_chunks as a string,
# and then the use of ''.join() to join all of the elements of the list with an
# empty string.
print(''.join(['number_words=', str(number_words), '\n']))
print(''.join(['number_lines=', str(number_lines), '\n']))

# END PROBLEM 2 SOLUTION

# END LAB EXERCISE