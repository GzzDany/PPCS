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

def sol_piedra_papel_tijera_lagarto_spock(jugador1, jugador2):
    # YOUR CODE HERE
    ganador = {"piedra":["tijera" ,"lagarto"] , "tijera":["papel" , "lagarto"] , "papel": ["piedra" , "spock"] , 
               "lagarto":["spock","papel"], "spock":["tijera" , "piedra"]}
    if jugador1 == jugador2: 
        print("Es un empate!")
    elif jugador2 in ganador[jugador1]:
        print(f"{jugador1} gana!")
    else: 
        print(f"{jugador2} gana!")

def input_piedra_papel_tijera_lagarto_spock():
  input_values = [[]]*5**2
  from itertools import product 
  input_args = [{"jugador1":jugador1, "jugador2":jugador2} for jugador1, jugador2 in product(["piedra", "papel", "tijera", "lagarto", "spock"], repeat=2)]
  return input_values, input_args

def sol_formato_fecha(fecha):
    conversion_mes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 
          9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
    # YOUR CODE HERE
    dia =  str(int(fecha[3:5])) + " de " + conversion_mes[int(fecha[0:2])] + ", " + fecha[-4:] #int para covertir en número entero
    return dia

# def input_formato_fecha(num_tests=15):
#   input_values = [[]]*num_tests 
#   from random import choice 
#   input_args = [{"fecha":str(choice(range(1, 13)))+"/"+str(choice(range(1, 25)))+"/"+str(choice(range(1990, 2025)))} for i in range(num_tests)]
#   return input_values, input_args


def input_formato_fecha(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choice 
  input_args = []
  for i in range(num_tests):
    fecha = ""
    mes = choice(range(1, 13))
    dia = choice(range(1, 25))
    anio = choice(range(1990, 2025))
    if mes < 10:
      fecha += "0" + str(mes)
    else:
      fecha += str(mes)
    fecha += "/"
    if dia < 10:
      fecha += "0" + str(dia)
    else:
      fecha +=  str(dia)
    fecha += "/" + str(anio)
    input_args.append({"fecha":fecha})
  return input_values, input_args


def sol_contar_frecuencias_letras(texto):
    # YOUR CODE HERE
    diccionario = {}
    texto = texto.lower() 
    
    for letra in texto: 
        if letra.isalpha():
            if letra in diccionario: 
                diccionario[letra] += 1
            else: 
                diccionario[letra] = 1
            
    return diccionario


def input_contar_frecuencias_letras(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"texto":" ".join(choices("abcdefABDECFg", k=length))} for length in choices(range(20, 40), k=num_tests)]
  return input_values, input_args

def sol_clasificar_temperaturas(temperaturas):
    # YOUR CODE HERE
    for fecha, temperatura in temperaturas.items(): 
        if temperatura < 10: 
            print(f"{fecha} será un día frío.")
        elif temperatura > 30: 
            print(f"{fecha} será un día caluroso.")

def input_clasificar_temperaturas(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choice 
  input_args = []
  for i in range(num_tests):
    length = choice(range(5, 10))
    fechas = [str(choice(range(1, 12)))+ "/"+str(choice(range(1, 25)))+"/"+str(choice(range(1990, 2025))) for i in range(length)]
    temperaturas = [choice(range(10, 42)) for i in range(length)]
    input_args.append(dict(zip(fechas, temperaturas)))
  return input_values, input_args


