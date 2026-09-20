city = input("Enter your city: ")
temperature = float(input("Enter the temperature in your city: "))

if temperature > 35:
    print("WARNING: It is a very hot day today!")

if temperature > 25:
    print("Great day to go outside!")
else: 
    print("Grab a jacket before you go out!")


if temperature > 35:
    print("Weather: Scorching Heat")
elif temperature > 25:
    print("Weather: Warm and Sunny")
elif temperature > 15:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold - stay warm!")


if city == "Delhi":
    print("You live in Delhi NCR")
elif city == "Dombivali":
    print("You live in Maharashtra")
elif city == "Lagos":
    print("You live in Lagos")
elif city == "Abuja":
    print("You live in FCT")

# Adding else is not mandatory!!!!!

import datetime

now = datetime.datetime.now()
print(now)