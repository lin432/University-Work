'''This module should be used to test the parameter and return types of your
functions. Before submitting your assignment, run this type-checker. This
typechecker expects to find file puzzles.py.

If errors occur when you run this typechecker, fix them before you submit
your assignment.

If no errors occur when you run this typechecker, then the type checks passed.
This means that the function parameters and return types match the assignment
specification, but it does not mean that your code works correctly in all
situations. Be sure to test your code before submitting.
'''

import a0 as puzzles


# Type check puzzles.total_occurrences
result = puzzles.total_occurrences('abc', 'a')
assert isinstance(result, int), \
    '''total_occurrences should return an int, but returned {0}''' \
    .format(type(result))

# Type check puzzles.in_puzzle_horizontal
result = puzzles.in_puzzle_horizontal('abc', 'a')
assert isinstance(result, bool), \
    '''in_puzzle_horizontal should return a bool, but returned {0}''' \
    .format(type(result))

# Type check puzzles.in_puzzle_vertical
result = puzzles.in_puzzle_vertical('abc', 'a')
assert isinstance(result, bool), \
    '''in_puzzle_vertical should return a bool, but returned {0}''' \
    .format(type(result))

# Type check puzzles.in_puzzle
result = puzzles.in_puzzle('abc', 'a')
assert isinstance(result, bool), \
    '''in_puzzle should return a bool, but returned {0}''' \
    .format(type(result))


# Type check puzzles.in_exactly_one_dimension
result = puzzles.in_exactly_one_dimension('abc', 'a')
assert isinstance(result, bool), \
    '''in_exactly_one_dimension should return a bool, but returned {0}''' \
    .format(type(result))


# Type check puzzles.all_horizontal
result = puzzles.all_horizontal('abc', 'a')
assert isinstance(result, bool), \
    '''all_horizontal should return a bool, but returned {0}''' \
    .format(type(result))


# Type check puzzles.at_most_one_vertical
result = puzzles.at_most_one_vertical('abc', 'a')
assert isinstance(result, bool), \
    '''at_most_one_vertical should return a bool, but returned {0}''' \
    .format(type(result))

print("If you see this (and no error messages above it), \
then you have passed the type checker")
