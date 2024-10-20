from car import Car
    
Car1 =  Car("Mustang",2024,"red", False)

Car2 = Car("BMW",2024,"green", True)

print (Car1.model)
print(Car1.year)
print(Car1.color)
print(Car1.for_sale)

print (Car2.model)
print(Car2.year)
print(Car2.color)
print(Car2.for_sale)

Car1.drive()
Car2.drive()
Car1.stop()
Car2.stop()


     