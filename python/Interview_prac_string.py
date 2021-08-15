#Check string palindrome
a = 'tit'

if a == a[::-1]:
    print('palindrome')
else:
    print('not palindrome')
    
#Symetrical or palindrome
a='abaaba'

def palindrome(a):
    if a == a[::-1]:
        print('palindrome')
    else:
        print('not palindrome')

def symetrical(a):
    if len(a) % 2 == 0:
        pos = int(len(a)/2)
        b = a[0:pos]
        c = a[pos:len(a)]
        if b == c :
            print('symetrical')
        else:
            print('not symetrical')
    else:
        print('not symetrical')

palindrome(a)
symetrical(a)

#reverse words in given sentence
a = "i am so good here"
b = a.split(' ')
for items in b:
    print(items[::-1])

#remove char from a string
a = "test"
n = 3
b = ''
print(len(a))

for items in range(len(a)):
    if items == n-1:
        print('removed')
    else:
        b = b + str(a[items])
print(b)        

#Check if a substring is present in a string
a = "testing"
b = "z"

a.find(b)

#Sentence
a = "this is what is the thing this"
print(a.title())
b = a.split(' ')
c = set(b)
print(c)

#CAmelcase
a = 'this_test_test_lkiuj'
b = a.replace("_"," ").title().replace(" ","")
print(b)

#even length string
a = "this is a test linee"
b = a.split(' ')
for items in b:
    if len(items) % 2 == 0:
        print(items)

#
a = {'a':0,'e':0,'i':0,'o':0,'u':0}
b = list('aeioooooiiii')
count = 0
for k,v in a.items():
    for items in b:
        if k == items:
            a[k] = a[k] + 1
            
for k,v in a.items():
    if a[k] >= 1:
        count = count+1
print(count)

a = 'asdfeghjohhuI' 
b = 'a','e','i','o','u' 
print ('No' if len(set(b) - set(a.lower())) >= 1 else 'Yes') 

#Matching chars in pair of string
a = set('aabbccddeeff')
b = set('def')
print(a.intersection(b))

#frequency in str
a = 'testtessssssssab'
dict_a = {}

for items in a:
    if items not in dict_a:
        dict_a[items] = 1
    else:
        dict_a[items] = dict_a[items] + 1
        

new = dict(filter(lambda ele : ele[1] == 1, dict_a.items()))
print(new)

#remove a particular char in string
a = 'testonethe'
n =3
print(a[0:n-1])
print(a[n:len(a)])

#replace a char in string
a = 'test'
a.replace('t','x')

#check if a given str is binary
a='11100000'
c={'1','0'}
b=set(a)
print(b)

if len(b) == 2:
    if len(b.intersection(c)) == 2:
        print('binary')
    else:
        print('non binary')
else:
    print('not binary')


#Uncommon words between string

a = 'geeks for geeks end'
b = 'learning from geeks for geeks and geeks'
c = set(a.split(' '))
d = set(b.split(' '))

print(c.difference(d))
print(d.difference(c))

#Duplicate occurence in string
b = 'learning from geeks for geeks and geeks'
a = {'geeks':'test'}
d = []
c = b.split(' ')
counter = 0

for items in c:
    print(items)
    if items in a and counter == 0:
        d.append(items)
        counter = counter +1
        print(counter)
    elif items in a and counter != 0:
        d.append(a[items])
        counter = counter + 1
        print(counter)
    else:
        d.append(items)
print(' '.join(d))


#Permutation of given string
from itertools import permutations
a = permutations('abc')
print(a)
for perm in list(a):
    print (''.join(perm))

#execute a string of code    
a = 'print(\'hello\')'
exec(a)
    
#rotation string
a = 'test'
n=1
print(a[n:len(a)] + a[0:n])
print(a[-n:] + a[:-n])

#substr deletion
a = "GEEGEEKSKS" 
b = "GEEKS"
c =''
while len(a)>=len(b):
    c = a.replace(b,'')
    if (len(c) == len(a)):
        print('cant drill')
        break
    
    
    
    