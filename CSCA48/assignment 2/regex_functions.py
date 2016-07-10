"""
# Copyright Nick Cheng, Brian Harrington, Danny Heap, Lintao Yin 2013, 2014,
# 2015, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2016
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from regextree import RegexTree, StarTree, DotTree, BarTree, Leaf

# Do not change anything above this comment except for the copyright
# statement

# Student code below this comment.


def is_regex(s):
    '''(string) -> boolean
    checks if the given string is a valid regular expression based on the
    rules outlined on assignment 2

    >>>is_regex('e')
    True
    >>>is_regex('(e*)|(2|(1|0))')
    True
    >>>is_regex('.e|e*|5')
    False

    REQ: type(s) == str'''
    index = 0
    ret = False
    # uses helper method to get the values, however helper method only
    # checks till end and may miss cases such as 'eee'
    (index, ret) = _try_next(s, index, len(s))

    # this is why this check exists such that if a string still exists past
    # a valid portion
    if((index + 1) != len(s)):
        ret = False

    return ret


def _try_next(s, index, end):
    '''(string, int, int) -> (int, boolean)
    helper method that takes a string and then tries two different techniques
    to verify the regex, 1. sends finds a binary and sends it to binary
    helper, 2. finds a value and checks it's an accepted value
    returns the end index and the boolean on whether the structure is a valid
    regex expression

    >>>_try_next('e', '0', '1')
    (0, True)
    >>>_try_next('(1|0)', 0, 5)
    (4, True)
    >>>_try_next('(e*|(2|(1|0)))', 0, 14)
    (13, True)
    >>>_try_next('(*(*()', 0, 6)
    >>>(1, False)

    REQ: end = len(s)
    REQ: index > 0'''
    ret = False
    # checks if the string just abruptly ends
    if(index != end):
        # case where there's a binary and we then send it to the binary helper
        if(s[index] == '('):
            if((index + 1) < end):
                (index, ret) = _try_binary(s, index + 1, end)

        # case where it's a value and checks as an allowed value
        elif(_is_val(s[index])):
            ret = True

            # checks for '*' and increments one if it exists
            # if the next value isn't a star then is_regex will catch
            # it if it isn't valid and there are still strings left in
            # the passed expression
            if((index + 1) < end and s[index + 1] == '*'):
                index = index + 1

    return (index, ret)


def _try_binary(s, index, end):
    '''(string, int, int) -> (int, boolean)
    helper that checks whether the string at index is a valid
    binary regex

    >>>_try_binary('e', 0, 1)
    (0, False)
    >>>_try_binary('(1|1)', 1, 5)
    (4, True)
    >>>_try_binary('((1.1)|1*)*', 1, 11)
    (10, True)

    REQ: s is of the form '(e1|e2)' or '(e1.e2)' where e1 and e2 are strings
    '''
    expressions = {'|', '.'}
    ret = False
    l = False

    # tries to get whether the left argument for binary is valid
    (index, l) = _try_next(s, index, end)
    if(l):
        # it is so we check the expression and whether it exists
        expression = 'fail'
        if((index + 1) < end):
            index = index + 1
            expression = s[index]
        if(expression in expressions):
            # expression is allowed so we check right argument
            r = False
            if((index + 1) < end):
                # exists so we try changing value
                (index, r) = _try_next(s, index + 1, end)
            if(r):
                # right argument is valid try finding end bracket
                if((index + 1) < end):
                    index = index + 1
                    if(s[index] == ')'):
                        # found so we just need to check for star
                        ret = True
                        if((index + 1) < end and s[index + 1] == '*'):
                            # star exists so we add to index
                            index = index + 1
    return (index, ret)


def _is_val(s):
    '''(string) -> boolean
    returns true if the value is a valid
    regex value of strings 0,1,2,e

    Ex.
    >>> _is_val('0')
    True
    >>> _is_val('')
    False
    >>> _is_val('7')
    False

    REQ: len(s) == 1'''
    values = {'0', '1', '2', 'e'}
    ret = False
    # checks set
    if(s in values):
        ret = True
    return ret


def all_regex_permutations(s):
    '''(string) -> set of strings
    takes a valid regex expression and
    returns a set of all permutations that are valid regexes
    based on the regex expression given.

    My method works by first
    permutating all the values then inserting the binary operations.
    Then playing with how they mesh(brackets) and finally permuting stars
    by adding and not adding at any two locations by the end the set will
    then be valid.

    >>>all_regex_permutations('(e|1)')
    {'(e|1)', '(1|e)'}

    REQ: is_regex(s) == True
    '''
    # create the default counters for all the characters
    binary_count = {'|': 0, '.': 0}
    unary_count = {'*': 0}
    values_count = {'e': 0, '1': 0, '2': 0, '0': 0}
    bracket_count = {'(': 0, ')': 0}
    permutations = set()

    # get the keys of the expressions
    binary = binary_count.keys()
    unary = unary_count.keys()
    values = values_count.keys()
    brackets = bracket_count.keys()

    total_bin = 0
    total_un = 0
    total_val = 0
    total_br = 0

    error = False
    # count all the values
    for char in s:
        if (char in binary):
            binary_count[char] += 1
            total_bin += 1
        elif(char in unary):
            unary_count[char] += 1
            total_un += 1
        elif(char in values):
            values_count[char] += 1
            total_val += 1
        elif(char in brackets):
            bracket_count[char] += 1
            total_br += 1
        else:
            error = True
            ret = set()

    if(not (total_bin + 1) == total_val):
        error = True
    if(bracket_count['('] != bracket_count[')']):
        error = True
    if(total_un > (total_val + total_bin)):
        error = True

    if(not error):
        # permutate values
        permutations = _permutate_values(values_count)
        # permutate all binaries and brackets
        if(total_bin > 0):
            permutations = _permutate_binary(permutations, binary_count)
        # permutate all the stars
        if(total_un > 0):
            permutations = _permutate_star(permutations, total_un)

    return permutations


def _permutate_binary(perms, binary):
    '''(set of str, {str:int}) -> set of str
    permutates all binary expressions into each string of regex values
    The task is split into two parts, the actual binaries{'|', '.'} which
    always seperate a value and the position of the brackets which
    are based on the length of the string

    >>>_permutate_binary{'e1','1e'}, {'|':1, '.':0}
    {'(1|e)','(e|1)'}

    REQ: sum off all values in binary != 0'''
    # creates a new set as the one passed would hold just values
    bin_set = set()

    # adds all the binary operations first using a helper
    for item in perms:
        temp = _permutate_binary_helper(1, len(item), binary, item)
        bin_set = bin_set.union(temp)

    # counts the number of binary operations in the string
    operations = 0
    for item in binary:
        operations += binary[item]

    # uses a helper to get all the patterns that represent
    # left brackets (I'm constructing right brackets later)
    bracket_set = _bracket_creator(operations)

    # then adds all the brackets into each possible combination of
    # values and binaries
    ret_set = set()
    for item in bin_set:
        for bracket in bracket_set:
            ret_set.add(_construct_pair(item, bracket))

    return ret_set


def _permutate_binary_helper(index, end, binary, string):
    '''(int, int, set of str, {str:int}, str) -> set of str
    Permutes all the binary expressions into the set of just values

    >>>_permutate_binary_helper(0, 2,{'1e', 'e1'}, {'|':1}, '')
    {'1|e', 'e|1'}

    REQ: index < end
    REQ: perms != None
    REQ: length of all items in perms > 0
    REQ: binary != None
    REQ: length of all items in perms == (sum of all items in binary) + 1
    '''

    ret = set()
    # we've reached the end so we stop and return the value
    if(index == end):
        ret = {string}
    else:
        # goes through all the binary operations given
        keys = binary.keys()
        for item in keys:
            # creates a new temp dict that keeps track of the number of
            # binaries that exist in this iteration
            if(binary[item] > 0):
                temp_binary = binary.copy()
                temp_binary[item] += -1
            # creates a string based on that binary
                new_string = string[:(index)] + item + string[(index):]
            # sends it recursively to the next portion to permutate it further
                temp = _permutate_binary_helper((index + 2), (end + 1),
                                                temp_binary, new_string)
                ret = ret.union(temp)
    return ret


def _bracket_creator(operations):
    '''(int) -> list of (list of int, list of int)
    returns a list with dicts that represent the locations for the brackets
    in relation to the string.

    >>>_bracket_creator(1)
    {([1],[0,1])}

    REQ: operations > 0'''
    l_brackets = [1] * operations
    # fill brackets with 1

    # grab all combinations without right brackets
    left_set = _bracket_helper(l_brackets, 0, operations)

    ret_set = []
    # takes all the left_brackets and pairs them
    for item in left_set:
        right_list = _place_right_bracket(item, operations)
        temp = (item, right_list)
        ret_set.insert(0, temp)

    return ret_set


def _bracket_helper(l_brackets, index, end):
    '''([int], int, int) -> list of list of int
    creates the set of all the possible permutations
    of the brackets. The algorithim works on the fact that
    each bracket from position of (e|(e|(e|....
    is only valid if it grabs consecutive brackets from
    ahead of it. I.E. (e|(e|(e|e)))) and (e|((e|e)|e))
    based on this we can create all possible permutations
    for any number of brackets

    >>>_bracket_helper([1], 0, 1)
    [[1]]

    REQ: index < end
    '''
    # the strategy for permuting brackets is that in order to increase
    # one bracket we must take the bracket ahead of it in order to
    # keep it as a valid regex, if we already have taken the one after it
    # then we take the one even further

    # makes sure we haven't already taken everything ahead of this one
    perms = []
    if(l_brackets[index] < (end - index)):
        # we start at the index because the ones that are running before
        # this one will deal with the cases where this index is also
        # increased.
        for i in range(index, end):
            # tries to find the next i with number > 1
            a = i + 1
            while(a < end and l_brackets[a] < 1):
                a += 1

            # checks to make sure that i + a is actually > 0
            if(a < end and l_brackets[a] > 0):
                # copies brackets, adds i+a to a and removes a number at
                # i + a
                temp_brackets = l_brackets[:]
                temp_brackets[i] += 1
                temp_brackets[a] += -1
                # continues to recursively permutate
                perms += _bracket_helper(temp_brackets, i, end)
    # add the current bracket since it is valid
    perms.insert(0, l_brackets)

    return perms


def _place_right_bracket(l_left, end):
    '''(list of int, int) -> (list of int)
    creates a list of right_brackets based on the location of the left
    brackets. The relationship of the right bracket placement is based on
    starting at the last left bracket, place one across from it. if there
    is more than one bracket we move spots n number of times where n is
    the number of brackets > 1 at that location. we remember the space
    of the last right bracket. moving backwards if there is an empty space
    it is now the location of our las right bracket. if it isn't empty then
    we add right brackets to the current right bracket location following the
    same n>1 rule

    >>>_place_right_bracket([1], 1)
    [0, 1]

    REQ: len(l_left) > 0'''
    # create list of right brackets we add one more as in my implementation
    # list of left brackets never uses last operation other wise the string
    # is incorrect
    l_right = [0]*(end + 1)

    right_bracket_end = end
    # goes through the left list in reverse to try and find the first
    # '(' from the end, we do this as it offsets the current location of
    # the next expected ')'
    for i in range((end - 1), -1, -1):
        if(l_left[i] > 1):
            # we have more than one '(' so we need to offset the right_bracket
            # so we need to offset the rght_bracket_end by at least n-1 spaces
            for offset in range(0, l_left[i]):
                # if we find a leftbracket we need to bounce spaces
                # till the current location isn't a left_bracket
                if((right_bracket_end + offset) < len(l_left)):
                    # we can check_left bracket(not at end of list)
                    if(l_left[right_bracket_end + offset] > 0):
                        # left_bracket has a spot so we need to find out
                        # where it ends
                        current_spot = right_bracket_end + offset
                        while(current_spot < len(l_left) and
                              l_left[current_spot] > 0):
                            # iterates until end
                            current_spot += 1
                        # updates right_bracket_end
                        right_bracket_end = current_spot - offset

                # adds to l_right
                l_right[(right_bracket_end + offset)] += 1

            right_bracket_end += l_left[i] - 1
        elif(l_left[i] == 1):
            # we have just one bracket so we add it to the end
            l_right[right_bracket_end] += 1
        elif(l_left[i] == 0):
            # no left_bracket this becomes the new point of right_bracket
            right_bracket_end = i

    return l_right


def _construct_pair(item, bracket):
    '''(str, ([int],[int])) -> str
    takes a string representing the value and binary operation
    then adds the brackets based on the location of the brackets

    >>>_construct_pair('1|e', ([1], [0, 1]))
    '(1|e)'

    REQ: (len(item) - 1) = sum of all items in bracket'''
    l_bracket = None
    r_bracket = None
    (l_bracket, r_bracket) = bracket

    # do first bracket so the rest of the algorithm works
    ret = ('(' * l_bracket[0]) + item
    # use recursive method to go through rest
    ret = _construct_pair_helper(l_bracket[0], 1, ret, l_bracket, r_bracket)
    # do last bracket so the rest of the algorithm works
    ret = ret + (')' * r_bracket[(len(r_bracket) - 1)])

    return ret


def _construct_pair_helper(i_str, i_br, s, l_bracket, r_bracket):
    '''(int, int, str, ([int],[int]), str) -> str
    takes all of the info above and inserts brackets at the next
    binary available from i_str to string s

    >>>_construct_pair_helper(0, 0, '1|e', ([1], [0, 1]), '')
    '(1|e)'

    REQ: i_str < len(s)
    '''
    # checks whether we still have brackets to add
    if(i_br < (len(r_bracket))):
        # initializes binary list and string
        binary = {'.', '|'}
        string = s

        # tries to find next binary location
        i_bin = i_str
        right_add = r_bracket[(i_br - 1)]
        left_add = 0
        while(s[i_bin] not in binary):
            i_bin += 1
        string = s[:i_bin] + (')' * right_add) + s[i_bin]
        if(i_br < len(l_bracket)):
            left_add = l_bracket[i_br]
            string += '(' * left_add
        if((i_bin + 1) < len(s)):
            string += s[(i_bin + 1):]

        i_str = i_bin + left_add + right_add + 1
        s = _construct_pair_helper(i_str, (i_br + 1), string, l_bracket,
                                   r_bracket)

    return s


def _permutate_values(values, string=''):
    '''(set, {str:int}) -> set
    returns a set of all permutations of the number of accepted values
    in a regex expression

    >>>_permutate_values({}, {'e':1, '1':1})
    {'1e', 'e1'}

    REQ: values != None'''
    # assume done until iterating dict
    perms = set()
    finished = True
    for item in values:
        # checks if there are any items in the dict
        if(values[item] > 0):
            # there are so we say that there are still values to add
            finished = False

    if(finished):
        # no values to add so we add string to the set of all value
        # permutations
        perms = {string}
    else:
        # there are values to continue adding so we loop and try and find them
        for item in values:
            if(values[item] > 0):
                # found a value so we must subtract its reptitions
                temp_values = values.copy()
                temp_values[item] += -1
                # then recursively continue searching
                perms = perms.union(_permutate_values(temp_values,
                                    (string + item)))
    # return the combined set of all permutations
    return perms


def _permutate_star(perms, star_count):
    '''(set of str, int) -> set of str
    iterates through all the strings and uses a helper to go through them
    and returns a string representing the permutations of all
    regex expressions with stars

    >>>_permutate_star({'(1|e)', '(e|1)'}, 1)
    {'(*1|e)', '(1|e*)', '(1|e)*', '(e*|1)', '(e|1*)', '(e|1)*'}

    REQ: star_count > 0'''
    ret = set()
    # for each string it goes through and splices the star using a helper
    for item in perms:
        ret.union(_permutate_star_helper(0, len(item), ret, star_count, item))

    return ret


def _permutate_star_helper(index, end, perms, star_count, s):
    '''(int, int, set of str, int, str) -> set of str
    goes through the options of having a star in the position and
    not having a star, adds only if the string has used all
    the stars

    >>>_permutate_star_helper(0, 5, {}, 1, '1|e')
    {'(*1|e)', '(1|e*)', '(1|e)*'}

    REQ: index < end'''
    if(index < end and star_count > 0):
        while(index < end):
            if(_is_val(s[index]) or s[index] == ')'):
                # assembles string with star value in middle
                star_string = s[:index+1] + '*' + s[index+1:]
                # iterates up two to reach next non '*'
                i = index + 2
                # gets the recursive set of strings
                ret_set = _permutate_star_helper(i, (end + 1), perms,
                                                 (star_count - 1), star_string)
                perms.union(ret_set)

                # recursively asks for next without the star
                ret_set = _permutate_star_helper((i-1), end, perms, star_count,
                                                 s)

            index += 1
    else:
        # adds to perms only if we've used up all the stars
        if(star_count == 0):
            perms.add(s)

    return perms


def regex_match(r, s):
    # what about cases with index+ fails but 'e' does not
    # what about cases where * takes all values and we have a . at end?
    '''(RegexTree, string) -> Boolean
    returns true if string s matches tree at r

    >>>t = build_regex_tree('(((1.0)*|(2|e)).1)')
    >>>s = '1010101'
    >>>regex_match(t,s)
    True

    >>>t = build_regex_tree('(((1.0)*|(2|e)).1)')
    >>>s = '101010'
    >>>regex_match(t,s)
    False

    >>>t = build_regex_tree('e')
    >>>s = ''
    >>>regex_match(t,s)
    True

    REQ: is_regex(s) == True
    '''
    ret = False
    (i, ret, index_up) = _determine_node(r, s, 0, len(s))

    # didn't go through it all so we know there is some missing
    if((i + 1) < len(s)):
        ret = False
    return ret


def _determine_node(r, s, index, end):
    '''(RegexTree, string, int, int) -> (int, boolean, boolean)
    determines what the node is and then sends it to the appropriate
    recursive method

    >>>_determine_node(BarTree(Leaf('1'), Leaf('1')), '1', 0, 1)
    (1, True, True)

    >>>_determine_node(BarTree(Leaf('e'), Leaf('2')), '', 0, 0)
    (0, True, False)

    >>>_determine_node(StarTree(Leaf('1')), '111', 0, 3)
    (2, True, True)

    >>>_determine_node(Leaf('2'), '2', 0, 1)
    (0, True, True)

    REQ: r = valid regex tree
    REQ: index < end
    REQ: type(r) == BarTree or StarTree or DotTree or Leaf
    '''
    # this will fail
    contin = False
    index_up = True
    if(isinstance(r, StarTree)):
        (index, contin, index_up) = _check_star(r, s, index, end)
    elif(isinstance(r, BarTree)):
        (index, contin, index_up) = _check_bar(r, s, index, end)
    elif(isinstance(r, DotTree)):
        (index, contin, index_up) = _check_dot(r, s, index, end)
    else:
        # r is a leaf
        val = r.get_symbol()
        if(val == 'e'):
            contin = True
            index_up = False
        elif(index < end):
            if(val == s[index]):
                contin = True

    return (index, contin, index_up)


def _check_bar(r, s, index, end):
    '''(BarTree, string, int, int) -> (int, boolean, boolean)
    helper method that checks the bar condition of the string

    >>>_check_bar(BarTree(Leaf('1'), Leaf('1')), '11', 0, 2)
    (0, True, True)
    >>>_check_bar(BarTree(Leaf('e'), Leaf('1')), '11', 0, 2)
    (0, True, False)
    >>>_check_bar(BarTree(Leaf('1'), Leaf('1')), '21', 0, 2)
    (0, False, True)

    REQ: type(r) == BarTree
    REQ: index < end'''
    check = False
    index_up = False
    # tries the left child to get either a leaf or whether
    # the next tree is true as well
    # we need a temp index so the right side also parses properly
    l_index = index
    (l_index, check, index_up) = _determine_node(r.get_left_child(), s, index,
                                                 end)

    # if the left side is not true or we have an 'e' then we try the right
    if((not check) or (not index_up)):
        check2 = False
        index_up2 = False
        # try the right tree and see if that is true since left is false
        # or we have an e and we're trying to not get an 'e'
        (index, check2, index_up2) = _determine_node(r.get_right_child(), s,
                                                     index, end)

        # check of right side passed
        if(check2):
            # we know we are replacing something
            # if left side failed replace everything
            if(not check):
                check = check2
                index_up = index_up2
                l_index = index
            # if left side suceeded then we know index_up failed
            # so we try to check if we can do a index_up
            elif(index_up2):
                index_up = True
                l_index = index

    return (l_index, check, index_up)


def _check_dot(r, s, index, end):
    '''(DotTree, string, int, int) -> (int, {str: int}, boolean)
    helper method that checks the bar condition of the string

    >>>_check_dot(DotTree(Leaf('1'), Leaf('1')), '11', 0, 2)
    (1, True, True)
    >>>_check_dot(DotTree(Leaf('1'), Leaf('2')), '11', 0, 2)
    (1, False, True)

    REQ: index < end
    REQ: type(r) == DotTree'''
    check = False
    index_up = True
    first_index = index
    # tries left value
    (index, check, index_up) = _determine_node(r.get_left_child(), s, index,
                                               end)
    # if left side failed then we can just stop

    if(check):
        # checks if the value was 'e' if it isn't then add one to move through
        # the list
        if (index_up):
            index = index + 1
        # gets the next values
        (index, check, index_up) = _determine_node(r.get_right_child(), s,
                                                   index, end)
    return (index, check, index_up)


def _check_star(r, s, index, end):
    # save the value if it has been done, continue if the value is
    # in the saved, redo if it is not
    '''(StarTree, string, int, int) -> (int, {str:int}, boolean)
    helper method that checks the bar condition of the string

    >>>_check_star(StarTree(Leaf('1')), '', 0, 0)
    (1, True, False)

    >>>_check_star(StarTree(Leaf('1')), '111', 0, 0)
    (3, True, False)

    >>>_check_star(StarTree(Leaf('1')), '112', 0, 0)
    (2, True, False)

    REQ: index < end
    REQ: type(r) == StarTree'''
    previous_val = {}
    check = True
    index_up = True
    index_end = 0
    skip = False

    # stops when either we reach end value or we are returned a false or 'e'
    while(check and index_up and index < end):
        # values to loop on the already accepted strings
        dict_index = 0
        keys = previous_val.keys()
        # goes through and checks whether we have a word already found
        while (not skip) and (dict_index < len(keys)):
            # grabs one of the previous values
            item = keys[dict_index]
            # grabs portion of master string to check
            s_check = s[index: (index + previous_val[item])]
            if(s_check == item):
                # same so we activate skip
                skip = True
                # we have to increase index but the amount of previous value
                index += previous_val[item]
            else:
                # try looping to find another one
                dict_index += 1

        if(not skip):
            # try finding a new value
            (index_end, check, index_up) = _determine_node(r.get_child(), s,
                                                           index, end)
            if(check and index_up):
                string_works = s[index:(index_end+1)]
                index += len(string_works)
                previous_val[string_works] = len(string_works)

        skip = False
    # star is never false and we always by this alogrithim need not increase
    # the location of the string once finished
    return (index, True, False)


def build_regex_tree(regex):
    '''(string) -> RegexTree
    returns the root of the regex tree that represents a regex expression

    >>>build_regex_tree('(1|1)')
    BarTree(Leaf('1'), Leaf('1'))
    >>>build_regex_tree('e*')
    StarTree(Leaf('e'))
    >>>build_regex_tree('((1|1)*.(0|2))*')
    StarTree(DotTree(StarTree(BarTree(Leaf('1'), Leaf('1'))),
    BarTree(Leaf('0'), Leaf('2'))))

    REQ: is_regex(regex) == True'''
    ret = None
    end = len(regex)

    # sends to helper method
    (i, ret) = _create_regex(regex, 0, end)
    return ret


def _create_regex(s, index, end):
    '''(string, int, int) -> (int, RegexTree):
    helper method for _create_binary, reads the string and sends
    to the appropriate method to create the appropriate tree

    >>>_create_regex('(1|1)', 0, 5)
    (4,BarTree(Leaf('1'), Leaf('1')))
    >>>_create_regex('e*', 0, 2)
    (1, StarTree(Leaf('e')))
    >>>_create_regex('((1|1)*.(0|2))*', 1, 14)
    (6, StarTree(BarTree(Leaf('1'), Leaf('1'))))

    REQ:'''
    ret = None
    # checks if the value is a binary expression
    # and sends to appropriate recursive creator
    # we always pass an index so we know where we are in the list
    if(s[index] == '('):
        # we have a binary so we send it to binary creator
        (index, ret) = _create_binary(s, index, end)
    else:
        # we have a value so we send it to value creator
        (index, ret) = _create_val(s, index, end)
    return (index, ret)


def _create_binary(s, index, end):
    '''(string, int, int) -> (int, RegexTree)
    takes a string and returns a binary RegexTree node
    based on whether it is '|' or '.' as well as a int
    that represents the end of the bracket

    >>>_create_binary('(1|1)', 0, 5)
    (4, BarTree(Leaf('1'), Leaf('1')))
    >>>_create_binary('(1|(2.1)*)', 3, 10)
    (8, StarTree(DotTree(Leaf('2'), Leaf('1'))))

    REQ: s is of the form '(e1|e2)' or '(e1.e2)' where e1 and e2 are strings
    REQ: (index + 5) < end
    REQ: end == len(s)
    '''
    l = None
    r = None

    # sends to helper method to decide whether we need to
    # create a binary or value
    (index, l) = _create_regex(s, index + 1, end)

    # gets the expression
    index = index + 1
    expression = s[index]
    index = index + 1

    # uses helper method to get right node
    (index, r) = _create_regex(s, index, end)
    # adds to get to end bracket
    index = index + 1

    ret = None
    # creates based on either dot or bar
    if(expression == '.'):
        ret = DotTree(l, r)
    elif(expression == '|'):
        ret = BarTree(l, r)

    # checks end for star and creates star if it exists
    if((index + 1) < end):
        if(s[index + 1] == '*'):
            index = index + 1
            ret = StarTree(ret)
    return (index, ret)


def _create_val(s, index, end):
    '''(string, int, int) -> (int, RegexTree)
    takes a string and returns either a leaf or a star tree
    and returns an int that represents the index of the value or star

    >>>_create_val('(1|1)', 1, 5)
    (1, Leaf('1'))
    >>>_create_val('((1|(2.0)*).(2.e*))', 15, 19)
    (16, StarTree(Leaf('e')))

    REQ: s is a string
    REQ: index > -1
    REQ: end == len(s)'''
    # creates leaf node of value
    leaf = Leaf(s[index])
    # checks for star
    if(index + 1 < end):
        if(s[index + 1] == '*'):
            leaf = StarTree(leaf)
            index = index + 1

    return (index, leaf)
