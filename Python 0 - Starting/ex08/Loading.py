

def ft_tqdm(lst: range) -> None:
    """ Recreer la fonction tqdm, une barre de progression sur le terminal """
    total = len(lst)
    bar_length = 100
    
    for i, element in enumerate(lst):
        percent = (i + 1) / total * 100
        
        # Calculer combien de blocs remplis
        filled = int(bar_length * (i + 1) / total)
        
        # Creer la barre : █ pour rempli, ░ pour vide
        bar = '█' * filled + '░' * (bar_length - filled)
        
        # Afficher la progression
        print(f"{percent:.0f}%|{bar}| {i+1}/{total}", end="\r")
        yield element