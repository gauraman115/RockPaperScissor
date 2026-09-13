#factorial
def find_factorial(n):

  if(n==0):
    return 1
  else:
    return n*find_factorial(n-1)

ans=find_factorial(6)
print(ans)

#calculate sum of first n natural numbers yusing recursion
def calculate_sum(n):
  if(n==0):
    return 0
  else:
    return n+calculate_sum(n-1)


answer=calculate_sum(5)
print(answer)