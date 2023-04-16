

def read_input():
    ievade = input().strip()
    if ievade == "I":
        pattern = input().strip()
        text = input().strip()
    elif ievade == "F":
        with open("input.txt", "r")as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text

def print_occurrences(occurrences):
    print(" ".join(map(str, occurrences)))
  
def get_occurrences(pattern, text):
    t = 10**9+7
    return alg(pattern, text, t)


def alg(pattern,text,t):
    U,N,e,g,r,x,d,rez = len(pattern),len(text),256,t,pow(256,len(pattern)-1,t),0,0,[]
    for i in range(U):
        x = (x*e+ord(pattern[i]))%g
        d = (d*e+ord(text[i]))%g
    for i in range(N-U+1):
        if x == d and pattern == text[i:i+U]:
            rez.append(i)
        if i<N-U:
            d = (e(d-ord(text[i]), r)+ ord(text[i+U]))%g
        return rez
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))