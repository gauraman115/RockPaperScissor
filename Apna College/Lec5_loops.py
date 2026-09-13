#Print multiplication table
x=int(input("Enter number:"))
i=1
while(i<=10):
    print(x*i)
    i+=1

#Print sqaures till 1,4,9,---,100
j=1
while(j<=10):
    print(j*j)
    j+=1

#print list
list=[1,2,3,4,5,6,7,8,9]
index=0

while(index<len(list)):
    print(list[index])
    index+=1
#print list using for loop

for nums in list:
    print(nums)
#search for number 7
iterator=0
for nums in list:
    if(nums==7):
        print("Found at index",iterator)
        break
    iterator+=1
