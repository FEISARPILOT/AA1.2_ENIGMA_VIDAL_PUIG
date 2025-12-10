# AA1.2_ENIGMA_VIDAL_PUIG


# Que fa aquest projecte?
Aquest projecte és una implementació simple d'una màquina Enigma programa en Python. 
Permet xifrar i desxifrar missatges utilitzant tres rotors configurables.

# Què és la màquina ENIGMA?
La màquina ENIGMA es un dispositiu semblant a una maquina d'escriure que permet
xifrar i desxifrar missatges mitjançant l'us de rotors electromecanics.
Dita màquina, va ser inventada per Alemanya durant la WWII per protegir
les seves comunicacions a l'hora de desplegar tàctiques de batalla.

# ESQUEMA ASCII dels fitxers del projecte.
```
ENIGMA-BRANCH2/
│
├── Desxifrat.txt - Resultat de desxifrar el missatge xifrat
├── Missatge.txt  -  Missatge original no xifrat
├── Xifrat.txt    -  Missatge xifrat per Enigma
|
|   Cabejat: 1ra linea, Notch: 2na linia
├── rotor1.txt  - Cablejat i notch del rotor 1
├── rotor2.txt  - Cablejat i notch del rotor 2
├── rotor3.txt  - Cablejat i notch del rotor 3
│
├── main.py             - Menú Principal d'Enigma. Permet xifrar (1), desxifrar (2) i canviar la configuració dels rotors (3). 
├── extern.py           - Constants que invoquem les rutes dels arxius del projecte.
├── xifrar_desxifrar.py - Rotors que xifren i desxifren el missatge del usuari. 
├── rotors.py           - Modificar el cablejat i notch dels rotors (1 ,2, 3)
├── recursos.py         - Funcions auxiliars externes vinculades a mian.py, extern.py, xifrar_desxifrar.py i rotors.py (3)
```

## Funcionament del projecte ##

El menú ofereix les opcions:

1. Xifrar missatge
2. Desxifrar missatge
3. Editar rotors
4. Sortir

# Flux bàsic per xifrar/desxifrar:

# Xifrar
- Selecciona l'opció 1 (xifrar).
- Introdueix les 3 lletres de la finestra separades per espais (ex: `A B C`) que representen la posició inicial dels rotors.
- L'usuari introdueix un missatge on es guardarà en text pla al arxiu `Missatge.txt`.
  Després, el missatge es xifrarà i es guardarà a `Xifrat.txt` (1).

# Desxifrar
- Per desxifrar, escollirem la opció 2.
- Especificarem quines lletres de finestra vam utilizar anteriorment (ex: `A B C`).
- L'usuari introdueix el missatge xifrat del `Xifrat.txt` per poder desxifrar-lo.
- Si tot ha anat bé, el missatge desxifrat s'ha de veure a `Desxifrat.txt`
  el missatge original sense espais, i només amb lletres (A-Z)

# Edició de rotors:
- L'opició 3 ens permet indicar quin rotor volem editar (1, 2 , 3), on cada canvi:
  anirà vinculat al TXT vinculat a cada rotor: `rotor1.txt`, `rotor2.txt`, `rotor3.txt`
  per afegir el nou cablejat i 'notch'.


