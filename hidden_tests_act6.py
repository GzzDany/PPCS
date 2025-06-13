def sol_potencias(x):
    # YOUR CODE HERE
    y = 0
    while x**y <= 1500:
        pot = x**y
        y += 1
        print(pot)

def input_potencias(num_tests=15):
  input_values = [[]]*num_tests
  input_args = [{"x":x} for x in range(2, 2+num_tests)]
  return input_values, input_args

def sol_secuencia_collatz(x):
    # YOUR CODE HERE
    texto = ""
    primero = True
    while x != 1:     
        if not primero: 
            texto += ", "
        else: 
            primero = False
        texto += str(int(x))
        
        if x%2 == 0:
            x /= 2
        else: 
            x = (x*3)+1  
    
    texto += ", 1"
        
    print(f"La secuencia es: {texto}")

def input_secuencia_collatz(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"x":x} for x in choices(range(2, 100), k=num_tests)]
  return input_values, input_args

def sol_secuencia_fibonacci(limite):
    # YOUR CODE HERE
    num_1 = 0
    num_2 = 1
    num_3 = 1 
    primero = True 
    texto = "0, 1, "
    while num_1 + num_2 <= limite: 
        num_3 = num_1 + num_2
        num_1 = num_2
        num_2 = num_3
        if not primero: 
            texto += ", "
        else: 
            primero = False
        texto += str(int(num_3))
    
    print(f"La secuencia es: {texto}")

def input_secuencia_fibonacci(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"limite":limite} for limite in choices(range(100, 1000), k=num_tests)]
  return input_values, input_args

def sol_secuencia_pseudofibonacci(num_1, num_2, limite):
    # YOUR CODE HERE
    num_3 = 1
    primero = True 
    texto = f"{num_1}, {num_2}, "
    while num_1 + num_2 <= limite: 
        num_3 = num_1 + num_2
        num_1 = num_2
        num_2 = num_3
        if not primero: 
            texto += ", "
        else: 
            primero = False
        texto += str(int(num_3))
    
    print(f"La secuencia es: {texto}")

def input_secuencia_pseudofibonacci(num_tests=15):
  input_values = [[]]*num_tests 
  from random import choices 
  input_args = [{"num_1":num_1, "num_2":num_2, "limite":limite} for num_1, num_2, limite in zip(choices(range(1, 10), k=num_tests), 
                                                                                                choices(range(1, 10), k=num_tests), 
                                                                                                choices(range(100, 1000), k=num_tests))]
  return input_values, input_args

