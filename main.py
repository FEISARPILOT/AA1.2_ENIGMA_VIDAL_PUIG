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