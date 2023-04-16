def read_input():
    while True:
        try:
            ievade = input("Enter 'i' for interactive input or 'f' for file input: ")
        except EOFError:
            return None, None

        if ievade == '':
            continue
        elif ievade == 'i':
            pattern = input("pattern?: ")
            text = input("text?: ")
            return pattern, text
        elif ievade == 'f':
            filename = input("file name?: ")
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
 
    pattern_hash = sum(ord(pattern[o])for o in range (pattern_length))
    text_hash = sum(ord(text[o])for o in range(pattern_length))
    if pattern_hash == text_hash and text[:pattern_length] == pattern:
        occurrences.append(0)

    for o in range(1, text_length - pattern_length +1):
        text_hash = text_hash  - ord(text[o -1]) + ord(text[o+pattern_length-1])
        if pattern_hash == text_hash and text[o:o+pattern_length]==pattern:
            occurrences.append(o)
           
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

