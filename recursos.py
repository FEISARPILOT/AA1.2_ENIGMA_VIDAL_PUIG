import extern
import os
#     # Retornem el patró de lletres i patró brut
#     return lletres_netejades, no_lletres

def verificar_fitxers_enigma():
    """
    Verifica que tots els fitxers necessaris pel funcionament de l'Enigma
    (definits a extern.py) existeixen a l'arrel del projecte.
    
    Retorna True si tot és correcte.
    Retorna False si falta algun fitxer.
    """

    print("[INFO] Verificant arxius necessaris per a Enigma...\n")

    # Recollim tots els fitxers que extern.py exposa
    fitxers_requerits = {
        "TXT: Missatge del usuari NO xifrat": extern.GUARDAR_MISSATGE_INICIAL,
        "TXT: Missatge del usuari XIFRAT": extern.GUARDAR_MISSATGE_XIFRAT,
        "TXT: Missatge desxifrat": extern.GUARDAR_MISSATGE_DESXIFRAT,
        "TXT: Rotor 1": extern.ROTOR1,
        "TXT: Rotor 2": extern.ROTOR2,
        "TXT: Rotor 3": extern.ROTOR3
    }
    
    # Valors per defecte dels rotors (cablejat + notch)
    rotors_defecte = {
        extern.ROTOR1: ("JGDQOXUSCAMIFRVTPNEWKBLZYH", "M"),
        extern.ROTOR2: ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "F"),
        extern.ROTOR3: ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "K")
    }

    tot_correcte = True
    fitxer = None 

    # Verifica si els fitxers s'ubiquen al projecte.
    for nom, ruta_fitxer in fitxers_requerits.items():

        # os.path.isfile comprova si el fitxer existeix al projecte.
        if os.path.isfile(ruta_fitxer):
            print(f"[OK] {nom} trobat: {ruta_fitxer}")
        else:
            print(f"[ERROR] El fitxer {nom} no està al projecte: {ruta_fitxer}")
            print(f"[INFO] Procedint a crear {nom} al projecte: {ruta_fitxer}")
            try:
                
                # La "w" serveix per modificar el contingut d'un fitxer, o bé,
                # si no existeix: el crea. NO afegim la codificació UTF-8 en el cas
                # que l'usuari hagi afegit accents, ja que després els esborrarem.
                fitxer = open(ruta_fitxer, "w")

                print(f"[OK] Fitxer creat correctament: {ruta_fitxer}")

            # Llancem excepcions específiques per a cada tipus d'error.
            except FileNotFoundError as FileError:
                print(f"[ERROR] No s'ha pogut trobar el fitxer a: {ruta_fitxer}")
                print(f"[DEBUG] Detall de l'error: {FileError}")

            except PermissionError as ErrorPermission:   
                print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {ruta_fitxer}")
                print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
               
            except Exception as e:   
                print(f"[ERROR] Error inesperat a l'hora de guardar el missatge a: {ruta_fitxer}")
                print(f"[DEBUG] Detall de l'error: {e}")
          

            # Assegurem el tancament del fitxer només si el open() s'executa correctament,
            # i detectem el fitxer encara obert.
            finally:
                if fitxer is not None and not fitxer.closed:
                    fitxer.close()

    print("")  # línia en blanc final

    # Si falta algun fitxer, continuem per crear-lo

    # Comprovem que rotor1, 2 o 3 están buits
    print("[INFO] Verificant contingut dels rotors...\n")
    
    fitxer = None 
    
    # Si el fitxer existeix, però està buit: el reomplim 
    # amb un cablejat i notch per defecte.
    for ruta_fitxer, (cablejat, notch) in rotors_defecte.items():
        try:
            # Comprovar si el fitxer està buit (el fitxer no pessa res)
            if os.path.getsize(ruta_fitxer) == 0:
                print(f"[WARNING] El fitxer {ruta_fitxer} està buit!")
                print(f"Afegint cablejat i notch per defecte a: {ruta_fitxer}")

                # La "w" serveix per modificar el contingut d'un fitxer, o bé,
                # si no existeix: el crea. NO afegim la codificació UTF-8 en el cas
                # que l'usuari hagi afegit accents, ja que després els esborrarem.
                fitxer = open(ruta_fitxer, "w")
                
                # Guardem el nou cablejat i el notch
                fitxer.write(cablejat + "\n") # 1ra linea
                fitxer.write(notch + "\n")    # 2na linea
                print(f"[OK] Rotor restaurat correctament: {ruta_fitxer}\n")

            else:
                print(f"[OK] {ruta_fitxer} té el cablejat i notch correcte.")

        # Llancem excepcions específiques per a cada tipus d'error.
        except FileNotFoundError as FileError:
            print(f"[ERROR] No s'ha pogut trobar el fitxer a: {ruta_fitxer}")
            print(f"[DEBUG] Detall de l'error: {FileError}")
            tot_correcte = False

        except PermissionError as ErrorPermission:   
            print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {ruta_fitxer}")
            print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
            tot_correcte = False

        except Exception as e:   
            print(f"[ERROR] Error inesperat a l'hora de guardar el missatge a: {ruta_fitxer}")
            print(f"[DEBUG] Detall de l'error: {e}")
            tot_correcte = False

        # Assegurem el tancament del fitxer només si el open() s'executa correctament,
        # i detectem el fitxer encara obert.
        finally:
            if fitxer is not None and not fitxer.closed:
                fitxer.close()

    return tot_correcte
    

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

# index_a_lletra() -> Métode que fa el revès que el métode lletra_a_index().
#                     Es a dir, index_a_lletra() serveix per obtenir la lletra ASCII 
#                     acord a una possició númerica.
def index_a_lletra(index):
              
    # Ens asegurem que la lletra sempre sigui majúscula.
    # IMPORTANT! ASCII es key-sensitive (A != a) -> 'A' = 65, però 'a' = 97.
    codi_A = ord('A')
 
    # Calculem el codi ASCII final sumant l'índex
    codi_resultat = codi_A + index

    # Averigüem la lletra ASCII acord a la seva possicó
    lletra = chr(codi_resultat)
    return lletra


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