import matplotlib.pyplot as plt
from load_csv import load

def aff_life(path: str):
    graph = load(path)

    if graph is None:
        print("Error: could not load data")
        return None

    france = graph[graph['country'] == 'France'] #trie les colonnes pour ne prendre que France

    if len(france) == 0:
        print("Error: France not found")
        return None
    # toutes annees sauf la colonne country
    years = graph.columns[1:].astype(int)
    # graph.colums : va prendre toutes les colonnes [1:] a partie de l'index 1 donc sauf country
    life = france.iloc[0,1:].values
    #france.iloc il va prendre le fichier deja trie qui va prendre la ligne France,
    #[0,1:] 0 pour la premiere ligne, donc France, 1 pour prendre a partir de la 2eme colonne

    print(f"Années : {years[:5]}...")  # Affiche les 5 premieres
    print(f"Valeurs : {life[:5]}...")

    plt.plot(years, life)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")  # Label horizontal
    plt.ylabel("Life expectancy")  # Label vertical

    plt.xticks(range(1800, 2101, 40))
    plt.show()

    return france


if __name__ == "__main__":
    aff_life("life_expectancy_years.csv")