a = [['Mysore','Chamrajnagar'],['Erode','Trichy'],['Gobi','Erode'],\
     ['Bangalore','Mysore'],['Sathy','Gobi'], ['Chamrajnagar','Sathy']]


source = []
target = []
final = []


for items in a:
    source.append(items[0])
    target.append(items[1])    


src = [x for x in source if x not in target ]
starting = src[0]

tgt = [x for x in target if x not in source ]
ending = tgt[0]

for items in a:
    if starting in items:
        final.insert(0, items)
        a.remove(items)
    if ending in items:
        final.insert(1,items)
        a.remove(items)
        

array_counter = 1

while len(a) > 0:
    for items in a:
        if items[1] == final[len(final)-array_counter][0]:
            print("before")
            print(final)
            print(a)
            print(final[len(final)-array_counter][0])
            final.insert(len(final) -array_counter,items)
            a.remove(items)
            array_counter += 1
            print("after")
            print(final)
            print(a)
            


    


