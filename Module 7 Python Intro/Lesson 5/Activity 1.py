def intro():
    print("Good evening everyone!")

intro()
intro()
intro()

# Name is an argument. (Data that I can pass to the function.)
def greeting(name, age, city):
    print(f"Good evening, I am {name} and I am {age} years old.")
    print(f"I live in {city}.")

name = "Rudra"
age = "18"
city = input("Where do you live? ")
greeting(name, age, city)



