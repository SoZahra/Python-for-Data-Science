import sys

def ft_filter(fonction, iterable):
    """ Creer une fonction qui a le meme principe que filter
        la fonction va prendre 2 paranetres, la premiere est la contrainte de filtre et la seconde sur quoi ont va filtrer
        Pour chaque element x dans iterable :
        On appelle fonction(x)
        Si ça retourne True → on garde x
        Si ça retourne False → on ignore x
    """
    return[x for x in iterable if fonction(x)]

def main():
    """ Ecrire un programme qui va prendre l'output(string)
   		et selon le nb donne (number) s'il est plus grand
   		que la string il va afficher sinon il affiche pas.
    """
    if len(sys.argv) != 3:
        print("AssertionError")
        return

    string = sys.argv[1]
    try:
        nb = int(sys.argv[2])
    except:
        print("AssertionError")
        return

    mot = string.split()
    res = ft_filter(lambda mot: len(mot) > nb, mot)
    print(res)


if __name__ == "__main__":
  main()