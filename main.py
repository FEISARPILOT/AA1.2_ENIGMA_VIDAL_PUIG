# Evitar problemes d'incompatiblitat a l'hora
# d'invocar fitxers a Python mitjançant l'ús de rutes absolutes.
import os 
base = os.path.dirname(__file__)

# Missatge.txt = Ruta absoluta del fitxer on es guarda el missatge original
ruta_missatge = os.path.join(base, "Missatge.txt") 

sortir_menu = False
    
print("-------------------------------")
print(r"""
          
   ██████████ ██████   █████ █████   █████████  ██████   ██████   █████████  
   ░███░░░░░█░░██████ ░░███ ░░███   ███░░░░░███░░██████ ██████   ███░░░░░███ 
   ░███  █ ░  ░███░███ ░███  ░███  ███     ░░░  ░███░█████░███  ░███    ░███ 
   ░██████    ░███░░███░███  ░███ ░███          ░███░░███ ░███  ░███████████ 
   ░███░░█    ░███ ░░██████  ░███ ░███    █████ ░███ ░░░  ░███  ░███░░░░░███ 
   ░███ ░   █ ░███  ░░█████  ░███ ░░███  ░░███  ░███      ░███  ░███    ░███ 
   ██████████ █████  ░░█████ █████ ░░█████████  █████     █████ █████   █████
    ░░░░░░░░░░ ░░░░░    ░░░░░ ░░░░░   ░░░░░░░░░  ░░░░░     ░░░░░ ░░░░░   ░░░░░                                                                      
                                                                            
    """)

print("-------------------------------")
    
# Només es surt del menú principal d'Enigma
# si s'escull una opció correcte.
while not sortir_menu:
    print("\n")
        
    print("-------------------------------")
    print("      Menú Principal           ")
    print("-------------------------------")
    print("\n")
    print("\t 1. Xifrar missatge \n")
    print("\t 2. Desxifrar missatge \n")
    print("\t 3. Editar rotors \n")
    print("\t 4. Sortir \n")


    # Esborrem espais a la dreta i a l'esquerra
    # per treballar amb un input net.
    decisio = input("Introdueix una opció : ").strip()

    # Si l'entrada de l'usuari està buida. Torna al menú principal
    if not decisio:
        print("\n[ERROR] La entrada del usuari es buida. Introdueix un número d'1-4.")
        continue
    
    # Si no es pas un dígit (0-9). Torna al menú principal
    if not decisio.isdigit():
        print("\n[ERROR] La entrada del usuari no es pas un dígit. Introdueix un número d'1-4.")
        continue

    # Convertim de String a Integer per revisar
    # si el número del usuari està dintre del rang.
    decisio = int(decisio) 
    
    if 1 <= decisio <= 4: # 1 - 4
        
        # El número introduït està en el menú.
        sortir_menu = True
    else:
        # Numero incorrecte, NO està en el menú.
        print(f"\n[ERROR] El número: {decisio} no està dintre del rang. El número ha de ser d'1-4.")
    

# El bucle s'ha acabat. L'opció del usuari es correcte.
print(f"[OK] Has triat l'opció {decisio}\n")


# Xifrar (1) o Desxifrar (2)
# Aquí millor una llista ja que només son dos nombres fixos
# al estar vinculats a una opció concreta del menú.

if decisio in (1,2):
    # Es tornarà True si el format de les lletres de la finestra son correctes.
    lletres_finestra_valides = False
    
    # Si es detecta un element del array no vàlid, reiniciem el bucle.
    element_array_no_valid = False
    
    while not lletres_finestra_valides:
        print("[INFO] Les lletres no tenen perquè ser ordenades alfabeticament. (A-Z)")
        print("[INFO] Cada una de les 3 lletres es OBLIGATORI que estiguin separades per un espai. Ex: A B C")
        lletres_finestra = input("Introdueix lletres de la finestra (ex: A B C): ").upper().split()
        print("\n")

        # Si el patró de la finestra està buit:
        # Torna al menú principal.
        if not lletres_finestra:
            print("[ERROR] La entrada del usuari està buida.")
            continue
        
        # Comprovem que el patró de la finestra té exactament 3 caracters.
        if not len(lletres_finestra) == 3:
            print("[ERROR] La entrada del usuari ha de tenir un patró exacte de 3 lletres (A-Z) separada cada una d'elles per espais.")
            continue
        
        # Verifiquem que cada element de la llista sigui una sola lletra.
        for lletra in lletres_finestra:
            if len(lletra) != 1 or not lletra.isalpha():
                print(f"[ERROR] L'element '{lletra}' NO és vàlid. Cada espai NOMÉS ha de tenir una sola lletra.")
                element_array_no_valid = True
                break

        # Si es detecten elements d'array no vàlids, 
        # tornem a demanar noves finestres.
        if element_array_no_valid:
            continue
        
        # El bucle s'ha acabat. 
        # Les lletres coincideixen amb el patró de la finestra.    
        lletres_finestra_valides = True
        
    print(f"[OK] El patró es correcte: {lletres_finestra}\n")