a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b) # contains all the elements in a along with all the elements in b
print(c)

d = a.intersection(b) # contains only the elemnts that are present in a as well as b
print(d)
e = a.difference(b)
print(e)

