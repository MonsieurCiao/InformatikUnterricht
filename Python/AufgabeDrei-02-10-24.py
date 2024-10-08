def greet():
  name = input("Wie heißt du? ")
  alter = int(input("Wie alt bist du? "))

  print(f"Guten Tag {name}. Du bist", alter * 365, "Tage alt.");

greet()