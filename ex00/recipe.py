class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = None
		self.cooking_lvl = None
		self.cooking_time = None
		self.ingredients = None
		self.description = description
		self.recipe_type = None
		
		self.set_name(name)
		self.set_cooking_lvl(cooking_lvl)
		self.set_cooking_time(cooking_time)
		self.set_ingredients(ingredients)
		self.set_recipe_type(recipe_type)
	
	def __str__(self):
		return f"{self.name} ({self.recipe_type})\n\
            Difficulty: {self.cooking_lvl} / 5\n\
            Time: {self.cooking_time} min\n\
            Ingredients: {', '.join(self.ingredients)}\n\
            Description: {self.description}" 

	def set_name(self, name):
		if isinstance(name, str) == False:
			raise TypeError("Name should be a string")
		elif len(name) == 0:
			raise ValueError("Name can't be empty")
		else:
			self.name = name
	
	def set_cooking_lvl(self, cooking_lvl):
		if isinstance(cooking_lvl, int) == False:
			raise TypeError("Cooking level should be an int")
		elif cooking_lvl not in range(1, 6):
			raise ValueError("Cooking level should be in range 1 to 5")
		else:
			self.cooking_lvl = cooking_lvl
	
	def set_cooking_time(self, cooking_time):
		if isinstance(cooking_time, int) == False:
			raise TypeError("Cooking time should be an int")
		elif cooking_time < 0:
			raise ValueError("Cooking level should not be negative")
		else:
			self.cooking_time = cooking_time
	
	def set_ingredients(self, ingredients):
		if isinstance(ingredients, list) == False:
			raise TypeError("Ingredients should be a list")
		elif len(ingredients) == 0:
			raise ValueError("Ingredients list should not be empty")
		elif all(isinstance(ingredient, str) for ingredient in ingredients) == False:
			raise TypeError("Some ingredients in the list are not a string")
		else:
			self.ingredients = ingredients
	
	def set_recipe_type(self, recipe_type):
		valid_types = ["entrante", "comida", "postre"]
		if isinstance(recipe_type, str) == False:
			raise TypeError("Recipe type should be a string")
		elif len(recipe_type) == 0:
			raise ValueError("Recipe type can't be empty")
		elif recipe_type not in valid_types:
			raise ValueError(f"Recipe type should be one of {valid_types}")
		else:
			self.recipe_type = recipe_type
		