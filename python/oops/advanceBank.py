class Bankaccont:
  def __init__(self,name,ac_no,balence):
    self.name=name
    self.ac_no=ac_no
    self.balence=balence
    
  def deposite(self,amount):
    self.balence+=amount
    print(f"you {amount} is deposite succesfully ")
  

