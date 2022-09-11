#Creating and Using a Class
class Dog:
    """A simple attemp to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simultate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

def main():
        my_dog = Dog("Willie", 6)
        print(f"my dog's name is {my_dog.name}.")
        print(f"my dog's is {my_dog.age}years old.")

        #call metods
        my_dog.sit()
        my_dog.roll_over()

        #creating multiples instances

        your_dog = Dog('lucy',3)
        print(f"\n Your dog's name is {your_dog.name} ")
        print(f"\n Your dog is {your_dog.age} years old.")
        your_dog.sit()
        your_dog.roll_over()

if __name__ == "__main__":
    main()
