# type: ignore
import numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]: 
    """Calculer l'IMC de deux personnes et retourner la list d'IMC"""
    if len(height) != len(weight):
        print("AssertionError: list is not the same size")
        return
    try:
        result = []
        for h, w in zip(height, weight):
            imc = w / (h ** 2)
            result.append(imc)
        return result
    except:
        print("AssertionError: not a int or a float")
        return
         
    
    
    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]: 
    """Prend une liste d'IMC et une limite (ex: 26 dans notre cas)
        Verifie pour chaque IMC : est-il superieur a la limite ?
        Return une liste de True/False"""
    result = []
    for x in bmi:
        if x > limit:
            result.append(True)
        else:
            result.append(False)
    return result
        

#return[x > limit for x in bmi] 
# for x in bmi → parcourt chaque élément de la liste bmi
# x > limit → compare chaque élément avec limit
# Résultat : True si x > limit, False sinon
    