from sympy.solvers.diophantine import diophantine
from sympy import symbols
from string import ascii_lowercase
import math

#Big prime numbers
p = 11
q = 13

#Public key
n = p * q
phi = (p - 1) * (q - 1)

#Defining e
e = 2
while True:
    if e < phi and math.gcd(e, phi) == 1:
        break
    else:
        e += 1

#Solving diophantine equation to get k and d
k, d = symbols("k, d", integer = True)
diop = diophantine(phi*k + e*d - 1)
diop = str(diop).strip('{()}').replace("t_0", "0").split(', ')
k = eval(diop[1])
d = eval(diop[0])

#Reading the message to encrypt
f = open("user-input.txt", "r")
message = f.read()
message = message.rstrip()
f.close()

#Making the dictionary letters and respective numbers (a=10, b=11, ...)
group = {}
count = 10
for i in ascii_lowercase:
    group[i] = count
    count += 1
group[" "] = 99

#Pre-encrypting
numered = ''
blocks = []
for letter in message:
    numered = numered + str(group[letter])

#Dividing in blocks
index = 0
while index <= len(numered):
    try:
        if int(numered[index:index + 3]) < n and numered[index + 3] != '0':
            blocks.append(int(numered[index:index + 3]))
            index += 3
        elif numered[index + 2] != '0':
            blocks.append(int(numered[index:index + 2]))
            index += 2
        else:
            blocks.append(int(numered[index]))
            index += 1
    except IndexError:
        blocks.append(int(numered[index:]))
        break

#Encrypting using power and mod operations with each block element
coded = []
for block in blocks:
    coded.append(block**e % n)
print("Encrypted message:", coded)

#Decrypting using power and mod operations with each block element
daux = phi + d
decoded = []
for block in coded:
    decoded.append(block**daux % n)
print("Decrypted message:", decoded)
