import sys
def read_input():
    while True:
        try:
            ievade = sys.stdin.readline().rstrip()
        except EOFError:
            return None, None

        if ievade == '':
            continue
        elif ievade == 'i':
            pattern = sys.stdin.readline().rstrip()
            text = sys.stdin.readline().rstrip()
            return pattern, text
        elif ievade == 'f':
            filename = sys.stdin.readline().rstrip()
            try:
                with open(filename,'r')as g:
                    pattern = g.readline().rstrip()
                    text = g.readline().rstrip()
                return pattern, text
            except IOError:
                print("Faila nav")
        else:
            print("Invalid input")
    

def print_occurrences(output):
    if not output:
        print("Nav")
        return
    if not isinstance(output,list):
        print("Nepareizs izvades tips")
        return

    occurrences = get_occurrences(output[0], output[1])
    if not occurrences:
        print("Nav")
    else:
        print(' '.join(map(str, occurrences)))

def get_occurrences(pattern, text):
    if pattern is None or text is None:
        return []
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
        # compute the hash value of the next substring using the rolling hash function
        text_hash = (text_hash - ord(text[i - 1]) * highest_pow) % sys.maxsize
        text_hash = (text_hash * PRIME + ord(text[i + pattern_length - 1])) % sys.maxsize

        if pattern_hash == text_hash and text[i:i+pattern_length]==pattern:
            occurrences.append(i)

           
    return occurrences
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

