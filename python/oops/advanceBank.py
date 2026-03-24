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
  def display(self):
      print("\n--- Account Details ---")
      print("Name:", self.name)
      print("Account No:", self.acc_no)
      print("Balance:", self.balence)
  
class SavingsAccount(Bankaccont):
  def add_interest(self):
    interest=self.balence*0.5
    self.balence+=interest
    print(f"Interest added: ₹{interest}")

class CurrentAccount(Bankaccont):
  def __init__(self,name, ac_no, balence):
    super().__init__(self,name,ac_no, balence)
    self.overdraptlimt=5000
  def withdraw(self,amount):
   if amount <= self.balence + self.overdraft_limit:
      self.balence -= amount
      print(f"₹{amount} withdrawn (Overdraft allowed).")
   else:
      print("Overdraft limit exceeded!")
  

