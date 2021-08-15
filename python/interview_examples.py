#Palindrome
a = "test"
b = a[::-1]
print(b)

#remove ith char
a = "test"
b = ""
for i in range(len(a)):
    if(i!=1):
      b = b + a[i]
print(b)

#replace the 2nd occurence on a string
test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '
repl_dict = {'Gfg': 'It', 'Classes': 'They'}
lst_str = test_str.split(" ")
print(lst_str)
gfg_counter = 0
classes_counter = 0
out = []
for items in lst_str:
    if(items=="Gfg") :
        if(gfg_counter == 0):
            gfg_counter = gfg_counter + 1
            out.append(items)
        else:
            out.append(repl_dict['Gfg'])
    elif(items == "Classes") :
        if (classes_counter == 0):
            classes_counter = classes_counter + 1
            out.append(items)
        else:
            out.append(repl_dict['Classes'])
    else:
        out.append(items)

print(out)

#list of tuples sort using 2nd value
a = [(1,2),(2,0),(3,-3)]
a.sort(key= lambda x : x [1])
print(a)

#Fibonacci series
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if(nterms == 1):
    print(n1)
else:
    while count < nterms:
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1


#Dictionary examples
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}

res = {ele for i in test_dict.values() for ele in i}
print(res)

