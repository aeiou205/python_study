from fileinput import filename
import json


#create json file 
def json1():
    print("hola")
    numbers = [2, 3, 5, 7, 11, 13]
    filename = 'numbers.json'
    with open(filename, 'w') as f:
        json.dump(numbers, f)


#show json file
def json2():
    filename = 'numbers.json'
    with open(filename) as f:
        numbers = json.load(f)
    print(numbers)

#saving and reading user_generated_data
def saving():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w')as f:
        json.dump(username,f)
        print(f"we'll remember you when come back, {username}!")


def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except:
        username = input("What is your name?")
        with open(filename,'w') as f:
            json.dump(username,f)
            print(f" well remember when you come back, {username}")
    else:
        print(f"Welcome back, {username}!")

def get_stored_username():

    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except:
        return None
    else:
        return username



def main():
    json1()
    json2()
    saving()
    greet_user()
    user=get_stored_username()
    print("hola",user)

if __name__ == '__main__':
    main()
