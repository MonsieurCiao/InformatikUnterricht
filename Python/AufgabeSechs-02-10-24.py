def bmi_kategorisierung():
    # Benutzereingaben
    alter = int(input("Bitte geben Sie Ihr Alter ein: "))
    height = float(input("Wie groß bist du in Metern? "))
    weight = float(input("Wie viel wiegst du in kg? "))
    bmi = weight/ height**2

    if alter < 25:
        if bmi < 19:
            kategorie = "Untergewicht"
        elif 19 <= bmi <= 24:
            kategorie = "Normalgewicht"
        else:
            kategorie = "Übergewicht"
    elif 25 <= alter <= 64:
        if bmi < 22:
            kategorie = "Untergewicht"
        elif 22 <= bmi <= 27:
            kategorie = "Normalgewicht"
        else:
            kategorie = "Übergewicht"
    else:  # Alter > 64
        if bmi < 24:
            kategorie = "Untergewicht"
        elif 24 <= bmi <= 29:
            kategorie = "Normalgewicht"
        else:
            kategorie = "Übergewicht"

    print(f"Sie haben {kategorie}.")

bmi_kategorisierung()