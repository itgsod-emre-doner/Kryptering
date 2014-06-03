def encrypt(cleartext, offset):
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')


    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
    cleartext = cleartext.upper()
    cleartext = list(cleartext)
    for letter in cleartext:
        print alphabet.index(letter)
    return ""