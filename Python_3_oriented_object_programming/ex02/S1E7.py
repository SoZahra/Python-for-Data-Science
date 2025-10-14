from S1E9 import Character

""" comment marche l'init avec super
C'est comme donner une commande a un restaurant :

Toi (Baratheon) : "Je veux un burger avec bacon et fromage"
Le cuisinier (Character) : "OK, je prépare avec ces ingrédients"

Le burger n'est prepare qu'une fois !
"""

class Baratheon(Character):
	"""Representing the Baratheon family."""

	def __init__(first_name, is_alive=True):
		"""Constructeur, il va servir a init nos attributs"""
		# Appeler le constructeur parent avec les valeurs Baratheon
		super().__init__( # super accede a la classe parent
			first_name=first_name,
			family_name="Baratheon",
			eyes="brown",
			hairs="dark",
			is_alive=is_alive
		)

	def die(self):
		self.is_alive = False

	def __str__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"



class Lannister(Character):
	"""Representing the Lannister family."""

	def __init__(self, first_name, is_alive=True):
		"""Constructeur, il va servir a init nos attributs"""
		# Appeler le constructeur parent avec les valeurs Baratheon
		super().__init__(
			first_name=first_name,
			family_name="Lannister",
			eyes="blue",
			hairs="light",
			is_alive=is_alive
		)

	def die(self):
		self.is_alive = False

	def __str__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	def __repr__(self):
		return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

	@classmethod #elle va creer un objet et le retourner
	def create_lannister(cls, first_name, is_alive=True):
		cal = cls(first_name, is_alive)
		return cal

	# Normalement : Lannister("Jaine", True)
	# Dans la methode de classe : cls("Jaine", True) ou cls(first_name, is_alive)

