from load_image import ft_load2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def transpose(array):
    """ fonction pour effectuer une rotation sur une image"""
    hauteur, largeur = array.shape
    transposed = np.zeros((largeur, hauteur), dtype=array.dtype)
    
    for i in range(hauteur): #lignes
        for j in range(largeur): #colonnes
            transposed[j][i] = array[i][j]
    return transposed
    

def rotate(path: str) -> np.ndarray:
    img = ft_load2(path)
    img_2d = img.squeeze()
    
    transposed = transpose(img_2d)
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    
    plt.imshow(transposed, cmap='gray')
    plt.show()
    return transposed




if __name__ == "__main__": 
    rotate("animal.jpeg")