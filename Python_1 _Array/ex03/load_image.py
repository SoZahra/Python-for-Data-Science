from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from zoom import ft_load


def ft_load2(path: str) -> np.ndarray:
    """ charger une  image et print ses infos : pixels en rgb  + display l'img apres zoom"""
    img = ft_load("animal.jpeg")
    print(img)
    start_y = 100
    start_x = 450
    
    new_img = img[start_y: start_y + 400, start_x: start_x + 400]
    gray = new_img[:, :, 0:1]

    print(f"New shape after slicing: {gray.shape} or {gray.squeeze().shape}")
    print(gray)
    
    plt.imshow(gray, cmap='gray')
    plt.show()
    
    return gray

if __name__ == "__main__": 
    ft_load2("animal.jpeg")