
from recursos import lletra_a_index, index_a_lletra
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

# Simplement extreure els valors deks arxius rotors, es retorna la cadena perm i l'index notch degut a que es simplefica la comparacio en avança_motors funció
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
            
    # El missatge net, el convertim d'Array a Strin
    output_final = "".join(resultat)
    return output_final

# Retorna la permutació inversa d'un rotor
def inversa_permutacio(perm):
    
    """
    Donada una permutació 'perm' (string de 26 lletres),
    retorna la permutació inversa com a string de 26 lletres.
    """
   
    # Creem una llista de 26 elements buits que ens serveix de plantilla
    # per anar posant-hi lletres a les posicions adequades.
    inv = [""] * 26

    # Recorrem cada posició i lletra de la permutació
    for index_sortida, lletra_sortida in enumerate(perm):
        
        # i = posició original de la lletra (entrada del rotor)
        # lletra = lletra de sortida per a aquesta posició
        index_entrada = lletra_a_index(lletra_sortida)
        inv[index_entrada] = index_a_lletra(index_sortida)

    # Convertim l'Array (cablejat = 1ra linia del rotor) a String
    return "".join(inv)


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
    
    # Invertir les permutacions si s'està desxifrant
    if not xifrar:
        perm1 = inversa_permutacio(perm1)
        perm2 = inversa_permutacio(perm2)
        perm3 = inversa_permutacio(perm3)
    
    # Llegirem el arxiu "Missatge.txt" per xifrar el missatge.
    fitxer = None 
    try:
        fitxer = open(arxiu_entra, "rt")
        text = fitxer.read()
    
    # Llancem excepcions específiques per a cada tipus d'error.
    except FileNotFoundError as FileError:
        print(f"[ERROR] No s'ha pogut trobar el fitxer a: {arxiu_entra}")
        print(f"[DEBUG] Detall de l'error: {FileError}")
        
    except PermissionError as ErrorPermission:   
        print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {arxiu_entra}")
        print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
      
    except Exception as e:   
        print(f"[ERROR] Error inesperat a l'hora de guardar el missatge a: {arxiu_entra}")
        print(f"[DEBUG] Detall de l'error: {e}")
        
    # Assegurem el tancament del fitxer només si el open() s'executa correctament,
    # i detectem el fitxer encara obert.
    finally:
        if fitxer is not None and not fitxer.closed:
            fitxer.close()

    # Aquí s'ha de crear una nova funció
    
    # Procedim a netejar els accents del missatge
    text = netejar_missatge(text)

    # Un cop tenim la String neta, avançarem els rotors
    # per descobrir la possició del abacedari que pertany
    # cada una de les lletres que forma part el missatge del usuari.
    resultat = []

    for lletra in text:
        
        # Identifiquem la possició inicial dels rotors
        pos1, pos2, pos3 = avanca_rotors(pos1, pos2, pos3, notch1, notch2)
        
        # Invoquem cada lletra del missatge del usuari 
        # (amb el seu número de possició del abecedari) per xifrar-la.
        index = lletra_a_index(lletra)
        
        if xifrar:
            # Cada lletra passa per cada un dels rotors per xifrar-se
            index = passa_rotor(index, pos1, perm1)
            index = passa_rotor(index, pos2, perm2)
            index = passa_rotor(index, pos3, perm3)
        else: 
            # Per desxifrar el missatge, els rotors
            # rotacionen a la inversa respecte
            # el seu procés de xifratge.
            index = passa_rotor(index, pos3, perm3)
            index = passa_rotor(index, pos2, perm2)
            index = passa_rotor(index, pos1, perm1)
        
        # A la array de resultat, afegim cada lletra xifrada
        # vinculat al missatge del usuari
        resultat.append(index_a_lletra(index))
    
    # Convertim d'Array a String el missatge sencer xifrat
    resultat_final = "".join(resultat)
    
    # Si esta xifrant (sortida_agrupar_en_cinc == True), 
    # agrupa les lletres de 5 en cinc.
    if sortida_agrupar_en_cinc:
        resultat_final = agrupar_cinc(resultat_final)
    
    
    # Guardem el missatge xifrat al fitxer "Xifrat.txt"
    # Si falla open() abans d'executar-se, ens hem d'assegurar
    # que close() no s'executi sobre un fitxer mai obert.
    fitxer = None 
    try:
        # La "w" serveix per modificar el contingut d'un fitxer, o bé,
        # si no existeix: el crea. NO afegim la codificació UTF-8 en el cas
        # que l'usuari hagi afegit accents, ja que després els esborrarem.
        escriure_sortida = open(arxiu_surt, "w")
        escriure_sortida.write(resultat_final)
        print(f"[OK] Missatge {xifrar} guardat a {arxiu_surt}")
    
    # Llancem excepcions específiques per a cada tipus d'error.
    except FileNotFoundError as FileError:
        print(f"[ERROR] No s'ha pogut trobar el fitxer a: {arxiu_surt}")
        print("L'arxiu 'Missatge.txt' (key-sensitive) ha d'estar al projecte.")
        print(f"[DEBUG] Detall de l'error: {FileError}")
        
    except PermissionError as ErrorPermission:   
        print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {arxiu_surt}")
        print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
      
    except Exception as e:   
        print(f"[ERROR] Error inesperat a l'hora de guardar el missatge a: {arxiu_surt}")
        print(f"[DEBUG] Detall de l'error: {e}")
    
    # Assegurem el tancament del fitxer només si el open() s'executa correctament,
    # i detectem el fitxer encara obert.
    finally:
        if fitxer is not None and not fitxer.closed:
            fitxer.close()

# Rep un text i el retorna agrupat en blocs 
# de 5 caràcters separats per espais.
#
# Exemple: "ABCDEFGHIJ" -> "ABCDE FGHIJ"
def agrupar_cinc(text):
    
    # Guarda el text final, separat en lletres de 5 en 5
    text_agrupat = ""
    
    # Utilitzem enumerate per tenir control de l’índex (i) i l’element (lletra)
    # a iterar en una llista, tupla o string: sense haver d’incrementar
    # el comptador de manera manual.
    for i, lletra in enumerate(text):

        # Afegim un espai cada 5 caràcters (excepte al primer bloc)
        # Si el index es múltiple de 5, vol dir que hem de separar un bloc de 5
        if i != 0 and i % 5 == 0:
            text_agrupat = text_agrupat + " "

        # Afegim el missatge xifrat amb el nou format a la nova cadena.
        text_agrupat = text_agrupat + lletra

    return text_agrupat

# Passa una lletra pel rotor d'Enigma.
# index = lletra en format numèric (0–25)
# pos   = offset del rotor (rotació actual 0–25)
# perm  = cablejat del rotor (permutació de 26 lletres)
# !! offset = Desplaçament numèric d'un rotor 
#             respecte la seva posició anterior.
# !!
def passa_rotor(index, pos, perm):
    
    # Simula la rotació del rotor.
    entrada = (index + pos) % 26

    # Substitució de la lletra basat en la permutació
    lletra_sortida = perm[entrada]

    # Averiguem la possició de la lletra al alfavet
    pos_lletra = lletra_a_index(lletra_sortida)

    # Desfem la rotació del rotor per tornar a la possició anterior.
    index_sortida = (pos_lletra - pos) % 26
    return index_sortida


# avanca_rotors() — Métode que serveix per simular el moviment dels rotors 
#                   després d'una pulsació d'una lletra.
#
#  El rotor 1 (dreta) sempre avança una posició per cada lletra teclejada.
#  Quan el rotor 1 passa pel seu notch, el rotor 2 avança una posició.
#  Quan el rotor 2 surt del seu notch, llavors el rotor 3 avança una posició.
#
#  Nota: El rotor 3 no fa moure cap altre rotor 
#        perquè no existeix un quart rotor.
#

def avanca_rotors(pos1, pos2, pos3, notch1, notch2):

    # L'operació (pos + 1) % 26 garanteix que després 
    # de 'Z' (25), el rotor torni a 'A' (0),
    # simulant el moviment circular real dels engranatges.
    # pos1 suma 1 per cada lletra trobada al missatge del usuari.
    pos1 = (pos1 + 1) % 26

    # Si el rotor 1 està sobre el seu notch, en la pulsació següent:
    # el rotor 2 avança un pas.
    if pos1 == notch1:
        pos2 = (pos2 + 1) % 26

    if pos2 == notch2:
        pos3 = (pos3 + 1) % 26

    # Retorna la possició de la lletra vinculada al notch de cada rotor
    return pos1, pos2, pos3


# Simplement extreure els valors dels arxius rotors, 
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
    