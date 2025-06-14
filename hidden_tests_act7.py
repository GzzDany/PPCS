def sol_par_impar(numeros):
    # YOUR CODE HERE
    pares = []
    impares = []
    for n in numeros:
        if n% 2 == 0:
            pares.append(n)
        else: 
            impares.append(n)
    texto = 'Los números pares son: '
    primero = True
    for num in pares: 
        if not primero: 
            texto += ", "
        else: 
            primero = False
        texto += str(num)
    print(texto)
    
    texto = 'Los números impares son: '
    primero = True
    for num in impares: 
        if not primero: 
            texto += ", "
        else: 
            primero = False
        texto += str(num)
    print(texto)


def input_par_impar(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices, choice
  input_args = [{"numeros":choices(range(1, 50), k=choice(range(10, 20)))} for i in range(num_tests)]
  return input_values, input_args

def sol_combinar_listas(lista1, lista2):
    # YOUR CODE HERE
    combina = []
    for elemento_1, elemento_2 in zip(lista1, lista2): 
        combina += elemento_1, elemento_2
    return(combina)

def input_combinar_listas(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices 
  input_args = [{"lista1":choices(range(1, 10), k=length), "lista2":choices(range(1, 10), k=length)} for length in choices(range(5, 10), k=num_tests)]
  return input_values, input_args

def sol_promedio(numeros):
    # YOUR CODE HERE
    suma = sum(numeros)/len(numeros)
    return(suma)

def input_promedio(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices
  input_args = [{"numeros":choices(range(1, 100), k=length)} for length in choices(range(10, 20), k=num_tests)]
  return input_values, input_args

def sol_mediana(numeros):
    # YOUR CODE HERE
    numeros.sort()
    if len(numeros)%2 == 0: 
        ind = len(numeros)//2
        prom = (numeros[ind-1]+ numeros[ind])/2
        print(f"La mediana es: {prom}")
    else: 
        ind = len(numeros)//2
        print(f"La mediana es: {numeros[ind]}")

  def input_mediana(num_tests=15):
    input_values = [[]]*num_tests 
    from random import choices 
    input_args = [{"numeros":choices(range(1, 50), k=length)} for length in choices(range(7, 15), k=num_tests)]
    return input_values, input_args

def sol_frecuencias(elementos):
    # YOUR CODE HERE
    frecuencia = []
    for elemento in elementos: 
        frecuencia.append(elementos.count(elemento))
    
    ya_revisado = []
    for elemento, freq in zip(elementos, frecuencia):
        if elemento not in ya_revisado:
            print(f"El elemento {elemento} tiene frecuencia {freq}")
            ya_revisado.append(elemento)

def input_frecuencias(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"elementos":choices(range(1, 10), k=length)} for length in choices(range(8, 20), k=num_tests)]
  return input_values, input_args


def sol_moda(elementos):
    # YOUR CODE HERE
    numeros = []
    frecuencias = []
    for elemento in elementos: 
        if elemento not in numeros: 
            numeros.append(elemento)
            frecuencias.append(elementos.count(elemento))
    max_frecuencia = max(frecuencias)
    if frecuencias.count(max_frecuencia) == 1: 
        ind = frecuencias.index(max_frecuencia)
        print(f"La moda es: {numeros[ind]}")
    else:
        print("No hay moda.")

def input_moda(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"elementos":choices(range(1, 10), k=length)} for length in choices(range(8, 15), k=num_tests)]
  return input_values, input_args

def sol_filtrar(elementos, eliminar):
    # YOUR CODE HERE
    fil = []
    for elemento in elementos: 
        if elemento not in eliminar: 
            fil.append(elemento)
    return(fil)

def input_filtrar(num_tests=15):
  input_values = [[]]*15
  from random import choices, choice
  input_args = []
  for i in range(num_tests):
    elementos = choices(range(1, 50), k=choice(range(10, 20)))
    arg = {"elementos":elementos, "eliminar":choices(elementos, k=len(elementos)//3)}
    input_args.append(arg)
  return input_values, input_args

  

    
