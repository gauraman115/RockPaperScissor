class Student:
  
  #default contructor
  # def __init__(self):
  #   pass


  #parameterized constructor
  college="Jaypee Institute of Information Technology" #class attribute
  def __init__(self,name,age):
    self.name=name  #object attribute
    self.age=age
    print("calling constructor....")

  def welcome(self):  #these are called methods
    print("Welcome:", self.name)

  def get_age(self): #method
    return self.age
  
  @staticmethod
  def hello(): #static method dont use self inside them- we use decorator to use them
    print("hello Class")


s1=Student("Aman",24)  #object
print(s1.name,s1.age)
s2=Student("Mansi",24)
print(s2.name,s2.age) #different for everyone so s2.name
print(Student.college) #class attribute bcz class.college because this is same for all

s3=Student("Shanti",25)
s3.welcome()
print(s3.get_age())
s3.hello()


    