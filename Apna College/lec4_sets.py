#set is a collection of unordered items
#each element in the set is unique and inmutable
#repeat elements stored only once
# numm_set=set()
collection={1,2,3,3,4,"Aman","Aman"}
print(collection)

#sets are mutable but element inside sets are not mutable means tuples can be paased inside sets but no list and dict

newSet=set()

newSet.add(1)
newSet.add(2)
newSet.add((1,2,3))
# newSet.add([1,2,3])#will throw error
newSet.remove(2)
print(newSet)

collection.clear()
print(collection)

#pop method- popping happend in random order means any element can be popped
newSet.pop()
print(newSet)
print(newSet)

# set1.union(set2)
#set1.intersection(set2)