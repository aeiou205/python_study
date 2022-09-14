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




def main():
    json1()
    json2()
    saving()

if __name__ == '__main__':
    main()
