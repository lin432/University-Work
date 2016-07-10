def create_dict(file_to_read):
    '''
    (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
    creates a dictionary from a file in which the key is
    the username and the list being stored represents
    [last name, first name, e-mail, age, gender]

    '''

    # read file into an array of lines
    users = file_to_read.readlines()
    dict = {}

    # go through all the lines
    for user in users:

        # split sentence into words
        stats = user.split()

        # create variables based on predefined positions of data
        username = stats[0]
        list_attr = [stats[2], stats[1], stats[5], int(stats[3]), stats[4]]

        # update dictionary
        dict.update({username: list_attr})

    return dict


def _key_word(key_word):
    '''
    (str) ->  int
    returns index at which property of key_word can be found
    accepted key words are "LAST", "FIRST", "E-MAIL", "GENDER"
    and "AGE"

    >>>_key_word("LAST")
    0
    >>>_key_word("AGE")
    3
    '''
    # Checks all accepted key words based on set pattern
    index = 0
    if(key_word == "LAST"):
        index = 0
    if(key_word == "FIRST"):
        index = 1
    if(key_word == "E-MAIL"):
        index = 2
    if(key_word == "AGE"):
        index = 3
    if(key_word == "GENDER"):
        index = 4

    return index


def update_field(dictionary, username, key_word, replace):
    '''
    (dict, str, str, object) -> NoneType
    mutates Dictionary
    replaces a field located in the values
    of the dictionary based on a key word
    Accepted key words are "LAST", "FIRST", "E-MAIL",
    "GENDER", and "AGE"

    >>>diction = {"Rooster":["James", "Ben", "rooster@hot.ca", -500, "M"]}
    >>>update_field(diction, "Rooster", "E-MAIL", "BenJ1@respectable.com")
    >>>print(diction)
    {'Rooster': ['James', 'Ben', 'BenJ1@respectable.com', -500, 'M']}

    >>>diction = {"BFG":["Frankiln-Goodrich", "Ben", "bfg@tele.com", 80, "M"]}
    >>>update_field(diction, "BFG, "")
    '''

    index = _key_word(key_word)
    # grabs attributes of username and replaces info
    # at index
    list = dictionary[username]
    list[index] = replace


def select(dictionary, value_to_return, value_to_compare, value_wanted):
    '''
    (dict, str, str, object) -> set of object
    based on a value that is wanted go through the dictionary and
    returns the value_to_return of all key-value pairs that
    have the wanted value in a set. Accepted value_to_return and
    value_to_compare are "LAST", "FIRST", "E-MAIL",
    "GENDER", and "AGE". Returns set() if empty

    '''
    set_to_return = set({})

    # premptively finds indexes to avoid processing every iteration
    index_search = _key_word(value_to_compare)
    index_retrieve = _key_word(value_to_return)

    for entry in dictionary:
        # checks if value equals the value wanted
        if(dictionary[entry][index_search] == value_wanted):
            # adds to set
            set_to_return.add(dictionary[entry][index_retrieve])

    return set_to_return
