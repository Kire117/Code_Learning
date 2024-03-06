mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}
print(type(otro_set))
print(len(mi_set))
print(4 in mi_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

otro_set.add(6)
print(otro_set)
otro_set.remove(1)
print(otro_set)
otro_set.pop()
print(otro_set)



