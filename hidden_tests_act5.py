def sol_texto_numeros(x):
    # YOUR CODE HERE
    texto = ""
    primero = True
    for num in range (1,x+1):
        if not primero:
            texto += ", "
        else:
            primero = False
        texto += str(num)
    return texto

def input_texto_numeros(num_tests=15):
  input_values = [[]]*num_tests 
  input_args = [{"x":x} for x in range(1, num_tests+1)]
  return input_values, input_args 

def sol_sumar_numeros(x):
    # YOUR CODE HERE
    total = 0
    for num in range(x+1):
        total += num
    return total

def input_sumar_numeros(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices 
  input_args = [{"x":x} for x in choices(range(1, 50), k=num_tests)]
  return input_values, input_args

def sol_factorial(x):
    # YOUR CODE HERE
    num = 1
    for i in range (1,x+1):
        num *= i 
    return num

def input_factorial(num_tests=15):
  input_values = [[]]*num_tests 
  input_args = [{"x":x} for x in range(4, 4+num_tests)]
  return input_values, input_args

def sol_tabla_multiplicacion(x):
    # YOUR CODE HERE
    for tabla in range(11):
        print(f"{x} x {tabla} = {x*tabla}")


def input_tabla_multiplicacion(num_tests=15):
  input_values = [[]]*num_tests 
  input_args = [{"x":x} for x in range(1,11)]
  return input_values, input_args

def sol_promedio(lista_numeros):
    # YOUR CODE HERE
    total = 0
    cantidad = 0
    for i in(lista_numeros):
        cantidad += 1
        total += i 
    pro = total/cantidad
    print(f"El promedio es: {pro}")

def input_promedio(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices, choice
  input_args = [{"lista_numeros":choices(range(1, 50), k=choice([5, 10, 15, 20]))} for i in range(num_tests)]
  return input_values, input_args

def sol_factorizar(numero):
    # YOUR CODE HERE
    texto = ""
    primero = True
    for i in range(1,numero+1): 
        if numero%i==0: 
            if not primero:
                texto += ", "
            else:
                primero = False
            texto += str(i)
        
    print(f"Los factores son: {texto}")

def input_factorizar(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices
  input_args = [{"numero":num} for num in choices(range(1, 100), k=num_tests)]
  return input_values, input_args



