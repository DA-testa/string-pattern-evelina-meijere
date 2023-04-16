import sys
PRIME = 101
def read_input():
    pattern = input().strip()
    text = input().strip()
    return pattern, text
    

def print_occurrences(occurrences):
    if occurrences:
        print(' '.join(map(str, occurrences)))
    else:
        return

    

def get_occurrences(pattern, text):
    occurrences = []
    if pattern is None or text is None:
        return occurrences
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
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)

    

