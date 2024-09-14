print("Zadej velikost čtverce:")

velikost = int(input())
strana = str("*" * velikost)
x = 0

for i in range(velikost):
    x += 1
    if x == velikost or x == 1:
        print(strana)
    else:
        print("*" + " " * (velikost - 2) + "*")
