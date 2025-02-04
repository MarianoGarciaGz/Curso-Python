# Escribe una función que tome como entrada una cadena de paréntesis () y determine si está balanceada. Una cadena de paréntesis está balanceada si cada paréntesis de apertura tiene un correspondiente paréntesis de cierre en el orden correcto.


def is_correct(text: str) -> bool:
    """Verifica si la cadena solo contiene los caracteres '(' y ')'."""
    return all(char in "()" for char in text)  # Asegura que solo tenga '(' y ')'


def is_balanced(text: str) -> bool:
    """Determina si la cadena de paréntesis está balanceada."""
    stack = []
    for char in text:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack  # Si la pila está vacía, está balanceada


# Bucle para pedir una cadena válida (solo '(' y ')')
while True:
    text = input("Introduce una cadena de paréntesis: ").strip()

    if not text:
        print("No se permiten cadenas vacías. Intenta de nuevo.")
        continue

    if is_correct(text):
        break  # Sale del bucle cuando la cadena es válida

    print("La cadena no es válida. Solo se permiten '(' y ')'. Intenta de nuevo.")

# Bucle para evaluar si está balanceada
while not is_balanced(text):
    print("La cadena NO está balanceada. Intenta de nuevo.")
    text = input("Introduce una cadena de paréntesis: ").strip()

    while not is_correct(text):  # Verificar si la cadena ingresada es correcta
        print("La cadena no es válida. Solo se permiten '(' y ')'. Intenta de nuevo.")
        text = input("Introduce una cadena de paréntesis: ").strip()

print("La cadena está balanceada.")
