import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"^.+(https?://)(?:www\.)?(youtube)\.com/embed/(\w+).+", s)
    if link:
        return f"https://youtu.be/{link.group(3)}"
    else:
        return None


if __name__=="__main__":
    main()