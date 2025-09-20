import sys
from PIL import Image, ImageOps

def main():

    format = ("jpg","jpeg",".png")

    if len(sys.argv) < 3:
        sys.exit("To few Arguments!")
    if len(sys.argv) > 3:
        sys.exit("To many Arguments!")
    if not sys.argv[1].lower().endswith(format) or not sys.argv[2].lower().endswith(format):
        sys.exit("Wrong Format!")

    end1 = sys.argv[1].split(".")[-1]
    end2 = sys.argv[2].split(".")[-1]
    if end1 != end2:
        sys.exit("Same format required for both files!")

    with Image.open(sys.argv[1]) as im:

        copy = Image.open("shirt.png")
        size = im.size
        shirt_size = copy.size
        resize = ImageOps.fit(im, shirt_size)
        resize.paste(copy, mask = copy)
        resize.save(sys.argv[2])

if __name__ == "__main__":
    main()
