def sol_palabra_en_texto(texto, palabra):
    # YOUR CODE HERE
    texto = texto.lower()
    palabra = palabra.lower()
    
    finder = texto.count(palabra)
    return finder

def input_palabra_en_texto(num_tests=15):
  input_values = [[]]*num_tests 
  words = ["hola", "si", "no", "yo", "ty", "cuando", "dijo", "el", "ella", "nosotros"]
  from random import choices, choice
  input_args = [{"texto":" ".join(choices(words), k=length), "palabra":choice(words)} for length in choices(range(10, 20), k=num_tests)]
  return input_values, input_args

def sol_letra_mas_comun(texto):
    # YOUR CODE HERE
    texto = texto.lower()
    
    elementos = []
    frecuencias = []
    for char in texto:
        if char.isalpha() and char not in elementos:
            elementos.append(char)
            frecuencias.append(texto.count(char))
    
    
    max_frec = max(frecuencias) 
    if frecuencias.count(max_frec) != 1:
        print("No hay letra más común.")
    else:
        ind = frecuencias.index(max_frec)
        print(f"La letra más común es: {elementos[ind]}")


def input_letra_mas_comun(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices
  input_args = [{"texto":"".join(choices("abcdeABCDEfgHigh", k=length))} for length in choices(range(20, 30), k=num_tests)]
  return input_values, input_args

def sol_capitalizar(texto):
    # YOUR CODE HERE
    resultado = ""
    texto = texto[0].upper() + texto[1:]
    ind = texto.find(". ")
    while ind != -1:
        texto = texto[0:ind+2] + texto[ind+2].upper() + texto[ind+3:]
        ind = texto.find(". ", ind+1)
    
    return texto

def input_capitalizar(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices, choice
  input_args = []
  words = ["hola", "esto", "texto", "yo", "tu", "nosotros", "dicen", "sabes", "que", "la", "no", "si"]
  for i in range(num_tests):
    sentences = []
    for j in range(choice(range(3, 6))):
      sentence = choices(words, k=choice(range(3, 10)))
      sentences.append(" ".join(sentence))
    input_args.append({"texto":". ".join(sentences) + "."})
  return input_values, input_args 


def sol_es_palindromo(texto):
    # YOUR CODE HERE
    texto = texto.lower() 
    t = ""
    for char in texto:
        if char.isalpha(): 
            t += char
    if t == t[::-1]: 
        print("Es un palíndromo.")     
    else: 
        print("No es un palíndromo.")

def input_es_palindromo(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices, choice
  ### 5 non-palindromes:
  input_args = [{"texto":"".join(choices("abcdEFSFDSABC", k=length))} for length in choices(range(5, 15), k=5)]
  ### 5 easy palindromes:
  for i in range(5):
    texto = "".join(choices("abcdefg",  k=choice(range(5, 10))))
    texto += texto[::-1].upper()
    input_args.append({"texto":texto})
  ### 5 medium palindromes:
  for i in range(5):
    texto = "".join(choices("abcdefg", k=choice(range(5, 10))))
    texto += texto[::-1].upper()
    inds = choices(range(len(texto)), k=3)
    texto = texto[:inds[0]] + " "  + texto[inds[0]:inds[1]] + " " + texto[inds[1]:inds[2]] + " " + texto[inds[2]:]
    input_args.append({"texto":texto})
  ### 5 hard palindromes:
  return input_values, input_args

def sol_son_anagramas(texto1, texto2):
    # YOUR CODE HERE
    t1 = ""
    for char in texto1:
        if char.isalpha():
            t1+=char.lower()
            
    t2 = ""
    for char in texto2:
        if char.isalpha():
            t2+=char.lower()
            
    anagramas = True
    for char in t1: 
        if t1.count(char) != t2.count(char): 
            anagramas = False

    if anagramas: 
        print("Son anagramas.")
    else:
        print("No son anagramas.")


def input_son_anagramas(num_tests=15):
  input_values = [[]]*num_tests 
  input_args = []
  from random import choice, choices
  ### non-anagrams:
  for i in range(5):
    length = choice(range(5, 10))
    input_args.append({"texto1":"".join(choices("abcdefghi", k=length)), "texto2":"".join(choices("abcdefghi", k=length))})
  ### anagrams:
  for i in range(10):
    texto = "".join(choices("abcdefghi", k=choice(range(5, 10))))
    texto_anagrama = texto
    ### add random capital letters:
    inds = choices(range(len(texto)), k=3)
    for ind in inds:
      texto = texto[:ind] + texto[ind].upper() + texto[ind+1:]
    ### add random spaces:
    inds = choices(range(len(texto)), k=3)
    for ind in inds:
      texto = texto[:ind] + " " + texto[ind:]
    input_args.append({"texto1":texto, "texto2":texto_anagrama})
  return input_values, input_args


