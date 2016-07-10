def greeting(p):
    '''
    (string) -> string
    returns a greeting having been given p as a name
    '''
    return "Hello " + p + " how are you today?"


def mutate_list(l):
    '''
    (list)-> None
    mutates list and changes integers by multiplying them by 2
    all booleans are inverted, strings have their first an last letters
    removed andthe first element of the list is made hello
    '''
    if(l != []):
        l[0] = "Hello"
        for a in range(1, len(l)):
            if(type(l[a]) == str):
                s = l[a]
                l[a] = s[1:len(s) - 1]
            if(type(l[a]) == int):
                l[a] = l[a] * 2
            if(type(l[a]) == bool):
                l[a] = not l[a]


def merge_dicts(d1, d2):
    '''
    ({str:list of ints},{str:list of ints}) -> {str:list of ints}
    takes a dict and if the key exists in the second dict then it
    appends the list of ints into a new dict
    '''
    new = {}
    for key in d1:
        new[key] = d1[key][:]

    curr = new.keys()
    for key in d2:
        if(key in curr):
            new[key] += d2[key][:]
        else:
            new[key] = d2[key][:]

    return new
