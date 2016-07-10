'''This module should be used to test the parameter and return types of your
functions. Before submitting your assignment, run this type-checker. This
typechecker expects to find files reading.py, squeal.py, and
the .csv files provided in the starter code.

If errors occur when you run this typechecker, fix them before you submit
your assignment.

If no errors occur when you run this typechecker, then the type checks passed.
This means that the function parameters and return types match the assignment
specification, but it does not mean that your code works correctly in all
situations. Be sure to test your code before submitting.
'''

import reading
from database import *


def is_table(t):
    if not isinstance(t, Table):
        return False
    d = t.get_dict()
    if not isinstance(d, dict):
        return False
    for k in d:
        if not isinstance(k, str):
            return False
        value = d[k]
        if not isinstance(value, list):
            return False
        for s in value:
            if not isinstance(s, str):
                return False
    return True


def is_database(db):
    if not isinstance(db, Database):
        return False
    d = db.get_dict()
    if not isinstance(d, dict):
        return False
    for k in d:
        if not isinstance(k, str):
            return False
        value = d[k]
        if not is_table(value):
            return False
    return True

# typecheck the reading.py functions
result = reading.read_table('books.csv')
assert is_table(result), \
    'read_table should return a table; please check the handout \
    for the definition of a table.'

# typecheck reading.read_database
result = reading.read_database()
assert is_database(result), \
    'read_database should return a database; please check the handout \
    for the definition of a database.'

# typecheck the required squeal.py function
import squeal
d1 = {'a': ['b', 'c']}
d2 = {'d': ['e', 'f']}
t1 = Table()
t2 = Table()
t1.set_dict(d1)
t2.set_dict(d2)

result = squeal.cartesian_product(t1, t2)
assert is_table(result), \
    'cartesian_product should return a table; please check the handout \
    for the definition of a table.'
