

#THE CAR CLASS
from cgi import MiniFieldStorage


class Car:

    #INIT METOD
    def __init__(self, make,model,year):
        """inicializa los atributos"""
        self.make =  make
        self.model = model
        self.year = year
        """Setting a Default Value for an Attribute"""
        self.odometer_reading = 0

    #Descriptive car a car
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model} {self.model}"
        return long_name.title()

    #Read odometer of each car
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
       
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
       
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage      
        else:
            print("You can't roll back an odomoter")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles



def main():

    my_new_car = Car('AUDI','a4',2019)
    print(my_new_car.get_descriptive_name())

    """Modifying an Attribute’s Value Directly"""
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    my_new_car.update_odometer(50)
    my_new_car.read_odometer()
    my_new_car.update_odometer(70)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(20)
    my_new_car.read_odometer()


if __name__ == "__main__":
    main()
    
    
"""La seguridad efectiva requiere
atención extrema a los detalles además de controles básicos como los que se muestran aquí
"""
