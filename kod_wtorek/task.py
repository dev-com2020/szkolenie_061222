import argparse
import sys


def main(number, other_number):
    result = number / other_number
    print(f"Wynik wynosi {result}")


parser = argparse.ArgumentParser()
parser.add_argument("-n1", type=int, help="Liczba", default=1)
parser.add_argument("-n2", type=int, help="Inna liczba", default=1)

args = parser.parse_args()
main(args.n1, args.n2)





# Napisz program, który korzystając z instrukcji while, sumuje liczby parzyste
# od 1 do 100.

# Napisz program, który za pomocą instrukcji while sumuje wszystkie liczby
# całkowite od 1 do 100.

# Napisz program, który wyświetla duże litery alfabetu od A do Z i od Z do A
# z wykorzystaniem pętli for.