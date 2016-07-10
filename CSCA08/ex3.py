def percent_to_gpv(a):
    '''(int)->float
    Turns percent point to gpv
    >>> percent_to_gpv(100)
    4.0
    >>> percent_to_gpv(40)
    0
    REQ: a > 0.0
    '''

    if (a >= 85):
        return 4.0
    elif(a >= 80):
        return 3.7
    elif(a >= 77):
        return 3.3
    elif(a >= 73):
        return 3.0
    elif(a >= 70):
        return 2.7
    elif(a >= 67):
        return 2.3
    elif(a >= 63):
        return 2.0
    elif(a >= 60):
        return 1.7
    elif(a >= 57):
        return 1.3
    elif(a >= 53):
        return 1.0
    elif(a >= 50):
        return 0.7
    else:
        return 0.0

def card_namer(num,suit):
    n = [["A","Ace"],[2,"2"],[3,"3"],[4,"4"],[5,"5"],[6,"6"],[7,"7"],[8,"8"],[9,"9"],["T","10"],["J","Jack"],["Q","Queen"],["K","King"]]
    s = [["D","Diamonds"],["C","Clubs"],["H","Hearts"],["S","Spades"]]
    Number = None
    Suit = None


    for a in range(0,len(n)):
        if(str(n[a][0]) == str(num)):
            Number = a
            break

    for a in range(0,len(s)):
        if(str(s[a][0]) == str(suit)):
            Suit = a
            break

    if(Number == None or Suit == None):
        return "CHEATER!"

    
    return ''+ n[Number][1] + ' of ' + s[Suit][1]


def my_str(a):
    '''
    (object) -> str

    return object in string form based on its type

    '''

    if (type(a) == str):
        return a

    if (type(a) == bool):
        if(a):
            return 'YES'
        else:
            return 'NO'

    if (type(a) == int):
        if (a > 99):
            return 'Large Number'
        elif (a > 10):
            return 'Medium Number'
        else:
            return 'Small Number'

    if (type(a) == float):
        return str(round(a,2))

    return 'I dunno'
    

    

    
    
