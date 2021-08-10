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