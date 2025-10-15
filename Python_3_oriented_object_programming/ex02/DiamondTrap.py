from S1E7 import Baratheon, Lannister
from S1E9 import Character


class King(Baratheon, Lannister):

	def __init__(self, first_name, is_alive=True):
		Character.__init__(
			self,
			first_name=first_name,
			family_name="Baratheon",
			eyes="brown",
			hairs="dark",
			is_alive=is_alive
			)

	def get_eyes(self):
		return self.eyes

	def get_hairs(self):
		return self.hairs

	def set_eyes(self, value):
		self.eyes = value

	def set_hairs(self, value):
		self.hairs = value