def copy_me(il):
    ''' (list) -> list
        Takes a list and copies it but replaces
        nested lists with "List" and strings to uppercase.
        Integers and floats have their value +1
        booleans are negated

        >>>copy_me([4,"st",[5],False])
        [5,"ST","List",True]

        REQ: il != None
    '''

    input_list = il[:]

    for i in range(0, len(input_list)):
        if(type(input_list[i]) == str):
            input_list[i] = input_list[i].upper()

        if(type(input_list[i]) == bool):
            input_list[i] = not input_list[i]

        if(type(input_list[i]) == list):
            input_list[i] = "List"

        if(type(input_list[i]) == int or type(input_list[i]) == float):
            input_list[i] += 1

    return input_list


def mutate_me(input_list):
    ''' (list) -> None
        Takes a list and mutates it. Replaces
        nested lists with "List" and strings to
        uppercase. Integers and floats have their
        value +1 booleans are negated

        >>>li = [4,"st",[5],False]
        >>>mutate_me(li)
        >>>li
        [5,"ST","List",True]

        REQ: il != None
    '''

    for i in range(0, len(input_list)):
        if(type(input_list[i]) == str):
            input_list[i] = input_list[i].upper()

        if(type(input_list[i]) == bool):
            input_list[i] = not input_list[i]

        if(type(input_list[i]) == list):
            input_list[i] = "List"

        if(type(input_list[i]) == int or type(input_list[i]) == float):
            input_list[i] += 1
