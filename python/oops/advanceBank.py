class Bankaccont:
  def __init__(self,name,ac_no,balence):
    self.name=name
    self.ac_no=ac_no
    self.balence=balence

  def deposite(self,amount):
    self.balence+=amount
    print(f"you {amount} is deposite succesfully ")
  
  def withdraw(self,amount):
    if amount<=self.balence:
      self.belence-=amount
      print(f"you withdraw {amount} successfully")
    else:
      print("insufisient balence")

  

