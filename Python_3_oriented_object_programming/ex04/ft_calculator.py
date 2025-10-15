class calculator:
#le but ici est de ne pas instancier la class,donc on ne peut pas creer de d'objet a partir de cette class
# dans le sujet : utiliser les methodes de la classe sans avoir à instancier la classe (calculator).
	def decorator(func):
		def wrapper(*args, **kwargs):
			print("start")
			res = func(*args, **kwargs)
			print("end")
			return res
		return wrapper

	# @decorator
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		res = 0
		for element1, element2 in zip(V1, V2):
			res += element1 * element2
		print(f"Dot product is : {res}")

	# @decorator
	def add_vec(V1: list[float], V2: list[float]) -> None:
		res = []
		for element1, element2 in zip(V1, V2):
			add = float(element1) + float(element2)
			res.append(add)
		print("Add Vector is :", res)

	# @decorator
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		res = []
		for element1, element2 in zip(V1, V2):
			sous = float(element1) - float(element2)
			res.append(sous)
		print("Sous Vector is :", res)

