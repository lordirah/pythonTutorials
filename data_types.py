#List
#-General purpose
#-Grow and shrink as required
#-Sequence type
#-Sortable

#indexing
x = ['a','b','c']
print(x[1])

#slicing
#\[start:end+1:step\]
x = 'computer'
print(x[1:4])
print(x[1:2:3])
print(x[1:])
print(x[:5])
print(x[-1])

#Iterating
x = ['a','b','c']
for items in x:
    print(items)

for index,items in enumerate(x):
    print(index,items)

#Sorting
x = ['pig','horse','cow']
print(sorted(x)) #Creates new list
print(x)

x = ['pig','horse','cow']
x.sort()
print(x)

#Count of item
print(x.count('pig'))

#declaring different ways
x = list()
x = ['a','4','5.6','sbh']
#x = list(tuple)

#List comprehensions
x =[m for m in range(8)]
print(x)

x = [m*m for m in range(8) if m > 4]
print(x)

#delete item in index
x = ['a','4','5.6','sbh']
del(x[1])
del(x)

#Extending a list with other
x = ['a','4','5.6','sbh']
y = ['pig','horse','cow']
x.extend(y)
print(x)

#List.pop
y = ['pig','horse','cow']
y.pop(0)
print(y)

#list.remove it removes oly the instance of the item

#Tuples
#-All operation of the list can be performed on tuple
#-Immutable but the members of the list can be changed
#-Tuples are fast compared to list coz of python implementation

#declaration
x = ()
x = (1,2,3)
x = 1,2,3
x = 1,
x = tuple(y)

#immutable
x = (1,2,3)
del(x[1])