# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Lintao Yin
# MarkUs Login: yinlinta
#

PUZZLE1 = '''
glkutqyu
onnkjoaq
uaacdcne
gidiaayu
urznnpaf
ebnnairb
xkybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyotiutuvpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    >>> total_occurrences('ab/ncd', 'ab')
    1

    REQ: puzzle != None
    REQ: word != None
    '''
    # your code here

    total = 0

    # segment that counts first side of puzzle
    # rotates and adds 3 times to count the other sides
    total = total + lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)

    total = total + lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)

    total = total + lr_occurrences(puzzle, word)
    puzzle = rotate_puzzle(puzzle)

    total = total + lr_occurrences(puzzle, word)

    return total

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> boolean
    Returns true if the word can be located in
    the puzzle from directions left-right or right-left

    >>> in_puzzle_horizontal('cat\ntac', 'cat')
    True
    >>> in_puzzle_horizontal('ab\ncd', 'cda')
    False

    REQ: puzzle != None
    REQ: word != None
    '''

    # checks that original left-right word occurrences is not 0
    # then checks if the puzzle rotated twice to orient
    # left-right has any occurrences
    return (lr_occurrences(puzzle, word) or
            lr_occurrences(rotate_puzzle(
                rotate_puzzle(puzzle)), word)) > 0

# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> boolean
    Returns true if the word can be located in
    the puzzle from directions top-bottom or bottom-top

    >>> in_puzzle_vertical('cat\naac\ntac', 'cat')
    True
    >>> in_puzzle_vertical('ab\ncd', 'cda')
    False

    REQ: puzzle != None
    REQ: word != None
    '''
    # checks that top-bottom word occurrences is not 0
    # then checks if the puzzle rotated twice to orient
    # bottom-top has any occurrences
    return (lr_occurrences(rotate_puzzle(puzzle), word) or
            lr_occurrences(rotate_puzzle(rotate_puzzle(
                rotate_puzzle(puzzle))), word)) > 0


# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.

def in_puzzle(puzzle, word):
    '''
    (str, str) -> boolean
    Returns true if the word can be located in
    the puzzle from any direction: left-right,
    right-left, top-bottom, bottom-top

    >>> in_puzzle('cat\naac\ntac', 'cat')
    True
    >>> in_puzzle('ab\ncd', 'cda')
    False

    REQ: puzzle != None
    REQ: word != None
    '''
    # uses in_puzzle_vertical and in_puzzle_horizontal
    # to determine if the puzzle has the word in it
    # and returns result
    return in_puzzle_vertical(puzzle, word) or \
        in_puzzle_horizontal(puzzle, word)

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''
    (str, str) -> boolean
    Returns true if the word can be located in the
    puzzle from either the vertical column or the
    horizontal column

    >>> in_puzzle('cat\naac\ntac', 'cat')
    False
    >>> in_puzzle('ab\ncd', 'dc')
    True

    REQ: puzzle != None
    REQ: word != None
    '''

    # There are only two cases to check for
    # either it exists in vertical but not
    # horizontal or it exists in horizontal
    # but not vertical
    return (in_puzzle_vertical(puzzle, word) and (not
            in_puzzle_horizontal(puzzle, word))) or \
        (in_puzzle_horizontal(puzzle, word) and (not
            in_puzzle_vertical(puzzle, word)))


# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''
    (str, str) -> boolean
    Returns true if the word cannot be
    found vertically, therefore implying
    that all examples exist horizontally

    >>> in_puzzle('cat\naac\ntac', 'cat')
    False
    >>> in_puzzle('ab\ncd', 'dc')
    True

    REQ: puzzle != None
    REQ: word != None
    '''
    # checks only that in_puzzle_vertical does
    # not return true, meaning both requirements
    # of returning true when horizontal or empty
    # exists
    return not in_puzzle_vertical(puzzle, word)

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''
    (str, str) -> boolean
    Returns true if the word can only
    be found be found once vertically

    >>> in_puzzle('cat\naac\ntac', 'cat')
    False
    >>> in_puzzle('ab\ncd', 'ac')
    True

    REQ: puzzle != None
    REQ: word != None
    '''
    # checks if there is only one word
    # then checks if that word is vertical

    return (total_occurrences(puzzle, word) == 1) and \
        in_puzzle_vertical(puzzle, word)


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here

    # uses built-in lr-occurrences method to count names in direction
    # left-right
    print(lr_occurrences(puzzle, name))

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!

    # prints default line but rotates puzzle such that when running
    # lr_occurences we have the code running top-bottom instead
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    puzzle = rotate_puzzle(puzzle)
    print(lr_occurrences(puzzle, name))

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.

    # see 1b) comments
    print('Number of times', name, 'occurs right-to-left: ', end='')
    puzzle = rotate_puzzle(puzzle)
    print(lr_occurrences(puzzle, name))

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.

    # see 1b) comments
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    puzzle = rotate_puzzle(puzzle)
    print(lr_occurrences(puzzle, name))

    # right puzzle to original orientation
    puzzle = rotate_puzzle(puzzle)

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.

    print(total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.

    print (in_puzzle_horizontal(puzzle, name))

    # test print of the rest of the methods below
    #print (in_puzzle_vertical(puzzle, name))

    #print (in_puzzle(puzzle, name))

    #print (in_exactly_one_dimension(puzzle, name))

    #print (all_horizontal(puzzle, name))

    #print (at_most_one_vertical(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')


# *task* 7: call do_tasks on PUZZLE2 (that's a 2!) and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'brian')
do_tasks(PUZZLE2, 'nick')
do_tasks(PUZZLE2, 'zaacfas')


# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'anya'.
# Add only one line below. Your code should print only True or False.
do_tasks(PUZZLE2, 'anya')
