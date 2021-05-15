# importing 
import random

# Selecting charecter
charecters = ['#', '@', '$', '&', '*', '!', '(',')', '-', '+', '=', ',', '.', '%', '^',':', ';', '~']
numbers = [0,1,2,3,4,5,6,7,8,9]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_jack = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X' 'Y', 'Z']

# Chosing random charecter
a = random.choice(charecters)
b = random.choice(numbers)
c = random.choice(letters)
d = random.choice(letters_jack)
e = random.choice(charecters)
f = random.choice(numbers)
g = random.choice(letters)
h = random.choice(letters_jack)
i = random.choice(charecters)
j = random.choice(numbers)
k = random.choice(letters)
l = random.choice(letters_jack)
m = random.choice(charecters)
n = random.choice(numbers)
o = random.choice(letters)
p = random.choice(letters_jack)
q = random.choice(charecters)
r = random.choice(numbers)
s = random.choice(letters)
t = random.choice(letters_jack)
# Making an array of those random charecter
allinone = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]

# loop to print a 16 digit password
i = 0
i_end  = input('How many charecters do you want? ')

while i != int(i_end):
    print(random.choice(allinone), end='')
    i = i + 1
