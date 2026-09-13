class Account:
   def __init__(self,bal,acc):
      self.amount=bal
      self.accountNum=acc
  
   def credit(self,amount):
      self.amount+=amount
      print("Rs:",amount,"credited to your account")
      self.get_Balance()

   def debit(self,amount):
      self.amount-=amount
      print("Rs:",amount,"debited from your account")
      self.get_Balance()
    
   def get_Balance(self):
      print("Available balanxe is Rs:",self.amount)

Account1=Account(10000,123)
Account1.credit(5000)
Account1.debit(2900)