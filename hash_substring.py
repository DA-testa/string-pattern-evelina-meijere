import sys
PRIME = 101
def read_input():
    while True:
        try:
            ievade = input().strip()
        except EOFError:
            return None, None

        if ievade == '':
            continue
        elif ievade == 'i':
            pattern = input().strip()
            text = input().strip()
            return pattern, text
        elif ievade == 'f':
            filename = input().strip()
            try:
                with open(filename,'r')as f:
                    pattern = f.readline().strip()
                    text = f.readline().strip()
                return pattern, text
            except IOError:
                print("Faila nav")
        else:
            print("Invalid input")
    

def print_occurrences(output):
    if occurrences:
        print(' '.join(map(str, occurrences)))
    else:
        print("Nav")

def get_occurrences(pattern, text):
    occurrences = []
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length > text_length:
        return occurrences
 
    pattern_hash = 0
    text_hash = 0
    highest_pow = 1
    for i in range(pattern_length):
        pattern_hash = (pattern_hash * PRIME + ord(pattern[i])) % sys.maxsize
        text_hash = (text_hash * PRIME + ord(text[i])) % sys.maxsize
        highest_pow = (highest_pow * PRIME) % sys.maxsize

    if pattern_hash == text_hash and text[:pattern_length] == pattern:
        occurrences.append(0)

    for i in range(1, text_length - pattern_length + 1):
        
        text_hash = (text_hash - ord(text[i - 1]) * highest_pow) % sys.maxsize
        text_hash = (text_hash * PRIME + ord(text[i + pattern_length - 1])) % sys.maxsize

        if pattern_hash == text_hash and text[i:i+pattern_length]==pattern:
            occurrences.append(i)

           
    return occurrences
if __name__ == '__main__':
    pattern, tex = read_input()
    occurrences = get_occurrences(pattern,text)
    print_occurrences(occurrences)

