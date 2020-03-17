import csv

# In this homework, you will be working with data about three of the Marvel
# superheroines: Storm https://en.wikipedia.org/wiki/Storm_(Marvel_Comics);
# Scarlet Witch https://en.wikipedia.org/wiki/Scarlet_Witch; and Jessica Jones
# https://en.wikipedia.org/wiki/Jessica_Jones. You will build a class called
# <SuperHeroine> that will be able to capture several interesting bits of information
# from each hero. You will then instantiate <SuperHeroine> for each of Storm, Scarlet
# Witch, and Jessica Jones. Then you will call methods you built in <SuperHeroine> in
# order to update each instance, and finally you will write out each instance to a
# file by way of the __str__ method.

# Each task that you must complete in the below skeleton code is delineated by a
# "TO DO:"

# BEGIN CODING HERE - - - - - - - - - - - - - - - - - - - - -

def write_to_file(filepath, data_to_write):
    """
    TO DO:
    This function takes any <data_to_write>, converts it into a string via the str()
    function (if possible), and then writes it to a file located at <filepath>. Note
    that this function is a general writing function. It should not use the .csv
    module, but rather the python write() function. This is because we want this
    function to write ANYTHING we give it as the <data_to_write> parameter (in the
    case of this assignement, you will actually use it to write string representations
    of the class instances you create).

    NOTE: It is important that you convert <data_to_write> to a str BEFORE you write it!
    The object being passed into this function as <data_to_write> could already be a
    string, and if so, passing it through the str() function won't do anything. But
    any other object will need to be changed into a string object.

    Parameters:
        filepath (str): the filepath that points to the file that will be written.
        data_to_write (obj): any object capable of being converted into a string.

    Returns:
        None, but a file is produced.
    """

    str_data = str(data_to_write)
    f = open(filepath,'w')
    f.write(str_data)


class SuperHeroine(object):
    """
    This is a class that contains information on Superheroines.

    Attributes:
        name (str): The (superheroine) name of the heroine.
        full_name (str): The (given) name of the heroine.
        team (str): The team (if any) the heroine is a part of.
        eye_color (str): The eye color of the heroine.
        hair_color (str): The hair color of the heroine.
        base (str): The base of operations of the heroine.
        powers (list): A list of powers the heroine has.
        nemeses (list): A list of the enemies the heroine has faced.
    """

    def __init__(self, name, full_name, team, eye_color, hair_color, base):
        """
        TO DO:
        The constructor of the <SuperHeroine> class. Here you will need to create
        the attributes ("instance variables") that were described in the <SuperHeroine>
        docstring. Note that some of the attributes are defined by parameters passed
        to this constructor method, but others are not. In this case, the <power> and
        <nemeses> attributes should simply be defined as empty lists here.

        Parameters:
            name (str): The (superheroine) name of the heroine.
            full_name (str): The (given) name of the heroine.
            team (str): The team (if any) the heroine is a part of.
            eye_color (str): The eye color of the heroine.
            hair_color (str): The hair color of the heroine.
            base (str): The base of operations of the heroine.

        Returns:
            None
        """

        self.name = name
        self.full_name = full_name
        self.team = team
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.base = base
        self.powers = []
        self.nemeses = []


    def __str__(self):
        """
        This is the string method for the <SuperHeroine> class. Whenever an instance of
        <SuperHeroine> is passed to the str() or print() functions, the return string
        from this method will be returned.

        TO DO:
        In this case, you only need to fill in the instance attributes that are outlined by
        the <> characters in the <description> variable. Don't forget the {} required to
        insert a variable into an f-string!

        Parameters:
            None

        Returns:
            str: A string that describes this instance of <SuperHeroine>

        *As a side note, often in object-oriented programming, __str__ methods
        are not often accompanied by a docstring, because they have a very clear function.
        """

        description = self.name  + " is a member of the " + self.team + ", and has the following powers:\n"+str(self.powers)
        return description


    def add_power(self, power):
        """
        TO DO:
        This method will modify the <powers> attribute by appending the parameter <power>
        to it.

        Parameters:
            power (str): Description of the power that is to be added to the <powers> attribute.

        Returns:
            None
        """

        self.powers.append(power)


    def add_nemesis(self, nemesis):
        """
        TO DO:
        This method will modify the <nemeses> attribute by appending the parameter <nemesis>
        to it.

        Parameters:
            nemesis (str): Name of the nemesis that is to be added to the <nemeses> attribute.

        Returns:
            None
        """

        self.nemeses.append(nemesis)


def read_csv_file(input_filepath):
    """
    THIS SHOULD LOOK FAMILIAR, SO WE PROVIDED IT FOR YOU.

    This function reads a .csv file and parses it into a list of dictionaries,
    where each dictionary is formed from the data on one line of the .csv file.
    This function takes one argument <input_filepath>, which is the path of the file
    to be read. You will need to use the "csv" module in this function.

    The format of the returned list of dictionaries is as follows:

        [
            { <column 1 header>: <row 1 column 1 value>,
              <column 2 header>: <row 1 column 2 value>,
              <column 3 header>: <row 1 column 3 value>,
              ...etc
            },

            { <column 1 header>: <row 2 column 1 value>,
              <column 2 header>: <row 2 column 2 value>,
              <column 3 header>: <row 2 column 3 value>,
              ...etc
            },

            ...etc
        ]

    Parameters:
        input_filepath (str): The location of the file to read and parse.

    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """

    out_list = []

    with open(input_filepath, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i == 0:
                labels = row
            else:
                new_dict = {}
                for j,value in enumerate(row):
                    new_dict[labels[j]] = value
                out_list.append(new_dict)

    return out_list


def main():
    """
    In this function, you will instantiate <SuperHeroine> several times, given the data
    provided. Then, you will open "sh_additional_info.csv" and for each line in that file,
    perform an operation using one of the methods of one of your classes. Follow
    the commented instructions in this main() function.

    Parameters:
        None

    Returns:
        None, but three files are produced.
    """


    # TO DO:
    # Read in the "sh_basic_info.csv" file using your <read_csv_file> function. Save the
    # returned list to <basic_info>. Each item in <basic_info> should be a dictionary
    # describing one of the heroines in the data set.
    basic_info = read_csv_file("sh_basic_info.csv")
    # print(basic_info)

    # TO DO:
    # There are several steps to this section.
    # 1. Create an empty dictionary called <heroines>.
    # 2. Loop through the <basic_info> list and create an instance of <SuperHeroine>
    #       for each item in <basic_info>.
    # 3. Within that loop, create a new key/value pair in <heroines> for each instance
    #       of <SuperHeroine> that you create. Make the key be the <name> of that heroine,
    #       and the value be the instance of <SuperHeroine> you created.
    # 4. Print out <heroines>. If done correctly, it should look something like this
    #       (except that your memory addresses will be different):
    #
    #       {
    #        'Storm': <__main__.SuperHeroine object at 0x100b6d2e8>,
    #        'Scarlet Witch': <__main__.SuperHeroine object at 0x100b6d240>,
    #        'Jessica Jones': <__main__.SuperHeroine object at 0x100b6d208>
    #       }
    heroines = {}
    for i in basic_info:
        heroines[i['name']] = SuperHeroine(i['name'],i['full_name'],i['team'],i['eye_color'],i['hair_color'],i['base'])
    # print(heroines)

    # TO DO:
    # Read the "sh_additional_info.csv" file using your <read_csv_file>. Save the
    # returned list to the variable <additional_info>
    additional_info = read_csv_file("sh_additional_info.csv")
    # print(additional_info)
    # TO DO:
    # Loop through the lines from 'sh_additional_info.csv' (which are now stored in
    # <additional_info>) and do the following:
    #
    # 1. Save the value associated with the "Heroine Name" key from each row of <additional_info>
    #       to a new variable.
    # 2. Use that new variable as the key to retrieve the correct instance from <heroines> and
    #       save that instance to a new variable <instance_affected>
    # 3. Save the values associated with the "Category" and "Value" keys from each row of
    #       <additional_info> to their own variables.
    # 4. Create a conditional ("if") statement that checks whether the "Category" variable
    #       is 'power' or 'nemesis'.
    # 5. Call the proper method (either <add_power> or <add_nemesis>) on the <instance_affected>
    #       variable.
    for i in additional_info:
        sh_name =  i['Heroine Name']
        for j in heroines:
            if sh_name == j:
                instance_affected = heroines[j]
        sh_cat = i['Category']
        sh_val = i['Value']
        if sh_cat == 'power':
            instance_affected.add_power(sh_val)
        if sh_cat == 'nemesis':
            instance_affected.add_nemesis(sh_val)


    


    # TO DO:
    # Call your <write_to_file> function three times:
    #
    # First: create a file called "storm.txt" that writes the <storm> instance.
    # Second: create a file called "scarlet_witch.txt" that writes the <scarlet_witch> instance.
    # Finally: create a file called "jessica_jones.txt" that writes the <jessica_jones> instance.
    # print(heroines)
    write_to_file('storm.txt',heroines['Storm'])
    write_to_file('scarlet_witch.txt',heroines['Scarlet Witch'])
    write_to_file('jessica_jones.txt',heroines['Jessica Jones'])


# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()