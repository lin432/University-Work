import reading
import database

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


def run_query(data, query):
    '''
    (Database, str) -> Table
    Given a database and a string query returns a table object that
    represents the result of the query following squeal rules

    REQ: query follows squeal rules
    REQ: headers in query must exist in one of tables specified
    REQ: table must exist in database
    '''
    # splits string
    query_str = query.split(" ")
    index = 0

    # initializes return variable
    return_table = database.Table({})

    # goes through string
    while(index < len(query_str)):
        # initialize variables here such that
        # every iteration the tables reset
        titles = []
        tables = []

        # found select statement
        if(query_str[index] == "select"):
            # increases by one and saves titles as list of string
            titles = query_str[index + 1].split(",")
            index = index + 2

            # found from so the code continues
            if (query_str[index] == "from"):
                # increases by 1 and saves tables as list of Table
                index = index + 1
                table_string = query_str[index].split(',')
                for table in table_string:
                    tables += [data.get_table(table)]

                # checks for end of string and where clause
                if((index+1) < len(query_str) and
                   query_str[index+1] == "where"):
                    # increments by two and isolates restrictions
                    index += 2
                    return_table = process_where(titles, tables,
                                                 query_str[index])
                else:
                    return_table = process_table(titles, tables)
        index += 1

    return return_table


def process_table(titles, tables):
    '''
    (list of str, list of Tables) -> Table

    takes a table and a string of titles to create
    a table from a database. if the string of titles is a star
    then it returns the entire table.
    REQ: titles exists in tables
    '''
    return_table = None
    # checks for *
    if(titles[0] == '*'):
        return_table = tables[0]
    else:
        # grabs proper table
        temp_table = table_by_title(titles[0], tables)
        dict_return = {}

        if (type(temp_table) != bool):
            # creates new table by grabbing columns and key from table
            # being processed
            for head in titles:
                dict_return[head] = temp_table.get_by_column(head)
            return_table = reading.Table(dict_return)

    return return_table


def table_by_title(title, tables):
    '''
    (str, list of Table) -> Table
    finds the table the title belongs to based on a list of Tables
    returns false if the table cannot be found
    '''
    found_table = False
    index = 0

    # iterates through all tables given to find the one in which
    # the header exists in
    while(not found_table and index < len(tables)):

        table = tables[index]
        titles = table.get_keys()
        if(title in titles):
            found_table = table

        index += 1

    return found_table


def process_where(titles, tables, restriction):
    '''
    (list of str, list of Table, str) -> Table
    creates a table based on the restirictions and returns
    a table with the elements of data that satisfied
    the restrictions
    REQ: restriction follows squeal rules
    REQ: titles exist tables
    '''
    # go through all cartesian creations
    superior_table = tables.pop()
    while(len(tables) > 0):
        superior_table = cartesian_product(superior_table, tables.pop())

    # split all restrictions
    restrictions = restriction.split(',')

    for string in restrictions:
        # searches for the operators allowed to split string
        index = 0
        while(string[index] not in "=><"):
            index = index + 1

        # splits up variables for use
        title1 = string[0:index]
        restrict = string[index:index+1]
        var = string[index+1:]

        # turns var into table if it doesn't refer to one
        if(not len(var.split('.')) > 1):
            temp_table = reading.Table({var: [var]})
            superior_table = cartesian_product(superior_table, temp_table)

        # sends to process to find the merge based on condition
        superior_table = process_restriction(title1, var, superior_table,
                                             restrict)

    superior_table = process_table(titles, [superior_table])
    return superior_table


def process_restriction(condition1, condition2, table, restriction):
    '''
    (str, str, Table, str) -> Table

    takes Table objects and retrieves the rows that satisfy the restriction
    and puts them into a new table
    REQ: restriction holds '=' or '>'
    REQ: condition1 exists in the format str + '.' + str
    REQ: condition1 and condition2 are comparable
    '''
    column = table.get_by_column(condition1)
    compare = table.get_by_column(condition2)
    new_table = reading.Table({})
    new_table.add_keys(table.get_keys())
    type_check = 'str'

    # finds the appropriate decision and adds rows that fulfill
    for index in range(0, len(column)):
        if(restriction == "="):
            if(column[index] == compare[index]):
                new_table.add_row_from(table, index)

        if(restriction == ">"):
            # deal with numeric and string values differently
            if(compare[index].isnumeric()):
                if(float(column[index]) > float(compare[index])):
                    new_table.add_row_from(table, index)
            else:
                if(column[index] > compare[index]):
                    new_table.add_row_from(table, index)
    # returns completed table
    return new_table


def cartesian_product(table1, table2):
    '''
    (Table, Table) -> Table
    returns the multiplication of both tables
    such that each term is matched to the other
    '''
    # initialize table to which the value are to be added
    return_table = reading.Table({})
    return_table.add_keys(table1.get_keys())
    return_table.add_keys(table2.get_keys())

    # Goes through one index of table 1 after every single index of table 2
    for index1 in range(0, table1.get_length_columns()):
        for index2 in range(0, table2.get_length_columns()):
            # grabs keys and adds all the elements to return)table
            return_table.add_row_from(table1, index1)
            return_table.add_row_from(table2, index2)

    return return_table


def print_csv(table):
    '''(Table) -> NoneType
    Print a representation of table.
    '''
    dict_rep = table.get_dict()
    columns = list(dict_rep.keys())
    print(','.join(columns))
    rows = num_rows(table)
    for i in range(rows):
        cur_column = []
        for column in columns:
            cur_column.append(dict_rep[column][i])
        print(','.join(cur_column))

# main code
if(__name__ == "__main__"):
    data = reading.read_database()
    query = input("Enter a SQuEaL query, or a blank line to exit:")

    # loop until a blank line is found
    while(query != ""):

        # try catch block to insure code will continue to run
        try:
            table = run_query(data, query)
            # print_csv(table) is not working for me
            print(str(table))
        except AttributeError:
            print("something went wrong")
        except IndexError:
            print("something was missing")
        except KeyError:
            print("a header was entered incorrectly/does not exist")

        # asks for next query
        query = input("Enter a SQuEaL query, or a blank line to exit:")
