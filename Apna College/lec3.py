marks=[98.95,88,99]

print(marks)
print(type(marks))
print(marks[0])

#strings are immutable in python while list are mutable
str="hello"
# str[0]="v" #not allowed

marks[0]=51#mutable
print(marks)

#slicing also available in lists

print(marks[0:4])

list=[1,2,3,5]
list.append(4)
print(list)

list.sort()
print(list)

# for descending
print(list.sort(reverse=True))
print(list)

list.reverse()
print(list)

#insert method insert(index,element)
array=[11,12,13]
array.insert(1,15)
print(array)#11,15,12,13

#remove-remove first occirance of that element
array.remove(11)
print(array)
#pop-at particular index
array.pop(2)
print(array)

# ____________TUPLES_______
tup=(1,2,2,3,4)
print(tup)

#count- count num of occurancees
x=tup.count(2)
print(x) #ans =2

# if we want only one value in tuple then 
tup1=(1,)
print(tup1)

#WAP to check if list is pallindrome or not
list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("list 1 is pallindrome")
else:
    print("list1 is not pallindrome")

