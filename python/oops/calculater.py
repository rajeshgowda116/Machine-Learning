class calculater:
  def __init__(self):
    self.a=0
    self.b=0
    self.c=0
    self.operator="" 
  
  def Take_input(self):
    self.a=int(input("Enter a Frist Number:\n"))
    self.b=int(input("Enter a Second Number:\n"))
    self.operator=input("Enter your operator:\n")

  def Calulation(self):
    if self.operator=="+":
      self.c=self.a+self.b
    elif self.operator=="*":
      self.c=self.a*self.b
    elif self.operator=="/":
      if self.b==0:
        print("Zero Division Error")
      else:
        self.c=self.a/self.b
    elif self.operator=="-":
      self.c=self.a-self.b
    elif self.operator=="^":
      self.c=self.a**self.b
    return self.c
  
  def Display(self):
    while True:
      self.Take_input()
      self.Calulation()
      print("===================================================================================================================") 
      print("Result: ",self.a,self.operator,self.b,"=",self.c)
      print("===================================================================================================================")
    

calcu=calculater()
calcu.Display()

    
    