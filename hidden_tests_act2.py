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
