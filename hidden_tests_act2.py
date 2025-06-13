def sol_formula_cuadratica_suma(a, b, c):
  return (-b + (b**2-4*a*c)**0.5)/(2*a)

def input_formula_cuadratica_suma(num_tests=15):
  input_values = [[]]*num_tests
  from random import choices
  input_args = [{"a":a, "b":b, "c":c} for a, b, c in zip(choices(range(1,10), k=num_tests), choices(range(1,10), k=num_tests), choices(range(1,10), k=num_tests))]
  return input_values, input_args
