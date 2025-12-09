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


# guardar_missatge() -> 
# Métode que serveix per guardar el missatge del usuari a "Missatge.txt"
# per guardar allà el missatge en text plà.
def guardar_missatge(ruta_missatge, missatge):
    
    # Si falla open() abans d'executar-se, ens hem d'assegurar
    # que close() no s'executi sobre un fitxer mai obert.
    fitxer = None 
    missatge_al_txt = False
    try:
        # La "w" serveix per modificar el contingut d'un fitxer, o bé,
        # si no existeix: el crea. NO afegim la codificació UTF-8 en el cas
        # que l'usuari hagi afegit accents, ja que després els esborrarem.
        fitxer = open(ruta_missatge, "w")

        # Guardem el missatge del usuari a "Missatge.txt"
        fitxer.write(missatge)
        
        missatge_al_txt = True
      
    
    # Llancem excepcions específiques per a cada tipus d'error.
    except FileNotFoundError as FileError:
        print(f"[ERROR] No s'ha pogut trobar el fitxer a: {ruta_missatge}")
        print("L'arxiu 'Missatge.txt' (key-sensitive) ha d'estar al projecte.")
        print(f"[DEBUG] Detall de l'error: {FileError}")
        
    except PermissionError as ErrorPermission:   
        print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {ruta_missatge}")
        print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
      
    except Exception as e:   
        print(f"[ERROR] Error inesperat a l'hora de guardar el missatge a: {ruta_missatge}")
        print(f"[DEBUG] Detall de l'error: {e}")
        
    # Assegurem el tancament del fitxer només si el open() s'executa correctament,
    # i detectem el fitxer encara obert.
    finally:
        if fitxer is not None and not fitxer.closed:
            fitxer.close()
        
    return missatge_al_txt