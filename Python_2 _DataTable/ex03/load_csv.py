import pandas as pd


def load(path: str):
	"""
	Ecrire kes dimensions d'un fichier data et le return.
	NumPy = pour les tableaux numériques (images, matrices)
	Pandas = pour les tableaux de donnees (personnes, statistiques, bases de données)
	On va utiliser Pandas, c'est comme avoir un excel en python
	"""
	assert isinstance(path, str), "Path must be an string"
	assert path != "", "Path cannot be empty"

	try:
		data = pd.read_csv(path)

		print(f"Loading dataset of dimensions{data.shape}")
		return data

	except FileNotFoundError:
		print("Error: file not found")
		return None
	except Exception as e:
		print(f"Error: {e}")
		return None

