import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter

def aff_pop(path: str):
	graph = load(path)

	if graph is None:
		print("Error: could not load data")
		return None

	france = graph[graph['country'] == 'France']
	maroc = graph[graph['country'] == 'Morocco']

	if len(france) == 0 or len(maroc) == 0:
		print("Error: country not found")
		return None

	population_str = france.iloc[0,1:]
	population = population_str.str.replace('M', '').astype(float)
	year = graph.columns[1:].astype(int)

	population_str_maroc = maroc.iloc[0,1:]
	population_maroc = population_str_maroc.str.replace('M', '').astype(float)

	plt.figure(figsize=(10, 6))

	plt.plot(year, population)
	plt.plot(year, population_maroc)
	plt.title("Population Projections")
	plt.xlabel("Year")
	plt.ylabel("population")

	plt.xticks(range(1800, 2041, 40))
	# plt.xlim(1795, 2050)
	# Genere : 1800, 1840, 1880, ..., 2040, 2080
	# S'arrete a 2040 (car 2040 + 40 = 2080 > 2041)
	# il faut trouver une valeur qui est entre 2040 et 2080

	plt.yticks([20, 40, 60]) # on affiche seulement les graduations 20M, 40M, 60M
	plt.ylim(0, 70) # L'axe Y va de 0 en bas jusqu'a 70 en haut

	def format_millions(value, pos):
		return f'{value:.0f}M'

	plt.gca().yaxis.set_major_formatter(FuncFormatter(format_millions))

	plt.legend(["France", "Maroc"], loc="lower right")

	plt.tight_layout(pad=1.5)

	# plt.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.12)
	plt.subplots_adjust(left=0.40, right=0.85, top=0.85, bottom=0.40)  # ← Plus de marge !
	plt.show()

	return france, maroc


if __name__ == "__main__":
    aff_pop("population_total.csv")