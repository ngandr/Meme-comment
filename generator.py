import random

comment = input('Enter comment: ')
temp = []
for letter in list(comment):
    cap = random.randint(0,1)
    if cap == 0:
        temp.append(letter.lower())
    elif cap == 1:
        temp.append(letter.upper())
        
newString = ''.join(temp)
print()
print(newString)
