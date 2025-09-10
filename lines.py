import sys

if len(sys.argv) > 2:
    sys.exit("To many Arguments!")
elif len(sys.argv) < 2:
    sys.exit("To few Arguments!")
else:
    i = 0
    try:
        if sys.argv[1].endswith(".py"):
            with open(f"{sys.argv[1]}") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    if line.startswith("#"):
                        continue

                    i += 1
                print(i, end = "")

        else:
            sys.exit("File Format not Correct!")
    except FileNotFoundError:
        sys.exit("File Not Found!")
