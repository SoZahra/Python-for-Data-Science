import matplotlib.pyplot as plt


def ft_invert(array):
    """ Inverts the color of the image received."""
    invert = array.copy()

    """  # comme toutes mes valeurs rgb sont = a 255,
    j'ai pas besoin de creer une variable pour chacun"""

    invert = 255 - invert
    plt.imshow(invert)
    plt.show()

    return invert


def ft_red(array):
    """
    Mettre le G et le B a 0 pour garder que le R
    """
    red = array.copy()

    red[:, :, 1] = 0 #vert
    red[:, :, 2] = 0 #bleu

    plt.imshow(red)
    plt.show()

    return red


def ft_green(array):
    """
    Mettre le R et le B a 0 pour garder que le G
    """
    green = array.copy()

    green[:, :, 0] = 0 #rouge
    green[:, :, 2] = 0 #bleu

    plt.imshow(green)
    plt.show()

    return green



def ft_blue(array):
    """
    Mettre le R et le G a 0 pour garder que le B
    """
    blue = array.copy()

    blue[:, :, 0] = 0 #rouge
    blue[:, :, 1] = 0 #vert

    plt.imshow(blue)
    plt.show()

    return blue



def ft_grey(array):
    """ tout mettre a 0"""
    if array is None:
        return None

    grey = array.copy()

    grey_value = (grey[:, :, 0] + grey[:, :, 1] + grey[:, :, 2]) /3

    grey[:, :, 0] = grey_value
    grey[:, :, 1] = grey_value
    grey[:, :, 2] = grey_value

    plt.imshow(grey)
    plt.show()

    return grey