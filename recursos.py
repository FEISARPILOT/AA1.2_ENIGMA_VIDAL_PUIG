# lletra_a_index() = Cada rotor d'Enigma treballa amb possicions numèriques
#                    (indexos) del 0 al 25 (26 lletres en total).
#                    Aquest métode serveix per obtenir la possició númerica de la lletra del alfabet,
#                    i utilitzar la seva ubicació com a index númeric del array.
#
#                    Ex: A , B , C   ->  0 , 1 , 2
#                    Ex: Q , W , E   ->  16, 22, 4
#
#                    Si no executem aquest métode, l'index de cada lletra 
#                    s'assignaria pel seu ordre d'entrada.
#
#                    Ex: ERR: Ex: Q, W , E   ->  1, 2, 3
#
def lletra_a_index(lletra):
    
    # Obtindrem la possició númerica (int) de la lletra del alfabet convertint-la en format ASCII.
    # Per saber la seva possició, la restem amb la 'A' (65 en ASCII) al ser la 1ra lletra.
    
    # Ens asegurem que la lletra sempre sigui majúscula.
    # IMPORTANT! ASCII es key-sensitive (A != a) -> 'A' = 65, però 'a' = 97.
    codi_lletra = ord(lletra.upper()) 
    codi_A = ord('A')
    
    # Possició final de la lletra al alfabet (0-25)
    index = codi_lletra - codi_A
    return index

