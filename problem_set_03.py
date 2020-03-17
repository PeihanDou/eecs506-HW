# START PROBLEM SET 03

# PROBLEM 1:

# SETUP
# You will work with a list of nintendo consoles for problem 1 and 2. The list
# contains an element for each nintendo television console released, followed by
# information on when that console was released. For example, the first element
# of the <nintendo_consoles> list describes the "Famicom/Nintendo Entertainment
# System" console, which was released in 1983.
nintendo_consoles = ["Famicom/Nintendo Entertainment System (NES), released: 1983",
                    "Super Famicom/Super Nintendo Entertainment System (SNES), released: 1990",
                    "Nintendo 64 (N64), released: 1996",
                    "GameCube, released: 2001",
                    "Wii, released: 2006",
                    "Wii U, released: 2012",
                    "Nintendo Switch, released: 2017"]
# END SETUP

# BEGIN CODING
# Using the <nintendo_consoles> list and your knowledge of list slicing and indexing,
# create new list variables as directed. Each list should contain the entire strings
# from <nintendo_consoles> that meet the criteria described. You should not have to use
# any list concatenation methods or operators.

# <eighties_consoles> should include all the nintendo consoles that were released from
# 1980 - 1989
eighties_consoles = nintendo_consoles[0]
# <nineties_consoles> should include all the nintendo consoles that were released from
# 1990 - 1999
nineties_consoles = nintendo_consoles[1:3]


# <oughts_consoles> should include all the nintendo consoles that were released from
# 2000 - 2009
oughts_consoles = nintendo_consoles[3:5]


# <teens_consoles> should include all the nintendo consoles that were released from
# 2010 - 2019
teens_consoles = nintendo_consoles[5:]

# END CODING
print(f"""\nProblem 1:\neighties_consoles = {eighties_consoles}
nineties_consoles = {nineties_consoles}
oughts_consoles = {oughts_consoles}
teens_consoles = {teens_consoles}""")
# END PROBLEM 1


# PROBLEM 2:
# Using <nineties_consoles>, a for-loop, and string/list methods, create a new list called
# <release_years> that contains all of the years in which Nintendo released a
# telivision-based video game console.
#
# Example of what your <release_years> list should look like:
# [ "1983", "1990", ... etc. ]

# BEGIN CODING
release_years = []
for i in nintendo_consoles:
    tmp = i.split(': ')
    release_years.append(tmp[-1])

# END CODING
print(f"\nProblem 2:\nrelease_years = {release_years}")
# END PROBLEM 2

# SETUP
# For Problems 3, 4, and 5, you will be implementing loops, conditionals, and methods
# within the function stubs provided. Read the docstrings of each function stub in order
# to understand what each function should do. Problems 3 and 4 have you create utility
# functions to perform specific tasks, and in Problem 5 you will write your main()
# function.
#
# For Problems 3, 4, and 5, you will be working with another video game console dataset,
# similar to <nintendo_consoles>, but expanded. The <vg_consoles> list contains data on
# the most popular video game consoles from each computing technological era (called
# "generations" in the dataset). Each element of <vg_consoles> is a string with data
# separated by commas (you'll see this format of data storage again soon!) in the following
# order:
#
# Console name | Production company | Generation | Release year | Approx. # units sold

vg_consoles = [
"Odyssey,Magnavox,1st Generation,1972,100000",
"Atari 2600,Atari,2nd Generation,1977,30000000",
"ColecoVision,Coleco Industries,2nd Generation,1980,2000000",
"Intellivision,Mattel Electronics,2nd Generation,1982,3000000",
"Famicom/Nintendo Entertainment System (NES),Nintendo,3rd Generation,1983,61910000",
"Master System,Sega,3rd Generation,1985,13000000",
"Atari 7800,Atari,3rd Generation,1986,3770000",
"Super Famicom/Super Nintendo Entertainment System (SNES),Nintendo,4th Generation,1990,49100000",
"Mega Drive/Genesis,Sega,4th Generation,1988,30750000",
"Saturn,Sega,5th Generation,1994,9260000",
"PlayStation,Sony,5th Generation,1994,102490000",
"Nintendo 64 (N64),Nintendo,5th Generation,1996,32930000",
"Dreamcast,Sega,6th Generation,1998,9130000",
"PlayStation 2,Sony,6th Generation,2000,155000000",
"GameCube,Nintendo,6th Generation,2001,21740000",
"Xbox,Microsoft,6th Generation,2001,24000000",
"Xbox 360,Microsoft,7th Generation,2005,84700000",
"PlayStation 3,Sony,7th Generation,2006,87400000",
"Wii,Nintendo,7th Generation,2006,101630000",
"Wii U,Nintendo,8th Generation,2012,13560000",
"PlayStation 4,Sony,8th Generation,2013,102800000",
"Xbox One,Microsoft,8th Generation,2013,46900000",
"Nintendo Switch,Nintendo,9th Generation,2017,47300000"
]
# END SETUP

# PROBLEM 3:
# HINT: Use string methods to isolate the number of units sold, convert that number into
# an integer, and then perform your conditional operation.
def filter_by_units_sold(console,minimum_units_sold):
    """
    This function will parse a string (i.e. one of the elements of <vg_consoles>),
    and return True if the number of units sold was higher than <minimum_units_sold>,
    or False if the number of units sold was lower than <minimum_units_sold>.

    Parameters:
        - console (str): A string containing all of the information on the console (i.e.
            an element from <vg_consoles>).
        - minimum_units_sold (int): An integer to compare the number of units sold against.

    Returns:
        - (bool): True or False, depending on if the number of units sold in <console> are
            greater than minimum_units_sold or not.
    """
    part = console.split(',')
    if int(part[-1]) > minimum_units_sold:
        return True
    else:
        return False


# When you have finished <filter_by_units_sold>, uncomment the below lines to test your
# function:
print(f"\nProblem 3:\nThis should print False: {filter_by_units_sold(vg_consoles[0],100000)}")
print(f"This should print True: {filter_by_units_sold(vg_consoles[0],1000)}")


# PROBLEM 4:
# HINT: f-strings will be helpful here.
def format_string(console):
    """
    This function accepts a string of video game console data, delmited by commas (e.g. an
    element from <vg_consoles>), and returns a formatted string.

    Parameters:
        - console (str): A string containing all of the information on the console (i.e.
            an element from <vg_consoles>).

    Returns:
        - (str): A string that has formatted the information from <console> in the following
            format:

            "<Console name> was produced in <Release year> by <Production company>"
    """
    part = console.split(',')
    str = part[0]+" was produced in "+part[3]+" by "+part[1]
    return str

# When you have finished <format_string>, uncomment the below lines to test your
# function:
print(f"\nProblem 4:\nThe following two lines should be the same:")
print("Odyssey was produced in 1972 by Magnavox")
print(f"{format_string(vg_consoles[0])}")


# PROBLEM 5
# HINT: You will need to call both <filter_by_units_sold> and <format_string> in
# this function. You will also need to use a for-loop.
def main(console_list):
    """
    This function takes a list of video game console data (i.e. <vg_consoles>) as an
    argument, and returns a list showing formatted information on the consoles that
    were extremely commercially succesful (sold more than 100,000,000 units). In order
    to do so, this function will loop over <console_list>, determine which elements have
    sold more than 100,000,000 units, and then format them and add them to the returned
    list.

    Parameters:
        - console_list (list of str): A list of strings containing comma-delimited information
            on video game consoles (i.e. <vg_consoles>)

    Returns:
        - (list of str): A list of strings, where each string is an instance of a video game
            console that has sold more than 100,000,000 units, formatted by <format_string>
    """
    l = []
    for i in console_list:
        if filter_by_units_sold(i, 100000000):
            l.append(format_string(i))
    return l

# When you are finished with your <main> function, uncomment the below lines.
print(f"\nProblem 5:\nThe following line should include: PlayStation, PlayStation 2, PlayStation 4, and Wii")
print(f"{main(vg_consoles)}")

# END PROBLEM SET