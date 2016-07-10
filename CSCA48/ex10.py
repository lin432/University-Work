def radix_sort(l):
    '''(list of int) -> int
    Performs a radix sort on the list of integers
    returns a sorted list of int'''
    # creates a bin of ten lists
    main = [[],[],[],[],[],[],[],[],[],[]]
    max_val = 0
    ret = []

    # calculates the end point
    for item in l:
        ret += [item]
        # compares and rewrites
        if (item > max_val):
            max_val = item

    # converts to string to get max index
    str_val = str(max_val)
    end = 10 ** (len(str_val) - 1)

    ret = helper_radix_sort(ret, main, 1, end)
    return ret
        
def helper_radix_sort(l, main, digit, end):
    '''(list of int, list of list of int, int, int) -> list of int
    helper method for radix sort'''
    # fill main
    while(len(l) > 0):
        item = l.pop(0)
        # get digit
        index = get_digit(item, digit)
        # add to main list
        main[index] = main[index] + [item]

    # goes though 0-9
    for i in range(0, len(main)):
        process = main[i]
        # retrieves first in for all values
        for a in range(0, len(process)):
            l = l + [process.pop(0)]

    # checks for end case
    ret = l
    if(digit != end):
        ret = helper_radix_sort(ret, main, digit * 10, end)

    return ret

def get_digit(val, digit):
    '''(int, int) -> int
    gets the digit of the given integer'''
    val = int(val / digit)
    return val % 10
