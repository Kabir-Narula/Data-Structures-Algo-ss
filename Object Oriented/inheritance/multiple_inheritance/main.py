class Prey:
  def flee(self):
    print("This animal is fleeing")

class Predator:
  def hunt(self):
    print("This animal is hunting")
    
class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey,Predator):
  pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee() # CANNOT ACCESS HUNT
hawk.hunt() #CANNOT ACCESS FLEE
fish.hunt() # CAN ACCES BOTH
fish.flee()

  
  
    