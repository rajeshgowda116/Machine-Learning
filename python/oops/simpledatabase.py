class Database:
  def __init__(self):
    self.__storage={}
  def write(self,key,value):
    self.__storage[key]=value
  def read(self,key):
      if key not in self.__storage:
        print("DB item not avalable")
      else:
       print(self.__storage[key])

DB=Database()
DB.write("name","rajesh")
DB.write("age","20")
print(DB._Database__storage)
DB.read("name")
