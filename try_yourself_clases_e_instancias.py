class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name restaurant is : {self.restaurant_name}.")
        print(f"The cuisine_type is : {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("open restaurant")
    
    def number_Served(self,numer):
        self.number_served = numer
        print(f"number of customers actually is :  {self.number_served}.")

    def increment_number_served(self):
        self.number_served +=1
        print(f"a day of business: {self.number_served}.")

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0


    def describe_user(self):
        print(f"name user is {self.first_name}.")
        print(f"name user is {self.last_name}.")

    def greet_user(self):
        print(f"welcom user{self.first_name}")

    def increment_loging_attempts(self):
        self.login_attempts +=1
        print(f"{self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"{self.login_attempts}")



def main():

    my_restaurant=Restaurant("danielGurmet","COCINARAPIDA")
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

    restaurant_silvia =  Restaurant("silvia","fonda")
    restaurant_silvia.describe_restaurant()
    restaurant_silvia.open_restaurant()

    daniel = User("Daniel","Suarez")
    daniel.describe_user()
    daniel.greet_user()

    oscar = User("Daniel","Suarez")
    oscar.describe_user()
    oscar.greet_user()

    
    restaurant = Restaurant("daniel","fonda")
    restaurant.number_Served(7)
    restaurant.increment_number_served()
    
    user=User("daniel","fonda")
    user.increment_loging_attempts()
    user.reset_login_attempts()

if __name__ == "__main__":
    main()
    
        
