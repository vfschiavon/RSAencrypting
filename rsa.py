from string import ascii_lowercase
import math

p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = 103

if (math.gcd(e, phi) != 1) and (e < phi):
    print('coisa')
    exit()

f = open("user-input.txt", "r")
message = f.read()
message = message.rstrip()
f.close()

group = {}
count = 10
for i in ascii_lowercase:
    group[i] = count
    count += 1
group[" "] = 99

numered = ''
blocks = []

for letter in message:
    numered = numered + str(group[letter])
print(numered)

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
# i = 0
# for letter in message:
#     message = message.replace(message[i], str(group[letter]))
#     i += 1

print("BLOCKS: ",blocks)


#separar em blocos tal que cada bloco seja menor que n

#realizar as operações de encriptação10
MARCO