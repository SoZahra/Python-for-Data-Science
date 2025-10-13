from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray: #retourner un tableau NumPy (pas une liste Python classique).
    """ charger une  image et print ses infos : pixels en rgb """
    assert isinstance(path, str), "Path must be an string"
    assert path != "", "Path cannot be empty"
    
    try:
        img = Image.open(path)
        array = np.array(img)
        print(f"The shape of image is: {array.shape}")
        print(array)
        return array
        
    except FileNotFoundError:
        print("Error: file not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None