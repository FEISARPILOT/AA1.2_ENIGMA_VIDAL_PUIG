
from recursos import lletra_a_index
import extern, unicodedata

# Per xifrar o desxifrar el missatge del usuari, necessitarem invocar les 
# l'index de les possicions de les lletres introduïdes per l'usuari 
# + el TXT on es guarda el missatge en text pla del usuari
# + el TXT on es guarda el missatge xifrat,
# + el TXT de cada rotor on es guarda el cabljeat (1ra fila) 
#   i el seu notch (2na fila)
def processar_amb_rotors(pos1, pos2, pos3, xifrar: bool):
    #
    # Invoquem el nom dels fitxers ubicats al fitxer "extern.py"
    # Mencionem la CONSTANT que compté el nom del fitxer.
    
    if xifrar:
        # Xifrar (1)
        arxiu_entra_missatge = extern.GUARDAR_MISSATGE_INICIAL   # Missatge.txt
        arxiu_surt_missatge  = extern.GUARDAR_MISSATGE_XIFRAT    # Xifrat.txt
    else: 
        # Dexifrar (2)
        arxiu_entra_missatge = extern.GUARDAR_MISSATGE_XIFRAT    # Xifrat.txt
        arxiu_surt_missatge  = extern.GUARDAR_MISSATGE_DESXIFRAT # Desxifrat.txt
    
    pasar_missatge_rotors(
        pos1, pos2, pos3,
        arxiu_entra_missatge,
        arxiu_surt_missatge,
        #
        # Rotors
        extern.ROTOR1, 
        extern.ROTOR2, 
        extern.ROTOR3,
        xifrar=xifrar, # True = Xifrar, False = Desxifrar
        sortida_agrupar_en_cinc=xifrar # El missatge es separa en blocs de 5 lletres.
    ) 

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

#Funció per processar un missatge (xifrar o desxifrar) amb la lògica dels rotors.
def pasar_missatge_rotors(pos1, pos2, pos3,
                               arxiu_entra, arxiu_surt,
                               rotor1, rotor2, rotor3,
                               xifrar,
                               sortida_agrupar_en_cinc=False):
    
    # Carregar les permutacions i notchs dels rotors
    try:
        # perm = 1ra linea del rotor = Cablejat / permutació
        # notch = 2na linea del rotor = Posició clau
        # !!! No farem servir el 'notch3' al no haver un rotor Nº4, i així consecutivament.
        perm1, notch1 = carregar_rotor(rotor1) # rotor1.txt
        perm2, notch2 = carregar_rotor(rotor2) # rotor2.txt
        perm3, notch3 = carregar_rotor(rotor3) # rotor3.txt
    except:
        print(f"[ERROR] No s'ha pogut carregar un rotor")
        return
    
# Simplement extreure els valors deks arxius rotors, 
# es retorna la cadena perm i l'index notch.
def carregar_rotor(nom_arxiu):
    
    # Si falla open() abans d'executar-se, ens hem d'assegurar
    # que close() no s'executi sobre un fitxer mai obert.
    fitxer = None 
    try:
        fitxer = open(nom_arxiu, "rt") # Read (r) Text File (t)
        # Llegeix línea a línea el contingut de cada rotor (TXT) = readline()
        # treient espais d'esquerra a dreta = strip()
        # i convertint totes les seves lletres a majúscules.
        perm = fitxer.readline().strip().upper()  # 1ra linea = Cablejat (wiring)
        notch = fitxer.readline().strip().upper() # 2na linea = Notch (Posició clau)
    
    # Llancem excepcions específiques per a cada tipus d'error.
    except FileNotFoundError as FileError:
        print(f"[ERROR] No s'ha pogut trobar el fitxer a: {nom_arxiu}")
        print("L'arxiu 'Missatge.txt' (key-sensitive) ha d'estar al projecte.")
        print(f"[DEBUG] Detall de l'error: {FileError}")
        
    except PermissionError as ErrorPermission:   
        print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {nom_arxiu}")
        print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
      
    except Exception as e:   
        print(f"[ERROR] Error inesperat a l'hora de guardar el missatge a: {nom_arxiu}")
        print(f"[DEBUG] Detall de l'error: {e}")
        
    # Assegurem el tancament del fitxer només si el open() s'executa correctament,
    # i detectem el fitxer encara obert.
    finally:
        if fitxer is not None and not fitxer.closed:
            fitxer.close()
            
    # Retornem la permutació amb la possició númerica 
    # de la lletra del Notch de cada un dels 3 rotors 
    possicio_lletra_notch = lletra_a_index(notch)
    return perm, possicio_lletra_notch 
    