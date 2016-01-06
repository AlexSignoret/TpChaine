# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> print(getNext('zzzzz'))
    'aaaaa'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1 Converti pwd en list
    found = False
    i=len(pwd)-1

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 Modifie le mot de passe
           found = True             
        else:
           if i > 0:
               pwd[i] = 'a' 
               i = i-1
           else:
               return 'Erreur incrément index liste  '+password
    
    return ''.join(pwd) #3 Retourne le nouveau mot de passe avec la lettre changée. 



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
