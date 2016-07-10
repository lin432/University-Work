# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    '''
    (str)-> str
    Returns a copy of the string with only uppercase alphabetic letters
    and all symobols removed

    >>>clean_message("The lazy fox")
    "THELAZYFOX"
    >>>clean_message("as>.<sa")
    "ASSA"
    >>>clean_message("tttaaa.....")
    "TTTAAA"

    REQ: message != None
    REQ: message.find("\n") == -1
    '''

    res = ""

    # iterates file and uses str.isalpha to decide alphabetic, if it isn't then
    # it isn't added to the string that is returned
    for i in range(0, len(message)):
        if(message[i].isalpha()):
            # letter is alphabetic so adds to result
            res += message[i].upper()

    return res


def encrypt_letter(message, key):
    '''
    (str, int) -> str
    takes a single upper case letter and returns the letter with a keystream
    value added. it does this by taking the letter and finding position of
    the letter in the alphabet adding the keystream value and subtracting until
    that number is less than 26. "A" = 0, "Z" = 25

    >>> encrypt_letter("A", 1)
    "B"
    >>> encrypt_letter("A", 26)
    "A"
    >>> encrypt_letter("A", 25)
    "Z"

    REQ: len(message) == 1
    REQ: key != None
    '''

    alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                     "W", "X", "Y", "Z"]

    # takes letter and compares it to list to see if it exists in index
    # adds one each iteration to end up with proper index when broken
    message = message.upper()
    index = 0
    while(alphabet_list[index] != message and index < len(alphabet_list)):
        index += 1

    # adds key to letter index, then checks to make sure it can go into list
    index = index + key

    while(index > 25):
        index -= 26
    while(index < 0):
        index += 26

    # returns based in new index
    return alphabet_list[index]


def decrypt_letter(message, key):
    '''
    (str, int) -> str
    takes a single upper case letter and returns the letter with a keystream
    value subtracted. it does this by taking the letter and finding position of
    the letter in the alphabet subtracting the keystream value and adding until
    that number is less than 26."A" = 0, "Z" = 25

    >>> decrypt_letter("A", 1)
    "Z"
    >>> decrypt_letter("Z", 26)
    "Z"
    >>> decrypt_letter("Z", 25)
    "A"

    REQ: len(message) == 1
    REQ: message.upper == message
    REQ: key != None
    '''
    alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                     "W", "X", "Y", "Z"]

    message = message.upper()
    # same as encrypt, searches for index of letter
    index = 0
    while(alphabet_list[index] != message and index < len(alphabet_list)):
        index += 1

    # subtracts key from index and checks to make sure it's in bounds
    index = index - key

    while(index > 25):
        index -= 26
    while(index < 0):
        index += 26

    # returns based index
    return alphabet_list[index]


def swap_cards(deck, index):
    '''
    (list of int, int) -> NoneType
    mutates deck
    List of integer represents deck, integer is index, mutates list
    swaps integer at index with the one following it a.k.a. index+1
    if index is end of list it swaps with top of deck

    >>> l = [0, 1, 2]
    >>>swap_cards(l, 1)
    >>>print(l)
    [0, 2, 1]
    >>> l = [0, 6, 48, 97, 2, 1, 3456]
    >>>swap_cards(l, 6)
    >>>print(l)
    [3456, 6, 48, 97, 2, 1, 0]

    REQ: index > 0 and len(deck) > index
    '''

    # checks for case in which index is at end of list
    if((len(deck) - 1) == index):
        # uses tuples to switch top and bottom
        (deck[0], deck[index]) = (deck[index], deck[0])
    else:
        # uses tuples to switch index and index+1
        (deck[index], deck[index + 1]) = (deck[index + 1], deck[index])

    return None


def move_joker_1(deck):
    '''
    (list of int) -> NoneType
    mutates deck
    finds JOKER1 variable and then switches it with the card that follows
    a.k.a. (deck[index + 1], deck[index]) = (deck[index], deck[index + 1])
	treats list as circular

    >>>JOKER1 = 27
    >>>l = [0, 27, 1]
    >>>move_joker_1(l)
    >>>print(l)
    [0, 1, 27]

    >>>JOKER1 = 22
    >>>l = [0, 3, 4, 9, 45, 22]
    >>>move_joker_1(l)
    >>>print(l)
    [22, 3, 4, 9, 45, 0]

    >>>JOKER1 = 0
    >>>l = [0, 51, 3, 4, 8, 7, 2, 1, 164]
    >>>move_joker_1(l)
    >>>print(l)
    [51, 0, 3, 4, 8, 7, 2, 1, 164]

    REQ: JOKER1 exists in deck
    REQ: only one instance of JOKER1 in deck
    REQ: deck != NoneType
    '''

    # uses built-in list function to find JOKER1 then uses swap_cards function
    # to swap cards
    index = deck.index(JOKER1)
    swap_cards(deck, index)

    return None


def move_joker_2(deck):
    '''
    (list of int) -> NoneType
    mutates deck
    finds JOKER2 variable and then switches it with card two down
    a.k.a index = index + 2

    >>>JOKER2 = 28
    >>>l = [0, 28, 1]
    >>>move_joker_2(l)
    >>>print(l)
    [28, 1, 0]

    >>>JOKER2 = 22
    >>>l = [0, 3, 4, 9, 45, 22]
    >>>move_joker_2(l)
    >>>print(l)
    [3, 22, 4, 9, 45, 0]

    >>>JOKER2 = 0
    >>>l = [0, 51, 3, 4, 8, 7, 2, 1, 164]
    >>>move_joker_2(l)
    >>>print(l)
    [51, 3, 0, 4, 8, 7, 2, 1, 164]

    REQ: JOKER2 exists in deck
    REQ: only one instance of JOKER2 in deck
    REQ: deck != NoneType
    '''

    # uses built-in list function to find JOKER2
    index = deck.index(JOKER2)

    # turn it into B,A,C
    swap_cards(deck, index)

    # turn it into B,C,A, need check to make sure index doesn't pass
    # end of list
    if(index == len(deck) - 1):
        swap_cards(deck, 0)
    else:
        swap_cards(deck, index + 1)

    return None


def triple_cut(deck):
    '''
    (list of int) -> NoneType
    mutates deck
    Performs a triple cut by taking the top portion till either
    JOKER1 or JOKER2 whichever comes first. Then takes the second
    JOKER and all the cards till bottom. Switch them around so
    that deck[JOKER2 + 1:] + deck[JOKER:JOKER2 + 1] + deck[:JOKER]

    >>>JOKER1 = 1
    >>>JOKER2 = 2
    >>>l = [0, 1, 2, 3]
    >>>triple_cut(l)
    >>>print(l)
    [3, 1, 2, 0]

    >>>JOKER1 = 5
    >>>JOKER2 = 2
    >>>l = [0, 1, 2, 3, 4, 5]
    >>>triple_cut(l)
    >>>print(l)
    [2, 3, 4, 5, 0, 1]

    >>>JOKER1 = 1000
    >>>JOKER2 = 0
    >>>l = [-5, 7, 2, 1000, 6, 7, 2, 0, 98, 5, 67, 4]
    >>>triple_cut(l)
    >>>print(l)
    [98, 5, 67, 4, 1000, 6, 7, 2, 0, -5, 7, 2]

    REQ: only one instance of JOKER1
    REQ: only one instance of JOKER2
    REQ: JOKER1 != JOKER2
    REQ: deck != None
    '''

    # create lists to append and insert
    end_index = 0
    begin_index = 0
    beginning = []
    end = []

    # Finds first joker and second joker
    if(deck.index(JOKER1) > deck.index(JOKER2)):
        end_index = deck.index(JOKER1)
        begin_index = deck.index(JOKER2)
    else:
        end_index = deck.index(JOKER2)
        begin_index = deck.index(JOKER1)

    # load numbers into beginning and end lists to be switched
    for a in range(0, ((len(deck) - 1) - end_index)):
        end.append(deck.pop())
    for a in range(0, begin_index):
        beginning.append(deck.pop(0))

    # reload numbers into deck but switched
    for a in range(0, len(beginning)):
        deck.append(beginning[a])
    for a in range(0, len(end)):
        deck.insert(0, end[a])

    return None


def insert_top_to_bottom(deck):
    '''
    (list of int) -> NoneType
    mutates deck
    Takes n integers from top based on last number of list and moves them just
    above last integer. Unless JOKER2 is bottom card in which case JOKER1 is
    number of cards

    >>>JOKER1 = 0
    >>>JOKER2 = 5
    >>>l = [1, 3, 0, 4, 5, 2]
    >>>insert_top_to_bottom(l)
    >>>print(l)
    [0, 4, 5, 1, 3, 2]

    >>>JOKER1 = 3
    >>>JOKER2 = 5
    >>>l = [1, 4, 8, 2, 5]
    >>>insert_top_to_bottom(l)
    >>>print(l)

    >>>JOKER1 = 3
    >>>JOKER2 = 5
    >>>l = [4, 2, 7, 8, 1, 3, 5, 6]
    >>>insert_top_to_bottom(l)
    >>>print(l)
    [5, 4, 2, 7, 8, 1, 3, 6]

    REQ:JOKER1 < len(deck)
    REQ:last element in list must be smaller than len(deck)
    REQ:type(JOKER1) == int
    REQ:type(JOKER2) == int
    REQ:deck != None
    '''
    last_index = len(deck) - 1
    num = deck[last_index]

    iter = 0

    # check for special case first and decide iterations based on that
    if(JOKER2 == num):
        iter = JOKER1
    else:
        iter = deck[len(deck) - 1]

    # simulatneously pop numbers from front and move numbers to rear
    for a in range(0, iter):
        deck.insert(len(deck) - 2, deck.pop(0))

    return None


def get_card_at_top_index(deck):
    '''
    (list of int) -> int
    returns number at top of list. if top of list == JOKER2
    then we return deck[JOKER1]

    >>>JOKER2 = 15
    >>>JOKER1 = 5
    >>>l = [1, 2, 354, 8, 7, 5, 16, 15]
    >>>get_card_at_top_index(l)
    1

    >>>JOKER2 = 5
    >>>JOKER1 = 3
    >>>l = [5, 2, 6, 7, 89, 3]
    >>>get_card_at_top_index(l)
    7

    >>>JOKER2 = 0
    >>>JOKER1 = 6
    >>>l = [56, 2, 1, 65, 4, 8, 2, 0, 6, 7, 5]
    >>>get_card_at_top_index(l)
    56

    REQ:deck != None
    REQ:type(JOKER2) == int
    REQ:type(JOKER2) == int
    REQ:JOKER1 < len(deck)
    '''

    res = 0

    # check for special case
    if(deck[0] == JOKER2):
        res = JOKER1
    else:
        res = deck[0]

    return res


def get_next_value(deck):
    '''
    (list of int) -> int
    mutates deck
    Does the encryption maneuveur and returns the next key value
    to be encrypted. Steps are: swap JOKER1 down one, swap JOKER2 down 2
    Do a triple cut at JOKER1 and JOKER2, move n cards based on last number
    and grab top of list

    >>>JOKER1 = 27
    >>>JOKER2 = 28
    >>>l = [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    >>>get_next_value(l)
    29

    >>>JOKER1 = 1
    >>>JOKER2 = 2
    >>>l = [0, 1, 2, 3, 4]
    >>>get_next_value(l)
    0

    REQ: JOKER1 exists in deck
    REQ: only one instance of JOKER1 in deck
    REQ: JOKER2 exists in deck
    REQ: only one instance of JOKER2 in deck
    REQ: JOKER1 != JOKER2
    REQ: JOKER1 < len(deck)
    REQ: All elements of deck must be smaller than len(deck)
    REQ: type(JOKER1) == int
    REQ: type(JOKER2) == int
    REQ: deck != NoneType
    '''

    # step 1 move JOKER1 down one
    move_joker_1(deck)

    # step 2 mover JOKER2 down 2
    move_joker_2(deck)

    # step 3 perform triple cut
    triple_cut(deck)

    # step 4 move n number numbers from top based on last number
    insert_top_to_bottom(deck)

    # step 5 get number by index of top card
    return deck[get_card_at_top_index(deck)]


def get_next_keystream_value(deck):
    '''
    (list of int) -> int
    mutates deck
    repeats encryption process of function get_next_value
    until it receives and acceptable value. An acceptable
    value ranges from 0-26

    >>>JOKER1 = 27
    >>>JOKER2 = 28
    >>>l = [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    >>>get_next_keystream_value(l)
    8

    >>>JOKER1 = 1
    >>>JOKER2 = 2
    >>>l = [0, 1, 2, 3, 4]
    >>>get_next_keystream_value(deck)
    0

    REQ: JOKER1 exists in deck
    REQ: only one instance of JOKER1 in deck
    REQ: JOKER2 exists in deck
    REQ: only one instance of JOKER2 in deck
    REQ: JOKER1 != JOKER2
    REQ: JOKER1 < len(deck)
    REQ: All elements of deck must be smaller than len(deck)
    REQ: type(JOKER1) == int
    REQ: type(JOKER2) == int
    REQ: deck != NoneType
    '''

    # keep repeating until res is a value between 0 and 26
    res = get_next_value(deck)
    while(res > 26 or res < 1):
        res = get_next_value(deck)

    return res


def process_message(deck, message, key):
    '''
    mutates deck
    (list of int, str, str) -> str
    Using key word 'e' or 'd' to encrypt or decrypt a message
    using the keystream provided by the deck and the formula
    provided by the code. returns the encrypted/decrypted
    message

    >>>message = "cat"
    >>>l = [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    >>>process_message(l, message, "e")
    "KHJ"

    >>>message = "KHJ"
    >>>l = [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    >>>process_message(l, message, "d")
    "CAT"

    REQ: JOKER1 exists in deck
    REQ: only one instance of JOKER1 in deck
    REQ: JOKER2 exists in deck
    REQ: only one instance of JOKER2 in deck
    REQ: JOKER1 != JOKER2
    REQ: JOKER1 < len(deck)
    REQ: All elements of deck must be smaller than len(deck)
    REQ: type(JOKER1) == int
    REQ: type(JOKER2) == int
    REQ: deck != NoneType
    '''

    # clean message to make it all capital and no symbols
    message = clean_message(message)
    res = ""

    # process based on encryption and decryption
    # runs the message through helper functions
    if(key == 'e'):
        for a in range(0, len(message)):
            res += encrypt_letter(message[a], get_next_keystream_value(deck))
    elif(key == 'd'):
        for a in range(0, len(message)):
            res += decrypt_letter(message[a], get_next_keystream_value(deck))

    return res


def process_messages(deck, messages, key):
    '''
    (list of int, str, str) -> str
    mutates deck
    Using key word 'e' or 'd' to encrypt or decrypt a message
    using the keystream provided by the deck and the formula
    provided by the code. returns the encrypted/decrypted
    message

    >>>message = ["cat", "hat", "mat"]
    >>>l = [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    >>>process_message(l, message, "e")
    ['KHJ', 'SFJ', 'XXI']

    >>>message = ["KHJ", "SFJ", "XXI"]
    >>>l = [28, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    >>>process_message(l, message, "d")
    ['CAT', 'HAT', 'MAT']

    REQ: JOKER1 exists in deck
    REQ: only one instance of JOKER1 in deck
    REQ: JOKER2 exists in deck
    REQ: only one instance of JOKER2 in deck
    REQ: JOKER1 != JOKER2
    REQ: JOKER1 < len(deck)
    REQ: All elements of deck must be smaller than len(deck)
    REQ: type(JOKER1) == int
    REQ: type(JOKER2) == int
    '''

    res = []
    # go through all the messages and send the strings to helper method
    for a in range(0, len(messages)):
        x = process_message(deck, messages[a], key)

        # cast message into list
        res += [x]

    return res


def read_messages(file_to_read):
    '''
    (io.TextIOWrapper) -> list of str
    Takes a file and reads it into a list of strings
    with the '\n' stripped from each message

    REQ: file_to_read != None
    '''

    # use readlines to read into array
    strings = file_to_read.readlines()

    # go through all array elements and strip "\n"
    for a in range(0, len(strings)):
        strings[a] = strings[a].strip("\n")

    return strings


def read_deck(file_to_read):
    '''
    (io.TextIOWrapper) -> list of int
    takes a file and reads it into a list of integers

    REQ: all string elements in file can be parsed into integer
    '''

    # since we don't want to deal with list of str load entire file into one
    # string
    integers = file_to_read.read()

    res = []
    a = 0

    # First loop just checks to make sure we don't go out of bounds for index
    while(a < len(integers)):

        # checks to see if current character is integer
        if(integers[a] in "1234567890"):

            # create a temp variable to mark starting point
            temp = a

            # add one to a since we know that a is already a number
            # we need to check the one after a
            a = a + 1

            # This loop counts the amount of digits in the integer
            # a < len(integers) has to be first else the computer
            # will check integers[a] in ["1234567890"] and go past
            # last index.
            while(a < len(integers) and integers[a] in "1234567890"):
                a = a + 1

            # take start of number(temp) and add to end of number(a)
            res.append(int(integers[temp:a]))

        # add one so that original loop does not infinitely iterate and
        # since we have already checked current character
        a = a + 1

    return res
