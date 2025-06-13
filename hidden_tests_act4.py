def sol_precio_hotel_perros(num_dias, raza, peso, caminata_diaria, sesiones_entrenamiento):
    # YOUR CODE HERE
    if raza == "poodle" or raza == "chihuahua" or raza == "yorkshire": 
        precio_raza = 300 
    elif  peso < 7: 
        precio_raza = 350
    elif peso  < 14:  
        precio_raza = 400
    elif peso < 35: 
        precio_raza = 450
    elif peso >= 35: 
        precio_raza = 500
    resultado_raza = precio_raza * num_dias
    
    if caminata_diaria:
        caminata = num_dias * 200
    else:
        caminata = 0
   
    entrenamiento = sesiones_entrenamiento * 400
    
    resultado_esperado = resultado_raza + caminata + entrenamiento
    
    return resultado_esperado


def input_precio_hotel_perros(num_tests=15):
  ### num_dias, raza, peso, caminata_diaria, sesiones_entrenamiento
  input_values = [[]]*num_tests 
  from random import choices, choice
  razas = ["poodle", "chihuahua", "yorkshire", "pug", "beagle", "dalmata"]
  input_args = [{"num_dias":num_dias, "raza":raza, "peso":peso, "caminata_diaria":cam, "sesiones_entrenamiento":num_dias//choice(range(1, num_dias))-choice([0, 1])} 
                for num_dias, raza, peso, cam in zip(choices(range(2, 10), k=num_tests), 
                                                     choices(razas, k=num_tests), 
                                                     choices(range(5, 55), k=num_tests), 
                                                     choices([True, False], k=num_tests))]

  return input_values, input_args


def sol_diagnostico(urea, creatinina, bilirubina, fosfatasa_alcalina, colesterol):
    # YOUR CODE HERE
    sano = True
    if urea > 20 or urea < 7 or creatinina > 1.3 or creatinina < 0.7:
        sano = False
        print("El paciente podría tener una enfermedad renal.")
    if fosfatasa_alcalina < 30 or fosfatasa_alcalina > 120 or bilirubina < 0.3 or bilirubina > 1.0:
        sano = False
        print("El paciente podría tener una enfermedad hepática.")
    if colesterol < 100 or colesterol > 200 or bilirubina < 0.3 or bilirubina > 1.0:
        sano = False
        print("El paciente podría tener diabetes.")
        
    if sano:
        print("El paciente está en estado de salud.")


def input_diagnostico(num_tests=30):
  ### urea, creatinina, bilirubina, fosfatasa_alcalina, colesterol
  input_values = [[]]*num_tests
  from random import choices 
  input_args = [{"urea":urea, "creatinina":creatinina, "bilirubina":bilirubina, "fosfatasa_alcalina":fos_alc, "colesterol":colesterol} for 
                urea, creatinina, bilirubina, fos_alc, colesterol in zip(choices(range(3, 40), k=num_tests), 
                                                                         choices([i*0.1 for i in range(1, 20)], k=num_tests), 
                                                                         choices([i*0.1 for i in range(1, 15)], k=num_tests), 
                                                                         choices(range(10, 200, 10), k=num_tests), 
                                                                         choices(range(50, 250, 10), k=num_tests))]


  return input_values, input_args


def sol_piedra_papel_tijera(jugador_1, jugador_2):
    # YOUR CODE HERE
    if jugador_1 == jugador_2:
        print("Es un empate!")
    elif jugador_1 == "piedra":
        if jugador_2 == "papel":
            print("papel gana!")
        if jugador_2 == "tijera":
            print("piedra gana!")
    elif jugador_1 == "papel":
        if jugador_2 == "tijera":
            print("tijera gana!")
        if jugador_2 == "piedra":
            print("papel gana!")
    elif jugador_1 == "tijera":
        if jugador_2 == "papel":
            print("tijera gana!")
        if jugador_2 == "piedra":
            print("piedra gana!")



def input_piedra_papel_tijera():
  ### jugador_1, jugador_2
  input_values = [[]]*3**2
  from itertools import product 
  input_args = [{"jugador_1":jugador_1, "jugador_2":jugador_2} for jugador_1, jugador_2 in product(["piedra", "papel", "tijera"], repeat=2)]

  return input_values, input_args


