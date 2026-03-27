import re 

def main():
    print((validate(input("IPv4 Address: "))))


def validate(ip):
    num=re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if num:
        return all(0<=int(num.group(i))<=255 for i in range(1,5))
    else:
        return False

if __name__=="__main__":
    main()