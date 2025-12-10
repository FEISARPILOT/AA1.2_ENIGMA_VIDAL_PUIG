# Evitar problemes d'incompatiblitat a l'hora
# d'invocar fitxers a Python mitjançant l'ús de rutes absolutes.
import os 
base = os.path.dirname(__file__)

# Missatge.txt = Ruta absoluta del fitxer on es guarda el missatge original
ruta_missatge = os.path.join(base, "Missatge.txt") 


# Mencionem els fitxers externs vinculats al 'main.py'.
# Tot i així, nomes invoquem els métodes que necessitem
# d'aquests respectius fitxers per descartar tots aquells 
# métodes que no necessitem pas.
from recursos import lletra_a_index, guardar_missatge, verificar_fitxers_enigma
from rotors import editar_rotor
from xifrar_desxifrar import netejar_missatge, processar_amb_rotors

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

if not verificar_fitxers_enigma():
    print("[ERROR] El programa no es pot iniciar si falten fitxers essencials.")
    exit()
    
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

    # Invoquem cada lletra introduïda per la finestra
    pos1 = lletra_a_index(lletres_finestra[0])
    pos2 = lletra_a_index(lletres_finestra[1])
    pos3 = lletra_a_index(lletres_finestra[2])

    # Només sortim del bucle si el missatge del usuari compté només lletres 
    missatge_valid = False
    
    while not missatge_valid:
        # print("[INFO] Per motius de segureat, el missatge NOMÉS pot contenir entre 4-30 caracters.")
        missatge_usuari = input("Introdueix un missatge: ").strip()
        
        # L'usuari no pot introduïr missatges buits
        if not missatge_usuari:
            print(f"[ERROR] El missatge introduït està buit. Escriu un missatge entre 4-30 caracters")
            continue

        # S'ha de netejar el missatge per verificar 
        # que l'usuari ha introduït lletres en el missatge.
        missatge_net = netejar_missatge(missatge_usuari)
        if not missatge_net:
            print(f"[ERROR] El missatge introduït no conté lletres vàlides (A-Z). Torna-ho a intentar.")
            continue

        # total_missatge = len(missatge_usuari)
        # if not (4 <= total_missatge <= 30):
        #     print(f"[ERROR] El missatge introduït no té una longitud entre 4-30 caracters.")
        #     continue      
              
        # De moment, el misstge es valid encara es valid sense 
        # importar els simbols, numeros i lletres.
        missatge_valid = True
        
        print(f"[OK] El missatge es correcte parcialment: {lletres_finestra}\n")
        print(f"[INFO] Procedint a guardar-lo a '{ruta_missatge}'\n")
        print(f"[INFO] Loading... '\n")
    
    verificar_missatge = guardar_missatge(ruta_missatge, missatge_usuari)
    if (verificar_missatge):
        print(f"[OK] Missatge guardat correctament a '{ruta_missatge}'\n")
        # L'output del error s'ha escrit a la funció guardar_missatge()
    else:
        print("[INFO] Sortint del programa...")
        exit()

    # L'usuari vol xifrar o desxifrar un missatge.
    if decisio in (1, 2):
        xifrar = (decisio == 1)   # Xifrar (1) = True => Desxifrar (2) = False
        processar_amb_rotors(pos1, pos2, pos3, xifrar) 


# Cambiar rotor (3) 
elif decisio == 3:
    
    input_rotors = False
    
    #Gestio entrada valor rotor a editar.
    while not input_rotors:
        num_rotor_usuari = input("Quin rotor vols editar? (ex: 1, 2, 3): ").strip()
        
        # Intentem convertir el input del usuari a Int
        try:
            num_rotor = int(num_rotor_usuari)
        except ValueError:
            print("[ERROR] Has d'afegir un número.")
            continue
        
        if 1 <= num_rotor_usuari <= 3:
            arxiu = "rotor" + num_rotor_usuari + ".txt"
            print(f"Nom del arxiu del rotor a editar: {arxiu} ")
            
            editar_rotor(arxiu)
            input_rotors = True
        else:
            print("[ERROR] Has d'afegir un nombre entre 1 i 3.")

#Sortir(4)
else:
    print("\n[OK] Sortint de la maquina Enigma...")
    exit()
