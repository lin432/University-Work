def banana_game(s1, s2, c):
    '''(string, string, Container) -> boolean
    returns true if we can turn s1 to s2 using container c
    methods available, get, put, peek, is_empty and copy
    '''
    ret = helper(s1, s2, 0, 0, c)

    return ret


def helper(s1, s2, i1, i2, c):
    ret = True
    temp = False
    if(i2 < len(s2)):
        if((i1 < len(s1)) and s1[i1] == s2[i2]):
            if((not c.is_empty()) and (s1[i1] == c.peek())):
                cont = c.copy()
                cont.get()
                temp = helper(s1, s2, i1, (i2 + 1), cont)
            else:
                i1 += 1
                i2 += 1
                ret = helper(s1, s2, i1, i2, c)
        elif((not c.is_empty()) and (c.peek() == s2[i2])):
            c.get()
            i2 += 1
            ret = helper(s1, s2, i1, i2, c)
        else:
            if(i1 < len(s1)):
                c.put(s1[i1])
                i1 += 1
                ret = helper(s1, s2, i1, i2, c)
            else:
                ret = False

    if(temp or ret):
        ret = True

    return ret
