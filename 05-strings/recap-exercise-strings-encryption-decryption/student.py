def decode1(word):
    has_A = word.find('A')

    if has_A != -1:
        #word[has_A] = 'o'
        new_word = word[: has_A] + 'o' + word[has_A + 1:]
        return decode1(new_word)
    
    # returne word.replace('A','o')
    return word

def decode2(word):
    #if len(word) % 2 == 0:
    new_word = word[::2]
    return new_word

def decode3(word):
    has_space = word.find(' ')

    if has_space != -1:
        rev_word = word[has_space -1: :-1] 
        rest = word[has_space:]
        return rev_word + rest
    
    return word

def decode4(word):
    lenght = len(word)
    found = word[2 : lenght//2 + 2]

    return found