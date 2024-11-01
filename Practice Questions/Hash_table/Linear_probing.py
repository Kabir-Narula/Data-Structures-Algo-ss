class Hash_table:
  def __init__(self):
    
    self.size = 10
    self.table = [None] * self.size # Created and empty table with no inserted data
    
  def hash_function(self,key):
    return hash(key)% self.size
  
  
  def insert(self,key,value):
    
    index =  self.hash_function(key)
    
    while self.table[index] is not None:
      index = (index+1) %self.size
      
    self.table[index] = (key,value)