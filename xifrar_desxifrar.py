import unicodedata


def netejar_missatge(text):
   
    text = text.upper() # Forcem text a majúscules
       
    # NFD (Normalization Form Canonical Decomposition)
    #     Permet descomposar una vocal o lletra 
    #     (NFC = Normalization Form Canonical Composition)
    #     per deixar-la completament neta. Ex: "Á" → "A" + "´"
    #     
    #     Aquesta llibreria ens ajuda a estalviar-nos els nostres diccionaris
    #     per reemplaçar una vocal amb accent, amb una vocal neta.
    text = unicodedata.normalize('NFD', text)
  
    resultat = []

    for caracter in text:
        
        # Un cop separat l'accent de la vocal,
        # el 'Mn' (Mark Nonspacing) ens ajudarà 
        # a esborrar l'accent de la vocal
        if unicodedata.category(caracter) == 'Mn':
            # Si es detecta un accent, deixa la vocal neta i continua
            continue
    
    # Recorre la String amb un 'for' només mantenint les lletres A-Z.
    # Creem una variable buida per afegir el resultat final
    for caracter in text:
        if 'A' <= caracter <= 'Z':
            # Afegeix la String final lletra a lletra
            resultat.append(caracter)
            
    # El missatge net, el convertim d'Array a String
    output_final = "".join(resultat)
    return output_final

