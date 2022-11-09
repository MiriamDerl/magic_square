from tabulate import tabulate
import pyfiglet

class color:
    SUM = '\033[95m'
    ENDC = '\033[0m'

a = int(input("Gib eine Zahl a ein: "))
b = int(input("Gib eine Zahl b ein: "))

print("Magisches Quadrat: ")
print("----------------")
print("Zähle Spalte für Spalte, Zeile für Zeile, Diagonalen oder 2x2 Quadrate zusammen!")
print(color.SUM + "Die Summe lautet immer: " + str(11*a + 8*a + b + 2*a) + color.ENDC)

def main():
    table = [[a+b, a, 12*a, 7*a], [11*a, 8*a, b, 2*a], [5*a, 10*a, 3*a, 3*a+b], [4*a, 2*a+b, 6*a, 9*a]]
    print(tabulate(table, tablefmt="simple_grid", numalign="right"))
    print(pyfiglet.figlet_format("I LOVE YOU 4 ever <3" + input("Times i love you")))


if __name__ == "__main__":
    main()
