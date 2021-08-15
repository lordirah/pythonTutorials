#Max number in a list
a = [1,2,3,84,5,3,12]
print(max(a))

#COunt chars in a string
test_str = 'abcabcc'
test_dict = {}
for items in test_str:
    if items not in test_dict:
        test_dict[items] = 0
    else:
        test_dict[items] = test_dict[items] + 1
        
print(test_dict[max(test_dict)])

#Merge dictionary
a = {'a' : 10 , 'b' : 20 , 'c' : 30}
b = {'a' : 10 , 'b' : 20 , 'd' : 30, 'e' : 60}
c = {}

for k,v in a.items():
    for k1,v1 in b.items():
        if k == k1:
            print(k)
            c[k] = a[k] + b [k]
            print(c)
        else:
            c[k1] = b[k1]
            c[k] = a[k]
print(c)

#Armstrong number
a = '153'
b = []
sum1 = 1
total = 0

for items in a:
    for itesm_1 in range(len(a)):
        sum1 = sum1 * int(items)
    b.append(sum1)
    sum1 = 1
print(b)

for items in b:
    total = total + items
print(total)

if(total == int(a)):
    print("Armstrong")
else:
    print("non armstrong")
    
#Prime number in an interval
a = 3
b = 50

for items in range(a,b):
    for items_1 in range(2,items):
        if items%items_1 == 0 :
            break
        else:
            print(items)
            
#Fibonacci series
n,n1,n2 = 3,0,1
count = 0

if n == 1:
    print(n1)
else:
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1

###List examples
#Sum of array
a = [1,3,4,5,7,8,9]
total = 0
for items in a:
    total = total + items
print(total)

#Largest element in array
a = [1,3,4,5,7,8,9]
print(max(a))

#Array rotation
a = [1,3,4,5,7,8,9]
b = []
n = 2
for items in range(n):
    b.append(a[0])
    a.pop(0)
    print(a)
print(b)
for items in b:
    a.append(items)
print(a)

#Multiply array and divide by given number
a = [1,3,4,5,7,8,9]
mul = 1
n = 9
for items in a:
    mul = mul * items
final = mul / n
print(final)

#Monotonic increasing or decreasing
a = [1,3,4,5,7,8,9]
b = []
prev_item = 0
for items in range(len(a)):
    if items == 0:
        prev_item = a[0]
        #print(prev_item)
    else:
        print(prev_item , a[items])
        if a[items] < prev_item:
            print("lesser")
            b.append("lesser")
        else:
            print("greater")
            b.append("greater")
        prev_item = a[items]
            
len_set = len(set(b))

if len_set == 1:
    print("monotonic")
else:
    print("non monotonic")

#Interchange 1st and last element in a list
a = [1,3,4,5,7,8,9]
first_element = a[0]
last_element = a[len(a)-1]    
print(first_element, last_element)
a.pop(0)
a.pop(len(a)-1)
a.append(first_element)
a.insert(0,last_element)
print(a)

#Interchange given position
a = [1,3,4,5,7,8,9]
pos1,pos2 = 1,6

#reversing
a = [1,3,4,5,7,8,9]
print(a[2:4])
print(a[::-1])

x = 'computer'
print(x[1:4])
print(x[1:6:1])

#2nd largest number
a = [100,1,3,4,5,7,8,9]
a.sort()
print(a[len(a)-2])

print(a[-2:])

#Remove empty list from a list
a = [100,1,3,4,5,7,8,9,[],[1]]

for items in a:
    if type(items) is list:
        if len(items) == 0:
            a.remove(items)
print(a)

#Cloning a list
a = [100,1,3,4,5,7,8,9]
b = []

b = list(a)
print(b)

#Remove empty tuples from list
a = [100,1,3,4,5,7,8,9,(),(1,)]

for items in a:
    if type(items) is tuple:
        if len(items) == 0:
            a.remove(items)
print(a)

#Occurence of element in a list
a = [100,100,5,1,2,4,5,7,7,7,7]
b = set(a)
c = {}

for items in b:
    for items_1 in a:
        if items == items_1:
            if items not in c:
                c[items] = 1
            else:
                c[items] = c[items] + 1
print(c)

#DUPLICATES alone print from above dict
sorted(c.items(),key = lambda x:x[1])

#cumulative sum
a= [10,20,30,40,50]
b = []
total = 0

for items in a:
    total = total + items
    b.append(total)
print(b)

#sum of no of digits in list
a= [10,20,30,40,50,99,76]
b = []
total = 0

for items in a:
    for items_1 in str(items):
        total = total + int(items_1)
    print(total)
    total = 0

#Break list into chunks of n
a = [10,20,30,40,50,99,76]
n = 3
c = len(a)-1
test = 0

while test < c:
    b = a[0:n]
    print(b)
    for i in range(n):
        a.pop(0)
    print(a)
    c = c -n
