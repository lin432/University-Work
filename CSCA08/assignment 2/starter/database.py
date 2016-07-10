class Table():
    '''A class to represent a SQuEaL table'''

    def __init__(self, dict_to_load={}):
        '''
        (Table, {string, list of string}) -> NoneType
        create a dictionary that will store name of row and
        column of data
        '''
        self._dict = dict_to_load

        return None

    # used mainly for testing
    def __str__(self):
        '''(Table) -> string
        string representation of Table object that returns
        a string with the column name then the string representation
        of the string for a columns
        '''
        string = ""
        # creates a string by returning key(header) first then array of values
        for key in self._dict:
            string += key + str(self._dict[key]) + "\n"

        return string

    def add_keys(self, keys):
        '''(Table, set) -> Nonetype
        adds the keys to the table that are unimplemented in Table
        in the array to facilitate add_row_from
        '''
        # iterates through keys
        for key in keys:
            self._dict[key] = []

    def add_row_from(self, table, index):
        '''
        (Table, Table, int) -> Nonetype
        adds a row from a different Table to this table

        REQ: all keys in input table exist in local Table
        '''
        keys = table.get_keys()
        # iterates through all keys and adds to local array from
        # table
        for key in keys:
            value = table.get_by_row_column(key, index)
            self._dict[key] += [value]

    def get_by_row_column(self, key, index):
        '''
        (Table, str, int) -> object
        returns the values of a key and index in table
        from the internal dictionary
        '''
        return self._dict[key][index]

    def get_keys(self):
        '''
        (Table) -> list of str
        returns a list of all keys in the table dictionary
        '''
        return self._dict.keys()

    def get_length_columns(self):
        '''(Table) -> int
        returns the max length of the arrays in the table
        '''
        # goes through all columns as there is no
        # random grab item from set available
        max_length = 0
        for item in self._dict:
            array = self._dict[item]
            if (len(array) > max_length):
                max_length = len(array)

        return max_length

    def get_by_column(self, name):
        '''
        (Table, String) -> Array
        returns an array of of all the objects in
        the column found by specific name of the header
        for the column
        '''
        return self._dict[name]

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self._dict = new_dict
        return None

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self._dict


class Database():
    '''A class to represent a SQuEaL database'''

    def __init__(self):
        '''
        (Table) -> NoneType
        a class that holds various tables
        and returns Table objects based on keys
        '''
        self._tables = {}

    def add_table(self, name, table):
        '''
        (Database, String, Table) -> NoneType
        adds a table to the database
        '''
        self._tables[name] = table
        return None

    def get_table(self, name):
        '''
        (Database, String) -> Table
        returns the table if it exists in
        dictionary
        '''
        return self._tables[name]

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        REQ: new_dict == {table_name: table, ... }
        '''
        self._tables = new_dict
        return None

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._tables
