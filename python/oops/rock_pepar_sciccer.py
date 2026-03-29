import random
class Rock_Pepar_Sciccer:
  def __init__(self):
    self.list=['rock','pepar','sciccer']
    self.result=random.choice(self.list)
  def Rock(self):
    if self.result=='rock':
      print(f"You chosed rock and computer choose {self.result}. Tie")
    elif self.result=='sciccer':
      print(f"You chosed rock and computer choose {self.result}. You win")
    elif self.result=='pepar':
      print(f"You chosed rock and computer choose {self.result}. you lose")

  def paper(self):
    if self.result=='rock':
      print(f"You chosed pepar and computer choose {self.result}. You win")
    elif self.result=='pepar':
      print(f"You chosed pepar and computer choose {self.result}. Tie")
    elif self.result=='sciccer':
      print(f"You chosed pepar and computer choose {self.result}. You lose")

  def sciccer(self):
    if self.result=='rock':
      print(f"You chosed sciccer and computer choose {self.result}. you lose")
    elif self.result=='pepar':
      print(f"You chosed sciccer and computer choose {self.result}. you win")
    elif self.result=='sciccer':
      print(f"You chosed sciccer and computer choose {self.result}. Tie")

  def Play(self):
    while True:
      print("*************Rock pepar Sciccer game**************")
      print("1.rock")
      print('2.pepar')
      print('3.sciccer')
      print('4.Exit the game')
      choice=int(input("Enter Your Choice\n"))
      if choice==1:
        self.Rock()
      elif choice==2:
        self.paper()
      elif choice==3:
        self.sciccer()
      elif choice==4:
        break
      else:
        print("Inavalid choice try again\n")

game=Rock_Pepar_Sciccer()
game.Play()

      
      