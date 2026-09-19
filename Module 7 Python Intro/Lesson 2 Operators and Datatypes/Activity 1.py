snack_name = "Dumplings"
price = 100.50
quantity = 25
is_available = True
preference = None

print(snack_name, type (snack_name)) # str = STRING

print(price, type(price)) # float = FLOATING POINT

print(quantity, type(quantity)) # int = INTEGER

print(is_available, type(is_available)) # bool = BOOLEAN

print(preference, type(preference)) # NoneType = NOTHING INSIDE/ NULL FROM JS


total = (100 - price) * quantity

average = (110 + 220 + 330) / 3

print(f"Total bill = {total}") #f - formatted string
print(f"Sale Price = {price - 10.75}")


# Comparison Operators
print("Is price below 2?", price < 2)
print("More than 5 in stock?", quantity > 5)

a = 20
b = 10

save = a # save will become 20
a = b # a will become 10
b = save # b will become 20

print(a, b)

x = 1.5 
y = 4.9

x, y = y, x

print(x, y)


word = "Banana"

print( len(word) )

print( word[0])
print( word[1])
print( word[2])
print( word[3])
print( word[4])
print( word[5])

print( word[-1])
print( word[-2])
print( word[-3])
print( word[-4])
print( word[-5])
print( word[-6])

# print( word[6]) #Index Error - String index is out of range.

print( word[0:2]) #The last number is not inclusive.