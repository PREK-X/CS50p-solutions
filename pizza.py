import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("To many Arguments!")
if len(sys.argv) < 2:
    sys.exit("To few arguments!")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not csv format file!")
try:
    with open(f"{sys.argv[1]}") as f:
        content = csv.DictReader(f)
        print(tabulate(content, headers = "keys", tablefmt = "grid"))
except FileNotFoundError:
    sys.exit("File not found!")
