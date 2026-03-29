import re


def main():
    print(count(input("Text: ")))


def count(s):
    text=re.findall(r"\bum\b",s, flags=re.IGNORECASE)
    if text:    
        return len(text)
    else:
        return 0


if __name__ == "__main__":
    main()