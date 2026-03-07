class  Student:
  def __init__(self):
    self.name=""
    self.usn=''
    self.total=0
    self.subjects={}
    self.percentage=0
    self.subno=0
  
  def Details(self):
    self.name=input("Enter your name:\n")
    self.usn=input("Enter your usn:\n")
    self.subno=int(input("Enter how many subjects you have:\n"))
    for i in range(self.subno):
      sub=input(f"Enter your {i+1} subject name:\n")
      marks=int(input(f"Enter you marks on that subject:\n"))
      self.subjects[sub]=marks
    return self.subjects
  
  def Result(self):
    for i in self.subjects.values():
      self.total+=i
    self.percentage=self.total/self.subno
    return self.percentage
  
  def Display(self):
    self.Details()
    self.Result()
    print("===================================================================================================================")
    print("Name:",self.name)
    print("USN:",self.usn)
    for sub in self.subjects:
      print(sub, "Subject Marks:", self.subjects[sub])

    print("Total:", self.total)
    print("Percentage:", self.percentage)

    print("===================================================================================================================")

Result=Student()
Result.Display()