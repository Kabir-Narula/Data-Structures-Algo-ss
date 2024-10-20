class Student:
  
  class_year = 2024   #class variables defined outside the constructor
  num_student = 0
  
  def __init__(self, name,age):
    self.name = name
    self.age = age
    Student.num_student += 1 # allows to access the total number of students created
    
student1 = Student("Kabir", 19)
student2 = Student("Arnav", 20)

print(student2.name)
print(student2.age)
print(student1.class_year)
print(Student.num_student)
    