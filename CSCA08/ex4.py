def insert(listA, listB, index):
    n = listA
    if(type(listA) != type(listB)):
        if(type(listB) == str):
            n = ''
            for a in range(0, len(listA)):
                n = n + str(listA[a])
        else:
            n = []
            for a in range(0, len(listA)):
                n = n + [listA[a]]

    return listB[:index] + n + listB[index:]

    #len_of_a = len(listA)
    #for a in range(0, len_of_a):
        #listB.insert(listA[len_of_a-a])
    #return listB


def up_to_first(l, o):
    n = None
    if(l.count(o) > 0):
        n = l.index(o)

    return l[:n]

    #list_copy = []
    #counter = 0
    #while(counter < len(l) or l[counter] != 0):
        #list_copy.insert(l[counter], counter)

    #return list_copy


def cut_list(l, i):
    if(type(l) == str):
        o = str(l[i])
    else:
        o = [l[i]]
    return l[(i+1):] + o + l[:i]
