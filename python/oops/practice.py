class ATM:
  def __init__(self,balance=0):
    self.__balence=balance

  def check(self):
    print(self.__balence)
rbi=ATM(10000)
print(rbi.__balence)

