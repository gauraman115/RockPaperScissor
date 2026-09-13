#range() functions return a seq of numbers starting from 0 by default and increment by 1 by default and stops at specified number
#range(start(optional-0 by default),stop,step()optional)
seq=range(5)

for i in seq:
  print(i)
print("\n")

#print all even numbers till 100
for j in range(2,100,2):
    print(j)  