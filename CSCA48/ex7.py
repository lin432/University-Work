def edit_distance(s1, s2):
    '''(string, string) -> int
    figures out the minimum number of character switches
    to get s1 into s2'''
    return _edit_distance(s1, s2, 0, len(s1))


def _edit_distance(s1, s2, curr, end):
    '''(string, string, int, int) -> int
     helper methd'''
    ret = 0
    if(curr < end):
        change = 0

        if(s1[curr] != s2[curr]):
            change = 1

        x = _edit_distance(s1, s2, (curr + 1), end)
        ret = x + change

    return ret


def subsequence(s1, s2):
    '''(string, string) -> boolean
    returns true if s1 is a subsequence of s2'''
    return _subsequence1(s1, s2, 0, 0, len(s1), len(s2))


def _subsequence1(s1, s2, s1_index, s2_index, end1, end2):
    '''(string, string, int, int, int, int) -> boolean
    helper method that goes through s1'''
    ret = True
    if(s1_index < end1):
        want = s1[s1_index]
        (ret, s2_index) = _subsequence2(want, s2, s2_index, end2)

        if(ret is not False):
            ret = _subsequence1(s1, s2, (s1_index + 1), (s2_index + 1),
                                end1, end2)
    return ret


def _subsequence2(want, s, index, end):
    '''(string, string, int, int, int, int) -> boolean
    helper method for subsequence that goes through s2'''
    ret = (False, end)
    if(index < end):
        if(want == s[index]):
            ret = (True, index)
        else:
            ret = _subsequence2(want, s, index+1, end)
    return ret


def perms(s):
    '''(string) -> set of strings
    returns a set of all the permutations of s'''
    ret = {}
    if(s is not None):
        work_string = s[:]
        ret = _perms(work_string, '', len(s))
    return ret


def _perms(s, ret_string, end):
    '''(string, string) -> set of string
    helper method to return a set of all permuations in s'''
    if(end > 0):
        set_ret = set()
        for a in range(0, end):
            char = s[a]
            leftovers = s[:a] + s[a+1:]
            temp_string = ret_string + char
            s_returned = _perms(leftovers, temp_string, (end-1))
            for val in s_returned:
                set_ret.add(val)

        ret = set_ret
    else:
        ret = {ret_string}
    return ret
