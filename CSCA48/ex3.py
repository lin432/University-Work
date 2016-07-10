from container import *


def banana_verify(source, goal, container, moves):
    '''
    (str, str, object, list of str) -> bool
    returns true if the sequence of moves results in the goal word

    examples:

    restrictions:
    '''
    result = ''
    index = 0

    for move in moves:

        if(move == 'P'):  # put word into container and move index 1 up
            container.put(source[index])
            index += 1

        elif(move == 'G'):  # retrieve from container, no affect on source
            if(not container.is_empty()):
                result += container.get()

        elif(move == 'M'):  # move current source word to result
            result += source[index]
            index += 1

    if(result == goal):
        result = True
    else:
        result = False
    return result
