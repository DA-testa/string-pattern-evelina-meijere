# python3

def read_input():
    ievade = input("i vai f")
    if ievade == 'i':
        pattern = input("pattern?: ")
        text = input("text?: ")
        return pattern, text
    elif ievade == 'f':
        filename = input("faila nosaukums?: ")
        with open(filename,'r')as g:
            pattern = g.readline().rstrip()
            text = g.readline().rstrip()
        return pattern, text
    else:
        print("Nepareiza ievade tikai 'i' vai 'f'")
    

def print_occurrences(output):
  
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurances = []
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length > text_length:
        return occurances
 
    pattern_hash = sum(ord(pattern[o])for o in range (pattern_length))
    text_hash = sum(ord(text[o])for o in range(text_length))
    for o in range(text_length - pattern_length +1):
        if pattern_hash == text_hash and text[o:o+pattern_hash] == pattern:
            occurances.append(o)
        if o < text_length - pattern_length:
            text_hash = text_hash - ord(text[o]) + ord(text[i+p_len])
    return occurances


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

