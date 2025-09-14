import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many arguments!")
if len(sys.argv) < 3:
    sys.exit("To many arguments!")
for arg in sys.argv[1:]:
    if not arg.endswith(".csv"):
        sys.exit("Wrong format!")

values = []

try:
    with open(f"{sys.argv[1]}") as f:
        content = csv.DictReader(f)
        for row in content:
            last, first = row["name"].split(", ")
            house = row["house"]
            value = {}
            value["first"] = first
            value["last"] = last
            value["house"] = house
            values.append(value)

except FileNotFoundError:
    sys.exit(f"Can't read {sys.argv[1]}!")

try:
    with open(f"{sys.argv[2]}", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(values)

except FileNotFoundError:
    sys.exit(f"Can't read {sys.argv[2]}!")

