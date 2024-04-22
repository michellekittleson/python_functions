# Ingredient Preparation: Use slicing in lists to select specific segments of data. 
# You will be slicing a list to include only a specified portion of the ingredients
# needed for a recipe.

# Begin with a full list of ingredients.
# Use slicing to select the first half of the list.
# The length of the list can be found using the "len()" function, and you can divide it by 2 to find the midpoint.

ingredients = ["salt", "pepper", "paprika", "garlic", "onion", "beef", "tomato", "basil"]

needed_ingredients = ingredients[:len(ingredients)//2]

print(needed_ingredients)