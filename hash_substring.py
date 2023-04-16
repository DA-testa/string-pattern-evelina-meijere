import os
def read_input():
    ievade, *input_values = input().rstrip().split()
    if ievade == 'I':
        if len(input_values) != 2:
            print("Error")
            return "",""
        pattern, text = input_values
    elif ievade == 'F':
        if len(input_values) != 1:
            print("Error")
            return "",""
        filename, = input_values
        if not os.path.exists(filename):
            print("Error")
            return "",""
        with open(filename) as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        print("Error")
        return "",""
    return pattern, text

def print_occurrences(occurrences):
    print(" ".join(str(i) for i in occurrences))
  
def get_occurrences():
    input_string = input().split('\r\n')
    if input_string[0] == 'I':
        string = input_string[1]
        substring = input_string[2]
        indices = []
        for i in range(len(string) - len(substring) + 1):
            if string[i:i+len(substring)] == substring:
                indices.append(i)
        if indices:
            print(' '.join(str(i) for i in indices))
        else:
            print('')
    elif input_string[0] == 'F':
        string = input_string[1]
        for i in range(len(string)):
            if string[i].isdigit() and int(string[i]) % 2 == 1:
                print(i**2, end=' ')
        print('')
if __name__ == '__main__':
    pattern, text = read_input()
    if pattern and text:
        get_occurrences()
