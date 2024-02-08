# Lista: Estructura de datos

# lista de días
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

# imprimir el primer días del array, luego el siguiente y así consecutivamente
print(days[0])
print(days[1])
print(days[2])
print(days[3])
print(days[4])
print(days[5])
print(days[6])

# Error intencional
# print(days[7])

#! Se pueden sobreescribir en una lista

days[0] = "Mariano"

print(days)

#

print("Faltan meses")
months = ["February","March","April","June","July","August","September","October","November"]
print(months)

#! Append
print("Agregamos los meses")
months.append("December")
months.insert(3,"May")
months.insert(0,"January")
print(months)

#! Count
print(months.count("June"))

#! Index
print(months.index("July"))

#! Remove
months.remove("April")
print("Removiendo April")
print(months)

#! Extend
print("Agregando meses inventados")
new_months = ["sapember, hellomenber"]
months.extend(new_months)
print(months)
