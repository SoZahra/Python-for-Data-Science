import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter

def projection():
	graph_life = load("life_expectancy_years.csv")
	graph_gross = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

	if graph_life is None or graph_gross is None:
		print("Error: could not load data")
		return None


	life_1900 = graph_life['1900']
	gross_1900 = graph_gross['1900']

	plt.scatter(gross_1900, life_1900)

	plt.title("1900")
	plt.xlabel("Gross domestic product")
	plt.ylabel("Life Expectancy")

	# # plt.yticks([20, 25, 30, 35, 40, 45, 50, 55])
	# plt.ylim(0, 51)

	plt.xscale('log')
	plt.xlim(300, 10000)
	plt.xticks([300, 1000, 10000])

	def format_millions(value, pos):
		if(value >= 1000):
			return f'{int(value/1000)}k'
		else:
			return f'{int(value)}'

	plt.gca().xaxis.set_major_formatter(FuncFormatter(format_millions))

	plt.show()
	return life_1900, gross_1900

if __name__ == "__main__":
    projection()