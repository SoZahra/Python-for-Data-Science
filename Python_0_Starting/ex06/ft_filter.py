import sys

def ft_filter(fonction, iterable):
    """ Creer une fonction qui a le meme principe que filter 
        la fonction va prendre 2 paranetres, la premiere est la contrainte de filtre et la seconde sur quoi ont va filtrer
        Pour chaque element x dans iterable :
        On appelle fonction(x)
        Si ça retourne True → on garde x
        Si ça retourne False → on ignore x
    """
    return[x for x in iterable if fonction(x)] #list comprehensions: facon compacte de creer des listes

# nombres = [1, 2, 3, 4, 5, 6]
# resultat = ft_filter(lambda x: x > 3, nombres)
# print(resultat)  # Devrait afficher [4, 5, 6]