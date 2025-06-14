def sol_adn_complementario(adn):
    # YOUR CODE HERE
    
    bases = {"A":"T", "T":"A", "G":"C", "C":"G"}
    
    complementario = ""
    for letra in adn:
        complementario += bases[letra]
    return complementario

def input_adn_complementario(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"adn":"".join(choices("ATGC", k=length))} for length in choices(range(10, 20), k=num_tests)]
  return input_values, input_args

def sol_traduccion_morse(texto):
    codigo_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    " ": "/ " }
    # YOUR CODE HERE
    texto = texto.upper()
    
    codigo = ""
    primero = True
    
    for morse in texto: 
        if not primero:
            codigo += " "
        else: 
            primero = False
        
        codigo += codigo_morse[morse]
        
 
    return codigo

def input_traduccion_morse(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  words = ["ayuda", "hola", "no", "Solo", "Perdido", "peligro"]
  input_args = [{"texto":" ".join(choices(words, k=length))} for length in choices(range(5, 10), k=num_tests)]
  return input_values, input_args

def sol_piedra_papel_tijera(jugador1, jugador2):
    # YOUR CODE HERE
    ganador = {"piedra": "tijera" , "tijera":"papel" , "papel": "piedra"}
    if jugador1 == jugador2: 
        print("Es un empate!")
    elif jugador2 == ganador[jugador1]:
        print(f"{jugador1} gana!")
    else: 
        print(f"{jugador2} gana!")

def input_piedra_papel_tijera(num_tests=None):
  input_values = [[]]*3**2
  from itertools import product 
  input_args = [{"jugador1":jugador1, "jugador2":jugador2} for jugador1, jugador2 in product(["piedra", "papel", "tijera"], repeat=2)]
  return input_values, input_args 

