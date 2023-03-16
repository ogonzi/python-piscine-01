class GotCharacter:
	def __init__(self, first_name, is_alive = True):
		self._first_name = first_name
		self._is_alive = is_alive

	@property
	def first_name(self):
		return self._first_name

	@property
	def is_alive(self):
		return self._is_alive

class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name, is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
	
	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		self._is_alive = False