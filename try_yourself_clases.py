class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name restaurant is : {self.restaurant_name}.")
        print(f"The cuisine_type is : {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("open restaurant")

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"name user is {self.first_name}.")
        print(f"name user is {self.last_name}.")

    def greet_user(self):
        print(f"welcom user{self.first_name}")


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


if __name__ == "__main__":
    main()
    
