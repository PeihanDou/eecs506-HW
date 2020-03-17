# START PROBLEM SET 05

# The following 5 problems constitute a pre-midterm exam review. If a problem
# includes a setup section do not modify, delete or otherwise ignore the setup
# code.

# PROBLEM 1:

# SETUP
# We provide you with a tuple to start the problem
language1 = ("English",)
# END SETUP

# BEGIN CODING
# Create a new tuple named <language2> with two elements "Spanish" and "German" in exact order
language2 = ("Spanish", "German")

# Join two tuples <language1> and <language2> together to a new tuple <languages>
languages = language1 + language2

# Convert the tuple <languages> to a list <languages_list>
languages_list = list(languages)

# Create a new dictionary named <languages_dict> and add the key-value pair <languages>-<languages_list> to the dictionary
# The expected answer is {('English', 'Spanish', 'German'): ['English', 'Spanish', 'German']}
languages_dict = {languages:languages_list}

# END CODING
# When you have finished Problem 1, uncomment the lines below to test your result:
p1_test_ans = {('English', 'Spanish', 'German'): ['English', 'Spanish', 'German']}
print(f"\nProblem 1:\nThe following two lines should be the same:\nlanguages_dict = {languages_dict}")
print(f"languages_dict = {p1_test_ans}")

# END PROBLEM 1


# PROBLEM 2:

# SETUP
recipe = [
    'Preheat oven to 350 degrees F (175 degree C).\n',
    'Place the sliced apples in a 9x13 inch pan.\n',
    'Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.\n',
    'Pour water evenly over all.\n',
    'Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.\n',
    'Crumble evenly over the apple mixture.\n',
    'Bake at 350 degrees F (175 degrees C) for about 45 minutes.'
]
# <recipe> is a list of strings. Each element of <recipe> we call it step.
# You'll use this data for Problems 2,3,4,5
# Hint: Recall that string is immutable. You can't change strings. But you can create new strings.
# END SETUP

# BEGIN CODING
def format_step(step, order):
    """
    This function accepts a step from the recipe and the order of the step.
    If <step> contains "\n", the function should remove "\n"
    Then the function should return a formatted string.

    Parameters:
        - step (str): A string represents a step in the recipe (i.e. an element from <recipe>).
        - order (int): An integer represents the order of the step in the recipe

    Returns:
        - (str): A string that combines <step> and <order> in the following format:
            "Step<order>: <step>"
    """
    string = step
    string = string.replace("\n", "")
    return "Step"+str(order)+": "+string

# END CODING

# When you have finished <format_string>, uncomment the lines below to test your function:
print(f"\nProblem 2:\nThe following two lines should be the same:")
p2_res = format_step(recipe[0], 1)
print("Step1: Preheat oven to 350 degrees F (175 degree C).")
print(f"{p2_res}")
# END PROBLEM 2


# PROBLEM 3:
# Hint: Use .split(), list indexing to extract <order> and <step>
# BEGIN CODING
def create_step_length(step_list):
    """
    This function accepts a list of strings.
    Each element in <step_list> has the format "Step<order>: <step>".
    This function would return a dictionary.
    This function should iterate over the <step_list>.
    For each step, the function should add a new key-value pair 
    "step<order>" : the number of characters in the <step> to the returned dictionary
    e.g. for "Step1: Preheat oven", key-value pair should be "step1": 12
    When calculating the number of characters, you should NOT include the space after ":"
    i.e. if you're using split(), the seperator should be ": ", instead of just ":"
   
    Parameters:
        - step_list (list): A list contains steps of a recipe.

    Returns:
        - step_length(str): A dictionary that has key-value pair in the following format:
            "step<order>": length of the <step> 
    """
    step_length = {}
    for i in step_list:
        part = i.split(": ")
        step_length[part[0].lower()] = len(part[1])
    return step_length

# END CODING
# When you are finished with your <create_step_length> function, uncomment the lines below.
p3_test = ['Step1: Preheat oven','Step2: Place the sliced apples','Step3: Mix the white sugar']
p3_test_ans = {'step1': 12, 'step2': 23, 'step3': 19}
p3_res = create_step_length(p3_test)
print(f"\nProblem 3:\nThe following two lines should be the same: \n{p3_test_ans}")
print(f"{p3_res}")
# END PROBLEM 3

# PROBLEM 4:

# For those steps of a recipe, whose length is larger than half of the maximum of all step lengths, they are called "core steps"
# e.g. given a step_length {'step1': 3, 'step2': 5, 'step3': 8}
# core steps would be step2 and step3
# Because maximum of all step length is 8
# Based on the definition of core steps, only step2 and step3 have the length larger than 4.

# Write a function to filter the corresponding key-value pairs of core steps of a recipe.
# Hint: You can use built-in function max() to get the maximum value.
# BEGIN CODING
def filter_step_length(step_length):
    """
    This function accepts a dictionary with the key-value pair in the format "step<order>" : length of the <step>.
    This function returns a new dictionary.
    This function would iterate each key-value pair in <step_length>,
    This function would add corresponding key-value pairs of core steps to the returned dictionary

    Parameters:
        - step_length (dict): A dictionary contains key-value pair in the format "step<order>" : length of the <step>.

    Returns:
        - filtered_dict (dict): A dictionary that only contains "core steps" key-value pairs
    """
    max_v = max(step_length.values())
    filtered_dict = {}
    for i in step_length:
        if step_length[i] > max_v/2:
            filtered_dict[i] = step_length[i]
    return filtered_dict

# END CODING
# When you are finished with your <filter_step_length> function, uncomment the lines below.
p4_test = {"step1":4, "step2":5, "step3":7}
p4_res = filter_step_length(p4_test)
print(f"\nProblem 4:\nThe following two lines should be the same: \n{p4_test}")
print(f"{p4_res}")
# END PROBLEM 4


# PROBLEM 5:

# Now let's put what we have learned together. 
# Reuse the functions created in Problem 2,3,4 to find the order and content of those core steps

# Hint: Be careful with formatted step and step, they are different. 
# Hint: Since tuple is immutable, you can't add element to a tuple. You can join two tuples together
# BEGIN CODING
def main(step_list):
    """
    This function takes a list of steps of a recipe.
    This function returns two tuples.
    The first tuple should contain the order of those core steps in a recipe
    The second tuple should contain the formatted core steps in a recipe

    Parameters:
        - step_list (list): A list of strings containing steps of a recipe 
        (i.e. <recipe>)

    Returns:
        - tuple: either a tuple of ints containing the the order of core steps in a recipe 
                or a tuple of strings containing the formatted core steps in a recipe.
    """
    step = []
    for i in range(len(step_list)):
        step.append(format_step(step_list[i], i+1))
    step_dict = create_step_length(step)
    filt_step = filter_step_length(step_dict)
    core_step_num = []
    for i in filt_step:
        core_step_num.append(int(i[-1]))
    core_step_num_tuple = tuple(core_step_num)
    core_step = []
    for i in core_step_num_tuple:
        core_step.append(step[i-1])
    core_step_tuple = tuple(core_step)
    return core_step_num_tuple
# END CODING
# When you are finished with your <main> function, uncomment the lines below.
print(f"\nProblem 5:\nThe following two lines should be the same: if your function returns a tuple of ints")
p5_res = main(recipe)
print(f"(3, 5, 7)\n{p5_res}\n")
print(f"The following two lines should be the same: if your function returns a tuple of strings: \n('Step3: Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over the apples.', 'Step5: Combine the oats, 1 cup of flour, brown sugar, baking powder, baking soda and melted butter together.', 'Step7: Bake at 350 degrees F (175 degrees C) for about 45 minutes.')\n{p5_res}")
# END PROBLEM 5