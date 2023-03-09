def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    out = []

    # KSA
    for i in range(255):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = j = 0
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)

key = 'Key'
plaintext = 'Plaintext'

rc4(key,plaintext)