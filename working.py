import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    hours=re.search(r"^(\d+):?(\d+)? (\w+) to (\d+):?(\d+)? (\w+)",s,flags=re.IGNORECASE)
    if hours:
        if hours.group(2)==None :
            if hours.group(5)==None:
                return f"{format_change(int(hours.group(1)), 0, hours.group(3))} to {format_change(int(hours.group(4)),0, hours.group(6))}"
            else:
                return f"{format_change(int(hours.group(1)), 0, hours.group(3))} to {format_change(int(hours.group(4)),int(hours.group(5)), hours.group(6))}"
        else:
            if hours.group(5)==None:
                return f"{format_change(int(hours.group(1)), int(hours.group(2)), hours.group(3))} to {format_change(int(hours.group(4)),0, hours.group(6))}"
            else:
                return f"{format_change(int(hours.group(1)), int(hours.group(2)), hours.group(3))} to {format_change(int(hours.group(4)),int(hours.group(5)), hours.group(6))}"
    else:
        raise ValueError


def format_change(hour, min, period):
    if 1<=hour<=12 and 0<=min<60: 
        if period=="AM":
            if hour == 12:
                hour-=12
            return f"{hour:02}:{min:02}"
        elif period=="PM":
            if hour==12:
                hour-=12
            return f"{hour+12}:{min:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()

