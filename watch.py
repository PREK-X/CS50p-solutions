import re

def main():

    print(parse(input("HTML: ")))

def parse(s):

    try:
        link = re.search(r"<iframe.+\"(?P<link>(?P<start>https?://(?:www.)?youtube\.com/embed)/xvFZjo5PgG0)\".+</iframe>", s)

        change = re.sub(link.group("start"), "https://youtu.be", link.group("link"))
    except AttributeError:
        return None

    return change

if __name__ == "__main__":
    main()
