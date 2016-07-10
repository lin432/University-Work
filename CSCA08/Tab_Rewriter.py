def file_to_change(f):
    '''
    (str)->None
    writes a new file with all tabs replaced as
    4 spaces
    '''

    file_read = open(f,'r')
    
    string_array = file_read.readlines()

    for i in range(0,len(string_array)):
        process_string = string_array[i]
        process_string = process_string.strip("\n")
        string_write = ""
        index = 0
        num = 0
        while(index < len(process_string)):
            if(process_string[index:].find("\t") != -1):
                num +=1
            index += 1

        string_write = " " * (num*4) + process_string[(2*num) -(num*1):]

        print(string_write)

    
