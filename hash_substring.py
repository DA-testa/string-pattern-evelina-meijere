

def read_input():
    ievade = input().strip()
    if "I" in ievade:
        pattern = input().strip()
        text = input().strip()
    elif "F" in ievade:
        cels = './tests/06'
        try:
            with open(cels, mode="r")as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
        except Exception as y:
            print("kluda:", str(y))
            return
    else:
        print("Error")
        return
    return pattern, text

def print_occurrences(output):
    print(" ".join(map(str, output)))
  
def get_occurrences(pattern, text):
 lengthp = len(pattern)
 lengtht=lne(text)
 hashp=hash(pattern)
 hasht=hash(text[:lengthp])
 occurrences = []
 for i in range(lengtht-lengthp + 1):
    if hasht == hashp and pattern==text[i:i+lengthp]:
        occurrences.append(i)
    if(i<lengtht-lengthp):
        hasht=hash(text[i+1: i+lengthp+1])
return occurrences
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))