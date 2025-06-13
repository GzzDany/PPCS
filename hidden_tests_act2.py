def sol_formula_cuadratica_suma(a, b, c):
  return (-b + (b**2-4*a*c)**0.5)/(2*a)

def input_formula_cuadratica_suma(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices
  input_args = [{"a":a, "b":b, "c":c} for a, b, c in zip(choices(range(1,10), k=num_tests), choices(range(1,10), k=num_tests), choices(range(1,10), k=num_tests))]
  return input_values, input_args

def sol_calcular_hipotenusa(cateto1, cateto2):
  return (cateto1**2 + cateto2**2)**0.5

def input_calcular_hipotenusa(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices 
  input_args = [{"cateto1":cateto1, "cateto2":cateto2} for cateto1, cateto2 in zip(choices(range(1, 100), k=num_tests), choices(range(1, 100), k=num_tests))]
  return input_values, input_args

def sol_calcular_distancia(x1, y1, x2, y2):
    distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
    return distancia

def input_calcular_distancia(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices 
  input_args = [{"x1":x1, "y1":y1, "x2":x2, "y2":y2} for x1, y1, x2, y2 in zip(choices(range(100), k=num_tests), choices(range(100), k=num_tests), choices(range(100), k=num_tests), choices(range(100), k=num_tests))]
  return input_values, input_args

def sol_billetes_monedas(cantidad):
    ### Billetes: 500, 200, 100, 50, 20
    ### Monedas: 10, 5, 2, 1
    
    ### Código solucionado solo para determinar cuántos billetes de 500 hay que dar: 
    ### Cuántos billetes de 500 hay que dar? Se usa división de número entero
    billetes_500 = cantidad // 500 
    ### Opción 1 usando concatenación:
    print("Billetes de $500: " + str(billetes_500))
    ### Opción 2 usando f-strings
    ### print(f"Da {billetes_500} billetes de $500")

    ### Después de dar los billetes de 500, cuánto dinero hay que dar? 
    cantidad = cantidad%500 ### lo que sobra después de dividir entre 500

    ### YOUR CODE HERE
    cantidad_billetes200=cantidad//200
    print("Billetes de $200: " + str(cantidad_billetes200))
    cantidad = cantidad%200
    cantidad_billetes100=cantidad//100
    print("Billetes de $100: " + str(cantidad_billetes100))
    cantidad = cantidad%100
    cantidad_billetes50=cantidad//50
    print("Billetes de $50: " + str(cantidad_billetes50))
    cantidad = cantidad%50
    cantidad_billetes20=cantidad//20
    print("Billetes de $20: "+ str(cantidad_billetes20))
    cantidad = cantidad%20
    cantidad_monedas10=cantidad//10
    print("Monedas de $10: " + str(cantidad_monedas10))
    cantidad= cantidad%10
    cantidad_monedas5=cantidad//5
    print("Monedas de $5: "+ str(cantidad_monedas5))
    cantidad= cantidad%5
    cantidad_monedas2=cantidad//2
    print("Monedas de $2: "+str(cantidad_monedas2))
    cantidad = cantidad%2
    cantidad_monedas1=cantidad//1
    print("Monedas de $1: "+str(cantidad_monedas1))


def input_billetes_monedas(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices 
  input_args = [{"cantidad":cantidad} for cantidad in choices(range(600, 10000) k=num_tests)]
  return input_values, input_args
