#calculate avg of 4 numbers

def cal_avg(a,b,c,d):
  average=float((a+b+c+d)/4)
  return average

ans=cal_avg(1,2,3,4)
print(ans)

#WAP to print length of list as input
#WAF to print list in single line


names=["Aman","Shanti","Mansi"]

def cal_length(list):
  print(len(list))

cal_length(names)

for items in names:
  print(items,end=" ")

print(cal_length(names))

# WAF to convert usd to Inr
def convert_to_inr(amount):
  converted_amount=amount*95
  return converted_amount

amount=float(input("enter amount to convert into INR:"))

answer=convert_to_inr(amount)
print(answer)


 