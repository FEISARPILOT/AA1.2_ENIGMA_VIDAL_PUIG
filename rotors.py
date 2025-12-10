#Llegeix i edita el rotor a petició de l'usuari 
def editar_rotor(arxiu):


    print("\n")
    print("  -------------------------------")
    print(f"|     Canvi arxiu: {arxiu}     |")
    print("  -------------------------------")
    
    permutacio_valida = False
    
    while not permutacio_valida:
        
        print("Ex de permutació (26 lletres A-Z): EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        perm= input("Donem una nova permutació:  ").strip().upper()

        # Cada rotor consta d'un fitxer de 26 lletres majúscules barrejades.
        # El control de la permutació es compara mitjançant dos sets.
        # Aquí es comprova que la longitud del usuari sigui de 26 amb A-Z.
        if len(perm) != 26:
            print("[ERROR] La permutació ha de contenir totes les lletres de l'alfabet exactament una vegada.")
            continue
        
        if set(perm) != set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            print("[ERROR] La permutació no te la longitud correcta.")
            continue
        
        print("[OK] La permutació té la longitud i els caràcters correctes.")

        # Llegir NOTCH actual
        fitxer = None 
        try:
            fitxer = open(arxiu,"rt")
            fitxer.readline() # saltem la lectura de la permutació
            print(f"[OK] Permutació llegida correctament {arxiu}")
            
            notch = fitxer.readline() # Només necessitem el notch 
            print(f"[OK] Notch llegit correctament {arxiu}")
            
        # Llancem excepcions específiques per a cada tipus d'error.
        except FileNotFoundError as FileError:
            print(f"[ERROR] No s'ha pogut trobar el fitxer a: {arxiu}")
            print(f"[DEBUG] Detall de l'error: {FileError}")
            continue   
        
        except PermissionError as ErrorPermission:   
            print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {arxiu}")
            print(f"[DEBUG] Detall de l'error: {ErrorPermission}")
            continue
         
        except Exception as e:   
            print(f"[ERROR] Error inesperat a l'hora de guardar el nu cablejat i notch del rotor a: {arxiu}")
            print(f"[DEBUG] Detall de l'error: {e}")
            continue
                
        # Assegurem el tancament del fitxer només si el open() s'executa correctament,
        # i detectem el fitxer encara obert.
        finally:
            if fitxer is not None and not fitxer.closed:
                fitxer.close()
           
        # Guardar nova permutació
        try:   
            fitxer = open(arxiu, "w")
            fitxer.write(perm + "\n" + notch)
            print(f"[OK] Nou rotor guardat a {arxiu}")
            
            # Si tot ha anat correctament, el nou rotor s'ha guardat.
            permutacio_valida = True
            
        # Llancem excepcions específiques per a cada tipus d'error.
        except FileNotFoundError as FileError:
            print(f"[ERROR] No s'ha pogut trobar el fitxer a: {arxiu}")
            print(f"[DEBUG] Detall de l'error: {FileError}")    
            
        except PermissionError as ErrorPermission:   
            print(f"[ERROR] L'usuari no té permís per modificar o crear el fitxer {arxiu}")
            print(f"[DEBUG] Detall de l'error: {ErrorPermission}") 
        
        except Exception as e:   
            print(f"[ERROR] Error inesperat a l'hora de guardar el nu cablejat i notch del rotor a: {arxiu}")
            print(f"[DEBUG] Detall de l'error: {e}")
            
        # Assegurem el tancament del fitxer només si el open() s'executa correctament,
        # i detectem el fitxer encara obert.
        finally:
            if fitxer is not None and not fitxer.closed:
                fitxer.close()



