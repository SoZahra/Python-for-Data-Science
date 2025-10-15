
#*args permet de passer un nombre variable d’arguments à une fonction.
#Le * veut dire : “rassemble tout ce qui n’a pas été explicitement nommé dans une tuple”.


# **kwargs fonctionne de la même manière, mais pour les arguments nommés (les “keyword arguments”).
# Le ** veut dire : “rassemble tous les arguments nommés dans un dictionnaire”.

def ft_statistics(*args: any, **kwargs: any) -> None:
		assert args, "ERROR"
		assert all(isinstance(x, int) for x in args), "Must be int" #all() return True si tout les elements sont vrais
		print("c'est un int")