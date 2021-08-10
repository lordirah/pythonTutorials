import time

def find_number_in_list(lst, number):
    if number in lst:
        return True
    else:
        return False

short_list = list(range(100))
long_list = list(range(10000000))

start = time.time()
find_number_in_list(short_list, 99)
end = time.time()
print(end - start)

start = time.time()
find_number_in_list(long_list, 9999999)
end = time.time()
print(end - start)

def find_number_in_dict(dct, number):
    if number in dct.keys():
        return True
    else:
        return False

short_dict = {x:x*5 for x in range(1,100)}
long_dict = {x:x*5 for x in range(1,10000000)}

start = time.time()
find_number_in_dict(short_dict, 99)
end = time.time()
print(end - start)

start = time.time()
find_number_in_dict(long_dict, 9999999)
end = time.time()
print(end - start)