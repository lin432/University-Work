def rsum(l):
    l = l[:]
    if(len(l) == 0):
        return 0
    else:
        x = l.pop()
        if(type(x) == list):
            return rsum(x) + rsum(l)
        else:
            return x + rsum(l)


def rmax(l):
    ret = None

    if(len(l) != 0):
        l = l[:]
        x = l.pop()
        if(type(x) == list):
            x = rmax(x)

        y = rmax(l)
        if(y is not None and x is not None):
            if(x > y):
                ret = x
            else:
                ret = y
        else:
            if(y is None):
                ret = x
            else:
                ret = y

    return ret


# finish this up
def second_smallest(l):
    l = l[:]
    sm = None
    ssm = None
    (sm, ssm) = _smallest_pair(l)

    return ssm


def _smallest_pair(l):
    ret = None
    if(len(l) != 0):
        x = l.pop()

        sm = None
        ssm = None
        y = _smallest_pair(l)
        if(y is not None):
            (sm, ssm) = y
            sm2 = None
            ssm2 = None

            if(type(x) == list):
                x = x[:]
                x = _smallest_pair(x)
                if(x is not None):
                    (sm2, ssm2) = x
                else:
                    (sm2, ssm2) = (9999999, 99999999)
            else:
                (sm2, ssm2) = (x, x)

            if(sm2 < ssm):
                if(sm2 < sm):
                    ssm = sm
                    sm = sm2
                    if(ssm2 < ssm):
                        ssm = ssm2
                else:
                    ssm = sm2
            ret = (sm, ssm)

        else:
            if(type(x) == list):
                x = x[:]
                ret = _smallest_pair(x)
            else:
                ret = (x, 99999999)
    return ret


def sum_max_min(l):
    mx = None
    mn = None
    l = l[:]
    (mx, mn) = _max_min(l)
    return mx + mn


def _max_min(l):
    ret = None

    if(len(l) != 0):
        x = l.pop()

        mx = None
        mn = None

        y = _max_min(l)
        if(y is not None):
            (mx, mn) = y
            mx2 = None
            mn2 = None
            if(type(x) == list):
                x = x[:]
                x = _max_min(x)
                if(x is not None):
                    (mx2, mn2) = x
                else:
                    mx2 = -9999999999
                    mn2 = 99999999
            else:
                (mx2, mn2) = (x, x)
            if(mx2 > mx):
                mx = mx2
            if(mn2 < mn):
                mn = mn2
            ret = (mx, mn)

        else:
            if(type(x) == list):
                x = x[:]
                ret = _max_min(x)
            else:
                ret = (x, x)
    return ret
