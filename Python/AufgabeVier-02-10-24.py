import random 
def randInt():
  zahl = random.randint(0, 100)

  nichtErraten = True
  versuche = 0
  print("Errate eine Zahl von 0 bis 100!")
  while nichtErraten:
    guess = int(input("Rate! "))
    versuche = versuche + 1
    if guess > zahl:
      print("Zu hoch!")
    elif guess < zahl:
      print("Zu klein!")
    else:
      print("Richtig! Die Zahl war ", zahl, ". Du hast ", versuche, " Versuche gebraucht.")
      nichtErraten = False
randInt()