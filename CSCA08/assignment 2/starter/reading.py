# Functions for reading tables and databases

import glob
from database import *

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

# Write the read_table and read_database functions below


def strip_characters(strings):
    '''(list of str) -> list of list of str [][]
    preps the strings to read into a table format by
    using str.split() to divide it into a nest listed
    for ease of dissasembly

    >>>strip_characters(['m.title,m.value,m.oscar'],['tera,100,1999'])
    ['m.title','m.value','m.oscar'],['tera','100','1999']

    REQ: list of strings contains ','
    '''
    # takes the array of strings and strips "\n"
    # and then proceeds to split it into a nested list
    # based on ","
    for index in range(0, len(strings)):
        strings[index] = strings[index].strip('\n')
        if(len(strings[index]) > 0):
            strings[index] = strings[index].split(',')
        else:
            strings.pop(index)

    return strings


def string_add_csv(file_name):
    '''(str) ->str
    returns a string with .csv added onto the end if it is required

    >>>string_add_csv("bob")
    'bob.csv'
    >>>string_add_csv("tuna.csv")
    'tuna.csv'
    '''
    return_str = ''
    if(len(file_name) > 4 and file_name[(len(file_name)-4):] == ".csv"):
        return_str = file_name
    else:
        return_str = file_name + '.csv'

    return return_str


def read_table(file_name):
    '''
    (str) -> Table
    takes a string indicating the location of a
    *.csv file and constructs a Table representation
    of the object and returns it

    REQ: file_name == 'string' + '.csv'
    '''
    # open file and start dictionary
    file_handle = open(string_add_csv(file_name))
    dict_to_write = {}

    # reads file into array to split further
    strings = file_handle.readlines()

    # prep for reading
    strings = strip_characters(strings)
    # formats into dictionary by first going through headers of column
    for index in range(0, len(strings[0])):
        # list of values for each headers
        list_to_add = []

        # adds each value for header by column down
        for column in range(1, len(strings)):
            list_to_add += [strings[column][index]]

        # adds to dictionary
        dict_to_write[strings[0][index]] = list_to_add

    # closes file and returns completed table
    file_handle.close()
    return Table(dict_to_write)


def read_database():
    '''
    () -> Database
    Takes all files ending in .csv and adding them to a Database of
    Tables with the file name as the key. Then returns the Database
    object
    '''
    # creates database and gets list of files
    data = Database()
    file_list = glob.glob('*.csv')

    # uses Database method to add to database dictionary
    for file_name in file_list:
        data.add_table(file_name[:(len(file_name)-4)], read_table(file_name))

    return data
