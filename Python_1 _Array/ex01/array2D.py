
def slice_me(family: list, start: int, end: int) -> list:
    """ 
    Creer une fonction qui va prendre un tableau et trunquer dedans
    en fonction du start et du end donnes en parametres.
    """
    assert isinstance(family, list), "Family must be a list" 
    
    """ 
    Assert est une fonction qui va verifier la condition, 
    si elle est true elle continue si false elle va thru le msg 
    """
    
    assert len(family) > 0, "Family cannot be empty" 
    
    first_len = len(family[0]) #recup la taille de la premiere ligne, pour apres les comparer avec les autres
    for row in family:
        assert len(row) == first_len, "Family must have the same size"
    assert isinstance(start, int), "Family must be an int"
    assert isinstance(end, int), "Family must be an int"
    
    print(f"My shape is : ({len(family)}, {first_len})")
    
    new = family[start:end]
    print(f"My new shape is : ({len(new)}, {first_len})")
    return new