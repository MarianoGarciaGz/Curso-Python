#* Match

vocal = input("Introduce una vocal: ")

match vocal:
  case "a":
    print("Sí es vocal")
  case "e":
    print("Sí es vocal")
  case "i":
    print("Sí es vocal")
  case "o":
    print("Sí es vocal")
  case "u":
    print("Sí es vocal")
  case _: #! Esto es como un else
    print("No es una vocal")