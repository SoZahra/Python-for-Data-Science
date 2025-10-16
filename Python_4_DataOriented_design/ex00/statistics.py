
#*args permet de passer un nombre variable d’arguments à une fonction.
#Le * veut dire : “rassemble tout ce qui n’a pas été explicitement nommé dans une tuple”.


# **kwargs fonctionne de la même manière, mais pour les arguments nommés (les “keyword arguments”).
# Le ** veut dire : “rassemble tous les arguments nommés dans un dictionnaire”.

def ft_statistics(*args: any, **kwargs: any) -> None:

	if not args:#verifier si args n'est pas vide
		for _ in kwargs: #le faire pour chaque operateur
		# Le _ est une variable jetable qu'on utilise quand on n'a pas besoin de la valeur
		# Ça veut dire : "Je ne me soucie pas du nom de la cle, je veux juste boucler"
			print("ERROR")
		return

	# assert all(isinstance(x, int) for x in args), "Must be int" #all() return True si tout les elements sont vrais
	# print("c'est un int")
	for operator in kwargs.values(): #ca marche avec cle valeur, ce qui nous interesse c'est la valeur
		if operator == "mean":
			res = sum(args) / len(args)
			print(f"mean : {res}")
		elif operator == "median":
			sort_args = sorted(args)
			len_ = len(sort_args)
			if len_ % 2 == 0:
				res = (sort_args[len_//2-1] + sort_args[len_//2]) / 2
			else:
				res = sort_args[len_//2]
			print(f"median : {res}")
		elif operator == "quartile":
			sort_quartile = sorted(args) #trier si c'est pas deja fait
			len_ = len(sort_quartile) # prendre la taille de la liste

			# Prendre l'index arrondi
			q1 = float(sort_quartile[int(0.25 * (len_ - 1))])
			q3 = float(sort_quartile[int(0.75 * (len_ - 1))])

			print(f"quartile : [{q1}, {q3}]")
		# elif operator == "var": #mesure de dispersion des donnees autour de la moyenne
		# 	mean = sum(args) / len(args) #moyenne

		# 	somme_carres = 0
		# 	for x in args:
		# 		ecart = x - mean
		# 		somme_carres += ecart ** 2
		# 	n = len(args)
		# 	variance = somme_carres / (n - 1)
		# 	print(f"var : {variance}")
		elif operator == "var":
    # Étape 1 : Calculer la moyenne
			mean = sum(args) / len(args)

			# Étape 2 : Calculer la somme des carrés des écarts
			somme_carres = 0
			for x in args:
				ecart = x - mean
				somme_carres += ecart ** 2

			# Étape 3 : Diviser par n-1
			n = len(args)
			variance = somme_carres / (n - 1)

			print(f"var : {variance}")
		elif operator == "std":
			pass
