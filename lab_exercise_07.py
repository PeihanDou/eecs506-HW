#LAB EXERCISE 7

#Importing some required libraries:
import csv # You will use this one!
import operator # Don't worry about this.

#PROBLEM STATEMENT
# Scenario:
# You work for the US Department of Transportation.
# You are asked to determine the top TWO highly trafficked cities
# determined by the number of passengers passing through their airports.
# You have been given a CSV file of highly trafficked airports (airports.csv) to help you.
#
# Objective: Build a python script that will create an output file (airports_ranked.csv)
# of cities ranked in descending order by their number of travelers passing through their airports.
# Your output file should have the following headers:
#
#     <city>, <number of passengers>
#
# As an example, the output file should contain the following rows:
'''
Charlotte, 46444380
Miami, 45044312
Houston, 43807539
'''
# To accomplish this objective, build out the following stubbed functions. We have provided one
# function for you <sort_dictionary_by_value>. PLEASE DON'T CHANGE ANY CODE IN THIS FUNCTION!
# However, please read the docstring to understand how it works and what it is doing.


def sort_dictionary_by_value(dictionary):
    """
    DON'T CHANGE THIS FUNCTION. This function sorts a dictionary by its values in a
    descending fashion.
    Parameters:
        dictionary (dict): A dictionary to be sorted.
    Returns:
        dict: The sorted dictionary.
    """

    desc_dictionary = dict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True))

    return desc_dictionary
    

def read_csv_file(input_filepath):
    """
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

    As an example, if the input file were structured like so:

    Name,Age,Animal Type
    Lex,5,Dog
    Luke,7,Cat

    Then the returned list would be:
    [
        {
            "Name": "Lex",
            "Age": "5",
            "Animal Type": "Dog"
        },
        {
            "Name": "Luke",
            "Age": "7",
            "Animal Type": "Cat"
        }
    ]

    As a final example, if your input file were structured like so:

    Airport, City, Passengers
    Charlotte Douglas International Airport, Charlotte, 46444380

    Then the returned list should be:
    [
        {
            "Airport": "Charlotte Douglas International Airport",
            "City": "Charlotte",
            "Passengers": "46444380"
        }
    ]

    HINT: This is the most challenging part of this problem. You may want to consider
    using nested loops with enumerate statements. Don't worry about converting any
    strings to other types here; you can handle that later.
    Parameters:
        input_filepath (str): The location of the file to read and parse.
    Returns:
        list: A list of dictionaries, where each dictionary is one row from the
            input file.
    """

    li = []
    f = open(input_filepath,'r',newline='')
    csvfile = csv.reader(f)
    for row in csvfile:  
        li.append(row)
    header = li[0]
    airlist = []
    for i in range(len(li)):
        if i != 0:
            dic = {}
            for idx, head in enumerate(header):
                dic[head] = li[i][idx]
            airlist.append(dic)
    f.close()
    return airlist


def write_csv_file(output_filepath, dict_to_write, header):
    """
    Writes a .csv file using the "csv" module. The file will contain the information
    from <dict_to_write>, where each row of the new .csv file is one of the key/value
    pairs. In other words, the output file should have two columns.
    The resultant file should be structured in the following way:
        <header[0]>,<header[1]>
        key1,value1
        key2,value2
        key3,value3
        ...etc
    Parameters:
        output_filepath (str): The file path to the new file being created.
        dict_to_write (dict): The information to include in the file being created.

    Returns:
        None
    """

    f = open(output_filepath,'w',newline='')
    file = csv.writer(f)    
    file.writerow(header)
    key = list(dict_to_write.keys())
    val = list(dict_to_write.values())
    rows = []

    for i in range(len(dict_to_write)):    
        rows.append([key[i],val[i]])
    file.writerows(rows)


def passengers_per_city(list_of_airport_dicts):
    """
    This function takes a list of airport data (e.g. the return from
    <read_csv_file>), and returns a new dictionary of airports in each state. The output
    dictionary should have the format:
    {<airport city>: <total number of passengers passing through the airport in that city>}

    Parameters:
        list_of_airports (list): A list of dictionaries, where each dictionary contains the
            information on a specific airport.

    Returns:
        dict: A dictionary where the keys are the city and the values
            are the total number of passengers (integer) passing through the airport in that city.
        HINT: You may need to cast/transform string objects into integer objects for the returns.
    """

    city_dic = {}
    for dic in list_of_airport_dicts:
        city_dic[dic['City']] = 0
    for dic in list_of_airport_dicts:
        city_dic[dic['City']] += int(dic['Passengers'])

    return city_dic


def main():
    """
    Read in the data from "airports.csv". Then, parse that data and determine
    the number of passengers per city using your <passengers_per_city> function.
    Then, sort the resultant dictionary by number of passengers.
    Finally, write the sorted dictionary to a new file "airports_ranked.csv".
    Don't forget to include headers that are tuples into the "airports_ranked.csv" file!

    Parameters:
        None

    Returns:
        None
        HINT: You will need to call each of the functions in this script
        to complete this task.
    """

    inp_path = "airports.csv"
    out_path = "airports_ranked.csv"
    parklist = read_csv_file(inp_path)
    park_dic = passengers_per_city(parklist)
    park_dic = sort_dictionary_by_value(park_dic)
    head = ['City','Passengers']
    for i in park_dic.keys():
        park_dic[i] = park_dic[i]
    write_csv_file(out_path, park_dic, head)


# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()