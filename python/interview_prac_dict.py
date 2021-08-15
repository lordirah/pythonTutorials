#Unique values
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

test = []

for test1,values in test_dict.items():
    test.extend(values)
b = set(test)
print(type(b))
print(b)

#SUme of items in dictionary
test_dict = {'a':300 ,'b':60 ,'c':600}
sum_1 = 0

for items in test_dict.values():
    sum_1 = sum_1 +items

print(sum_1)

#Ways to remove keys from dict
test_dict = {'a':300 ,'b':60 ,'c':600}

del test_dict['a']
test_dict.pop('b')
print(test_dict)

#List of dictionay sort
lis = [{ "name" : "Nandini", "age" : 5}, { "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]
from operator import itemgetter

print(sorted(lis,key = itemgetter('age')))
print(sorted(lis, key=itemgetter('age', 'name')))
print(sorted(lis, key=itemgetter('age'),reverse = True))

#using lambda
print(sorted(lis, key = lambda x:x['age']))

test_dict = {'a':300 ,'c':60 ,'b':600}
print(sorted(test_dict, key = lambda x:x[0]))

#merging 2 dictionaries
dict1 = {'a': 10, 'b': 8 ,'e': 0}
dict2 = {'a': 20, 'b': 10,'d': 6, 'c': 4}
out = {}

a = set(dict1)
b = set(dict2)

c = a.union(b)

for items in c:
    if items in dict1 and items in dict2:
        out[items] = dict1[items] + dict2[items]
    elif items in dict1 and items not in dict2:
        out[items] = dict1[items]
    elif items not in dict1 and items in dict2:
        out[items] = dict2[items]
print(out)

#Flatten dictionary
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
a = dict(zip(test_dict['month'] , test_dict['name']))
print(a)

#Insersion at begining of ordered dict
from collections import OrderedDict
dict2 = OrderedDict([('a',20), ('b', 10),('d', 6), ('c', 4)])
dict2.update({'e':7})
dict2.move_to_end('e',last = False)
print(dict2)

#OrderedDict check order
# Function to check if string follows order of 
# characters defined by a pattern 
from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'
  
# Driver program 
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'egr'
    print (checkOrder(input,pattern)) 
    
    
#Election count
lst = ['harig','mani','peepin','prabha','harig','harig','mani','mani','a','a','a'] 
d = {} 
count = 0 
d1 = {} 
a = set(lst) 
for i in a:
    d[i] = lst.count(i) 
for key,value in d.items():
    if value == max(d.values()):
        d1[key] = len(key) 
print (min(d1, key=d1.get)) 

#having multiple keys
dict = {}
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z
a, b, c = 5, 2, 4
dict[a, b, c] = a + b - c
print(dict)

#find the kth non repeating string
a = "geeksforgeeks"
n = 3
from collections import OrderedDict

c = OrderedDict.fromkeys(a,0)
for ch in a:
    c[ch] += 1
print(c)
final = [k for k,v in c.items() if v == 1]
print(final)
if len(final) < n:
    print("no string")
else:
    print(final[n-1])

#binary representation of numbers
from collections import Counter
a = 8
b = 4
c = bin(a)[2:]
d = bin(b)[2:]
print(c,d)
zeros = abs(len(c)-len(d))
print(zeros)

if len(c) > len(d):
    d = zeros * '0' + d
else:
    c = zeros * '0' + c
print(c,d)

e = Counter(c)
f = Counter(d)
print(e,f)

if e == f:
    print("Same number of 0 and 1")
else:
    print("Not matching")
    
#Anagram counter
from collections import Counter
input = "ant magenta magnate tan gnamate"
input = input.split(" ")
print(input)
for i in range(0,len(input)):
     input[i]=''.join(sorted(input[i]))
print(input)
freqDict = Counter(input)

print (max(freqDict.values()))