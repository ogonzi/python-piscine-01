class Vector:
	def __init__(self, values, shape = None):
		# Constructor for the Vector call
		# Takes a single argument values, which should be a list of lists representing a column vector or a row vector
		if isinstance(values, int) or isinstance(values, tuple):
			self.values = self.get_values(values)
		else:
			self.values = values
		if shape != None:
			self.shape = (shape[0], shape[1])
		else:
			self.shape = self.get_shape()
	
	def __str__(self):
		return (f"Vector({self.values})")
	
	def __repr__(self):
		return (f"Vector({self.values})")

	def __add__(self, other):
		# Defines the behavior of the + operator when applied to two vectors
		if isinstance(self, Vector) == False or isinstance(other, Vector) == False:
			raise TypeError("Vector can only be added to another vector")
		elif self.shape != other.shape:
			raise ValueError("Vectors must have the same shape")
		return Vector([[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(self.values, other.values)])
	
	def __sub__(self, other):
		# Defines the behavior of the - operator when applied to two vectors
		if isinstance(self, Vector) == False or isinstance(other, Vector) == False:
			raise TypeError("Vector can only be subtracted from another vector")
		elif self.shape != other.shape:
			raise ValueError("Vectors must have the same shape")
		return self + other.scalar_mul(-1)

	
	def __mul__(self, other):
		# Defines the behavior of the * operator when applied to two vectors or a vector and a scalar
		if isinstance(other, Vector):
			return self.dot(other)
		elif isinstance(other, (int, float)):
			return self.scalar_mul(other)
		else:
			raise TypeError("Vector can only be multiplied by a scalar or another vector")
	
	def __rmul__(self, other):
		return self.__mul__(other)

	
	def __truediv__(self, other):
		# Defines the behavior of the / operator when applied to two vectors or a vector and a scalar
		if isinstance(other, Vector):
			raise NotImplementedError("Division of a vector by a vector is not defined here")
		elif isinstance(other, (int, float)) and other != 0:
			return self.scalar_mul(1 / other)
		elif other == 0:
			raise ZeroDivisionError("Zero division error: division by zero")
		else:
			raise TypeError("Vector can only be divided by a scalar or another vector")
	
	def __rtruediv__(self, other):
		raise NotImplementedError("Division of a scalar by a Vector is not defined here")

	def dot(self, other):
		# Computes the dot product of two vectors
		# @dev:	zip essentially takes two or more iterables and pairs
		#		their elements together in tuples. Any combination of
		#		iterables can be zipped together, as long as they have
		#		the same length
		if self.shape != other.shape:
			raise ValueError("Vectors must have the same shape")
		elif self.shape[0] == 1:
			return sum([x * y for x, y in zip(self.values[0], other.values[0])])
		else:
			return sum([x * y for (x, ), (y, ) in zip(self.values, other.values)])

	def T(self):
		# Returns the transpose of the vector
		return Vector(self.values, (self.shape[1], self.shape[0]))

	def get_values(self, values):
		if isinstance(values, int):
			self.values = [[float(i)] for i in range(values)]
		elif isinstance(values, tuple):
			self.values = [[float(i)] for i in range(values[0], values[1])]
		return self.values
	
	def get_shape(self):
		# Returns the shape of the vector as a tuple (row, column)
		return (len(self.values), 1) if len(self.values[0]) == 1 else (1, len(self.values[0]))
	
	def scalar_mul(self, scalar):
		# Multiplies the vector by a scalar
		return Vector([[x * scalar for x in row] for row in self.values])