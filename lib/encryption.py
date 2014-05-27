def encrypt(cleartext, offset):
    if len(cleartext) == 0:
        raise ValueError('can not encrypt empty string')
    if offset == 0:
        raise ValueError('offset must not be zero')


    return ""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
cleartext = raw_input('What do you want to encrypt?')
cleartext = cleartext.upper()
list(cleartext)
offset = raw.input('What is offset?')

