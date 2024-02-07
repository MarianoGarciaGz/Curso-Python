#* While: Mientras se cumpla la condición, se va a ejecutar
import random

num_random = random.randint(0, 10)
print(num_random)
attend = 0
num_attends = 5

num_input = input("Ingresa el número que estoy pensando: ")


if num_input == num_random:
  print("¡Ya has ganado a la primera!")
else:
  while num_random != num_input:
    num_input = int(input("Inténtalo de nuevo: "))
    attend += 1
  else:
    print("Has ganado a la " + str(attend) + "° oportunidad")
