def cesar(s):
    k = ''
    for t in s:
        n = ord(t) - 65
        n += 3
        n %= 26
        n += 65
        k += chr(n)
    return k

print(cesar('Wasap'))