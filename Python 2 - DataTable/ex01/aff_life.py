import matplotlib.pyplot as plt
from load_csv import load

def aff_life(path: str):
    graph = load(path)
    
    # x = graph[graph['country']]
    # y = graph[graph['France']]
    if graph is None:
        print("Error: could not load data")
        return None

    france = graph[graph['country'] == 'France'] #row
    
    if len(france) == 0:
        print("Error: France not found")
        return None
    # toutes annees sauf la colonnes country
    years = graph.columns[1:].astype(int) 
    life = france.iloc[0,1:].values
    
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