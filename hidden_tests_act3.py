def sol_divisible_entre(numero,divisor):
    if numero%divisor==0:
        print(f"{numero} es divisible entre {divisor}")
    print("Fin.")

def input_divisible_entre(num_tests=20):
  input_values = [[]]*num_tests
  from random import choices
  input_args = [{"numero":numero, "divisor":divisor} for numero, divisor in zip(choices(range(100, 500), k=num_tests), choices(range(1, 10), k=num_tests))]
  return input_values, input_args

def sol_puede_votar(edad):
    if edad >= 18: 
        print("La persona puede votar.")
    elif edad < 18:
        print("La persona no puede votar.")

def input_puede_votar(num_tests=15):
  input_values = [[]]*num_tests 
  input_args = [{"edad":edad} for edad in range(15, 30)]
  return input_values, input_args

def sol_raices_parabola(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant < 0:
        print("No hay raíces.")
    elif discriminant==0:
        raiz= (-b)/(2*a)
        print(f"La raíz es: {raiz}.")
    else:
        raiz1 = (-b + discriminant**0.5)/(2*a)
        raiz2 = (-b - discriminant**0.5)/(2*a)
        print(f"Las raíces son: {raiz1} y {raiz2}.")


def input_raices_parabola(num_tests=30):
  input_values = [[]]*num_tests
  from random import choices
  input_args = [{"a":a, "b":b, "c":c} for a, b, c in zip(choices(range(-10, 11), k=num_tests), choices(range(-10, 11), k=num_tests), choices(range(-10, 11), k=num_tests))]
  return input_values, input_args


def sol_calcular_propina(precio, satisfaccion):
    # YOUR CODE HERE
    if satisfaccion == 5:
        return precio*0.3
    elif satisfaccion == 4:
        return precio*0.2
    elif satisfaccion == 3:
        return precio*0.15
    elif satisfaccion == 2:
        return precio*0.1
    elif satisfaccion == 1:
        return precio*0.05
    elif satisfaccion == 0:
        return 0
    else:
      return None

def input_calcular_propina(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"precio":precio, "satisfaccion":satisfaccion} for precio, satisfaccion in zip(choices(range(300, 500), k=num_tests), choices(range(0, 6), k=num_tests))]
  return input_values, input_args

