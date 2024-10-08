def bmiCalc():
  print("Lass uns deinen BMI (Body Mass Index) berechnen.")
  height = float(input("Wie groß bist du in Metern? "))
  weight = float(input("Wie viel wiegst du in kg? "))
  print("Du hast einen BMI von " + str(weight/ height**2))
bmiCalc()