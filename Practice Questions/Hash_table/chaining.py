class hash_table:
  def __init__(self):
    self.size = 10
    self.table = [[]for _ in range(self.size)]
    
  def hash_function(self,key):
    return hash(key) % self.size
  
  
  def insert(self,key,value):
    index = self.hash_function(key)
    
    self.table[index].append((key,value))
    
  def lookup(self,key):
    index = self.hash_function(key)
    
    for v,k in self.table[index]:
      if k == key:
        return v
    
    return None
  
  
    
    
    
    