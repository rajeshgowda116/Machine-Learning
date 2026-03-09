class Bank:
  def __init__(self):
    self.Balance=0
  def Deposite(self):
    Deposite=int(input("Enter Your Amount:\n"))
    self.Balance +=Deposite
    return self.Balance
  def Withdrawn(self):
    Withdrawn=int(input("Enter Your Amount:\n"))
    self.Balance -=Withdrawn
    return self.Balance
  def Display(self):
    while True:
      print("==================================================================================================================")
      print("                                         HI WELCOME FOR OUR BANK")
      print("==================================================================================================================")
      print( "                  1.Check Balance")
      print( "                  2.Deposite")
      print( "                  3.Withdrawn")
      choice=int(input("Enter Your Choice:\n"))
      if choice==1:
        print("Your Bank Balance is:",self.Balance)
      elif choice==2:
        self.Deposite()
        print("Your Bank Balance is:",self.Balance)
      elif choice==3:
        self.Withdrawn()
        print("Your Bank Balance is:",self.Balance)
      else:
        print("Invalid Choice")
B=Bank()
B.Display()
    



    

  
 