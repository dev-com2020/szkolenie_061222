import argparse
import sys
import logging

log_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
log_level = logging.DEBUG


def main(number, other_number, output):
    logging.info(f'dzielenie {number} przez {other_number}')
    result = number / other_number
    print(f"Wynik wynosi {result}")


parser = argparse.ArgumentParser()
parser.add_argument("-n1", type=int, help="Liczba", default=1)
parser.add_argument("-n2", type=int, help="Inna liczba", default=1)
parser.add_argument("-l", dest='log', type=str, help="plik dziennika", default=None)
parser.add_argument("-o", dest='output', type=argparse.FileType("w"), help="Plik na dane", default=sys.stdout)

args = parser.parse_args()
if args.log:
    logging.basicConfig(format=log_format, filename=args.log, level=log_level)
else:
    logging.basicConfig(format=log_format, level=log_level)

try:
    main(args.n1, args.n2, args.output)
except Exception as e:
    logging.exception("Błąd w czasie wykonywania zadania")
    exit(1)
