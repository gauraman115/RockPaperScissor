str1="Aman"
str2="Gaur"
name=str1+" "+str2
print(name)
print(len(name))


print(name[2])

print(name[0:4]) #Aman
print(name[5:9]) #Gaur
print(name[5:len(name)]) #Gaur
print(name[5:])  #Gaur
print(name[:4])#Aman

#negative indexing
print(name[-9:-4]) #aman is -4,-3,-2,-1


#if-elif-else

age=82

if(age>=18):
        if(age>=80):
            print("can vote but can not drive")
        else:
            print("you can vote and drive")
else:
    print("can not vote and drive")

#check num is multiple or 7 or not

num=float(input("enter a number:"))

is_multiple=num%7

if(is_multiple==0):
    print("number is a multiple of 7")
else:
     print("number is not  a multiple of 7")