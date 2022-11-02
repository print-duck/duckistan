#############################
## id 391
## Puzzle Elo 1763
## Correctly solved 66 %
#############################

def encrypt(text):
    encrypted = map(lambda c: chr(ord(c) + 2), text)
    return ''.join(encrypted)


def decrypt(text):
    decrypted = map(lambda c: chr(ord(c) - 2), text)
    return ''.join(decrypted)


s = "xtherussiansarecomingx"
print(decrypt(encrypt(encrypt(s))) == encrypt(s))
