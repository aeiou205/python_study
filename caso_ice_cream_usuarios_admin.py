from hashlib import new


class Restaurant:
    #cuando mandaremos valores desde un principioi para imprirmir se agreagan todos los parametros al inicio donde cargamos todas las variables
    def __init__(self):
        self.number_served = 0
        self.login_attempts = 0


    def read_number_served(self):
        print(f"the values number served is : {self.number_served}")
        
    def set_number_served(self,newNumberServed):
        self.number_served = newNumberServed
    
    def increment_number_served(self,incrementServed):
        print(incrementServed)
        self.number_served += incrementServed

    def decrement_number_served(self,decrementServed):
        self.number_served -= decrementServed

    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"El numero de incrementos es : {self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class iceCreamStand(Restaurant):
    
    def outputfavor():
        favors = 0
        print("",favors)







def main():
    my_new_restaurant = Restaurant()
    user = Restaurant()
    my_new_restaurant.read_number_served()#leer
    my_new_restaurant.set_number_served(20)
    my_new_restaurant.read_number_served()#leer
    my_new_restaurant.increment_number_served(50)
    my_new_restaurant.read_number_served()#leer
    my_new_restaurant.decrement_number_served(50)
    my_new_restaurant.read_number_served()#leer
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.reset_login_attempts()
    user.increment_login_attempts()


    ice = iceCreamStand ()


if __name__ == '__main__':
    main()
