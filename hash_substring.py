# python3

def read_input():
    ievade = input("i vai f")
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
    

 
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
   
    occurances = []
    sakums = 0
    while True:
        sakums = text.find(patters,sakums)
        if sakums == -1:
            break
        occurances.append(sakums)
        sakums +=1
        return occurances
 
    #return [0]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

