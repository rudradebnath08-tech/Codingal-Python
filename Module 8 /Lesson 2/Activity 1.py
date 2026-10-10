pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 30, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

all_recipes = (pasta, biryani)
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe name:", all_recipes[1][2], "miss")
print("Pasta details sliced:", pasta[1:3])

print("\nPasta Recipe details:")
for detail in pasta:
    print("  -",detail)


pasta_ingredients = ["tomatoes", "garlic", "olive oil", "pasta", "chilli"]
biryani_ingredients = ["chicken", "rice", "spices", "tomato", "onions", "garlic"]

print("\nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total ingredients in Pasta:", len(pasta_ingredients))


pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated Pasta Ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll Ingredients (union):", all_ingredients)
print("Common Ingredients (intersection):", common)
print("Ingredients only in Pasta (difference):", only_pasta)
print("Not shared (sym. difference):", unique_to_each)