#Programa que cifra empleando RC4
#Antonio Roblero Alejandro Jesús
#Rojas Méndez Gabriel

import fileinput

lines = []
for line in fileinput.input(encoding="utf-8"):
    lines.append(line)

key = str.strip(lines[0])
plaintext = str.strip(lines[1])

S = 0
def KSA(key):
    global S
    S = [0] * 256
    for i in range(256):
        S[i] = i
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

i = 0 
j = 0 
def Encrypt(plain):
    global i
    global j
    encrypted = []
    for x in range(len(plain)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        encrypted.append(ord(plain[x]) ^ K)

    return encrypted

def imprimir(res):
    str = ""
    for i in res:
        str += "{0:02x}".format(i)
    return str.upper()

KSA(key)
print(imprimir(Encrypt(plaintext)))