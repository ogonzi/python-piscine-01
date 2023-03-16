from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = None
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {"entrante": [], "comida": [], "postre": []}
		self.set_name(name)
		
	
	def set_name(self, name):
		if isinstance(name, str) == False:
		    raise TypeError("Name should be a string")
		elif len(name) == 0:
		    raise ValueError("Name should not be empty")
		else:
		    self.name = name
	
	def set_last_update(self):
		self.last_update = datetime.now()
	
	def set_recipes_list(self, recipe):
		self.recipes_list[recipe.recipe_type].append(recipe) 
	
	def add_recipe(self, recipe):
		if isinstance(recipe, Recipe) == False:
			raise TypeError("Recipe should be of type Recipe") 
		else:
			self.set_recipes_list(recipe)
			self.set_last_update()
	
	def get_recipe_by_name(self, name):
		for recipes in self.recipes_list.values():
			for recipe in recipes:
				if recipe.name == name:
					return recipe
		return None
	
	def get_recipes_by_types(self, recipe_type):
		return self.recipes_list[recipe_type]
