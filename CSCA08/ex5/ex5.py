def function_names(file_to_read):

    list_to_return = []

    for line in file_to_read:
        if (line[:3] == 'def'):

            count = 0
            while (line[count+4] != '('):
                count +=1

            list_to_return += [line[4:count+4]]

    return list_to_return


def justified(file_to_read):
    
    file_line = file_to_read.readline()
    boolean = True

    while(file_line != '' and boolean == True):
        if(file_line[0] == ' '):
            boolean = False
            
        file_line = file_to_read.readline()

    return boolean

def section_average(file, section):
    None    

