from recipe import Recipe
from book import Book

try:
    ingredients = ['ingrediente1', 'ingrediente2', 'ingrediente3']
    recipe = Recipe(name="Tarta de manzana", cooking_lvl=3, cooking_time=60, ingredients=ingredients, description='', recipe_type='postre')
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
else:
    print(recipe)

book = Book("test")
book.add_recipe("patata")
print(book.recipes_list["postre"][0])
print(book.name)
print(book.creation_date)
book.add_recipe(recipe)
print(book.last_update)
print(book.get_recipe_by_name("Tarta de manzana"))
print(book.get_recipes_by_types("postre"))