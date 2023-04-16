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
    print(" ".join(map(str, occurrences)))
  
def get_occurrences(pattern, text):
    occurrences = []
    p = 1000000007
    x = 263
    p_hash = hash(pattern, p, x)
    hashes = precompute_hashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != hashes[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

def hash(s, p, x):
    h = 0
    for t in reversed(s):
        h = (h * x + ord(t)) % p 
    return h   

def precompute_hashes(text, pattern_length, p, x):
    hashes = [0] * (len(text) - pattern_length + 1)
    s = text[len(text) - pattern_length:]
    hashes[len(text) - pattern_length] = hash(s, p, x)
    y = 1
    for i in range(pattern_length):
        y = (y * x) % p 
    for i in range(len(text) - pattern_length - 1, -1, -1):
        pre_hash = x * hashes[i+1] + ord(text[i]) - y * ord(text[i+pattern_length])
        hashes[i] = pre_hash % p
    return hashes

def find_substring(input_string):
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
        filename = input_string[1]
        with open(filename) as file:
            string = file.readline().rstrip()
            substring = file.readline().rstrip()
        indices = []
        for i in range(len(string) - len(substring) + 1):
            if string[i:i+len(substring)] == substring:
                indices.append(i)
        if indices:
            print(' '.join(str(i) for i in indices))
        else:
            print('')
    else:
        print('')

if __name__ == '__main__':
    pattern, text = read_input()
    if pattern and text:
        occurrences = get_occurrences(pattern, text)
        print_occurrences(occurrences)
    else:
        find_substring(input().rstrip().split())