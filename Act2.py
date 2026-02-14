# create a class
class Vehicle:

    # create init method
    def __init__(self,max_speed,mileage):
        
        # blind the arguments
        self.max_speed= max_speed
        self.mileage= mileage

# object creation
modelX = Vehicle(240,18)

# acces variable inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:",modelX.mileage)
                                                                        