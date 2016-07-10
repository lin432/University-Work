def rsum(l):
    l = l[:]
    if(len(l) == 0):
        return 0
    else:
        x = l.pop()
        return x + rsum(l)


def rmax(l):
    l = l[:]
    x = l.pop()
    y = None
    if(len(l) == 0):
        y = x-1
    else:
        y = rmax(l)

    ret = None
    if(x > y):
        ret = x
    else:
        ret = y

    return ret


# sm = smallest of two
def second_smallest(l, sm=9999999999, ssm=9999999999):
    l = l[:]
    x = l.pop()
    if(x < ssm):
        if(x < sm):
            ssm = sm
            sm = x
        else:
            ssm = x

    ret = None
    if(len(l) == 0):
        ret = ssm
    else:
        ret = second_smallest(l, sm, ssm)

    return ret


def sum_max_min(l, mx=-9999999999, mn=9999999999):
    l = l[:]
    x = l.pop()
    if(x > mx):
        mx = x
    if(x < mn):
        mn = x

    ret = None
    if(len(l) == 0):
        ret = mx + mn
    else:
        ret = sum_max_min(l, mx, mn)

    return ret
# remove elements from list and return until we arrive back at l?
