#remove function in set it will remove element from set. 
# The .remove(x) it will return none. 
# if element not exists in set it will raise keyerror
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.remove(5)
print(s)

print(s.remove(2))

s.remove(5)
print(f'it will raise error: {s}')



# it will also remove element form set
# discard
# if key not exist not raise error
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s.discard(5)
print(s)

s.discard(5)
print(f'not raise key error {s}')




