def spellcheck(document, valid_words):
    document = document.lower()
    split_doc = document.split()
    set_valid = set(valid_words)

    new_words = set()
    for word in split_doc:
        if not (word in set_valid):
            new_words.add(word)
    return new_words
