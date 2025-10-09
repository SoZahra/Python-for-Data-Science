from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray: #retourner un tableau NumPy (pas une liste Python classique).
    """ charger une  image et print ses infos : pixels en rgb """
    assert isinstance(path, str), "Path must be an string"
    assert path != "", "Path cannot be empty"
    
    try:
        img = Image.open(path)
        array = np.array(img)
        # print(f"The shape of image is: {array.shape}")
        # print(array)
        return array
        
    except FileNotFoundError:
        print("Error: file not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def ft_load2(path: str) -> np.ndarray:
    """ charger une  image et print ses infos : pixels en rgb  + display l'img apres zoom"""
    img = ft_load("animal.jpeg")
    # print(img)
    start_y = 100
    start_x = 450
    
    new_img = img[start_y: start_y + 400, start_x: start_x + 400]
    gray = new_img[:, :, 0:1]
    gray_new = new_img[:, :, 1]

    print(f"The shape of image is: {gray.shape} or {gray.squeeze().shape}")
    print(gray)
    
    # plt.imshow(gray, cmap='gray')
    # plt.show()
    
    return gray_new

