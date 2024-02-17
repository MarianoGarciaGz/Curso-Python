print("Si tu nombre aparece en la lista de invitados, puedes pasar")
name= str(input("Introduce tu nombre: "))

list_names = ["Mariano", "Oscar", "Alberto", "Andrea", "Abigail", "Guillermo", "Fernanda", "Fernando", "María", "Francisco"]
name_match = False

for i in range(0, len(list_names)):
  if str(list_names[i]) == name:
    name_match= True
    break
  else:
    name_match= False
    continue

if name_match == True:
  print("Estás en la lista de invitados")
else:
  print("No estás en la lista de invitados")