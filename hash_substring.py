# python3

def read_input():
    ievade = input("i vai f")

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    if ievade == 'i':
        pattern = input("pattern?: ")
        text = input("text?: ")
    elif ievade == 'f':
        filename = input("faila nosaukums?: ")
        with open(filename,'r')as g:
            pattern = g.readline().rstrip()
            text = g.readline().rstrip()
    else:
        raise ValueError("nepareiza ievade")
        return pattern, text
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    occurances = []
    sakums = 0
    while True:
        sakums = text.find(patters,sakums)
        if sakums == -1:
            break
        occurances.append(sakums)
        sakums +=1
        return occurances
    # and return an iterable variable
    #return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

