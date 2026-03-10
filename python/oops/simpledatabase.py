class Database:
  def __init__(self):
    self.__storage={}
  def write(self,key,value):
    self.storage[key]=value
  def read(self,key):
      if key not in self.storage:
        print("DB item not avalable")
      else:
       print(self.storage[key])

DB=Database()
DB.write("name","rajesh")
DB.write("age","20")
print(DB.__storage)
DB.read("name")