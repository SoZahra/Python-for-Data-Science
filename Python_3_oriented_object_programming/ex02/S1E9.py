from abc import ABC, abstractmethod

#ABC une class qu'on ne peut pas instancier,
#elle va etre utiliser comme modele pour d'autres classes
class Character(ABC):
	"""class abstraite pour le personnage""" #self = object (l'instance)
	def __init__(self, first_name, family_name, eyes, hairs, is_alive=True): #__init__ constructeur
		"""Constructeur, il va servir a init nos attributs"""
		self.first_name = first_name #attribut
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs
		self.is_alive = is_alive

	@abstractmethod

	def die(self): #self = objet lui meme
		"""Method pour metre is_alive en False"""
		pass

