def decode1(word):
    return word.replace('A','o').lower()

def decode2(word):
    #if len(word) % 2 == 0:
    return word[::2]

def decode3(word):
    return word[:: -1]

def decode4(word):
    lenght = len(word)
    found = word[2 : lenght//2 + 2]

    return found
    #return word[2: -2]

def decode5(sentence):
    words = sentence.split()
    decoded = ""

    for i, word in enumerate(words):
        if i == 0:
            word = decode3(word)
        word = decode4(word)
        word = decode2(word)
        word = decode1(word)

        decoded += word + " "

    return decoded.strip()


'''
1.
MDEneEdU --> 8 / 2 weg begin == 4 weg op einde
oAXnkgaCteJE --> 12 / 4 weg begin == 3 weg op einde
2.
rAxNejhfTrns --> 12 / 3 weg begin== 4 weg op einde
'''