from tabulate import tabulate

def makeTable():
  cells = [
  ]
  for i in range(-20, 31):
    cells.append([i, (i * 9) /5 + 32])
  head = ["Celsius", "Fahrenheit"]


  print(tabulate(cells, headers=head, tablefmt="grid"))

makeTable()