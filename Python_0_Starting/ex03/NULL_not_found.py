
def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object}", type(object))
    elif object != object: #Not a number, il peut pas etre egale a lui meme, donc si un object n'est pas egale a lui meme alors c'est forvement un NaN
        print(f"Cheese: {object}", type(object))
    elif object is False:
        print(f"Fake: {object}", type(object))
    elif object == 0:
        print(f"Zero: {object}", type(object))
    elif object == '':
        print(f"Empty: {object}", type(object))
    else:
        print("Type not found ")
    return 1
