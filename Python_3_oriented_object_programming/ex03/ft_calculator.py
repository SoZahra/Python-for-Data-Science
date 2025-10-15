class calculator:

	def __init__(self, vector):
		self.vector = vector

	def __add__(self, object) -> None:
		res = [] #res = [element + object for element in self.vector]
		for element in self.vector:
			res.append(element + object)
		print(res)

	def __mul__(self, object) -> None:
		res = [element * object for element in self.vector]
		print(res)

	def __sub__(self, object) -> None:
		res = [element - object for element in self.vector]
		print(res)

	def __truediv__(self, object) -> None:
		if object == 0:
			print("Error: Division by zero")
			return
		res = [element / object for element in self.vector]
		print(res)
