from sys import argv, stderr
from math import log

DIGIT_MAP = {"one" : "1",
            "two" : "2",
            "three" : "3",
            "four" : "4",
            "five" : "5",
            "six" : "6",
            "seven" : "7",
            "eight" : "8",
            "nine" : "9",
            "zero" : "0"}

def convert(num_list):
    number = ""

    try :
        for num in num_list:
            number += DIGIT_MAP[num]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=stderr)
        raise


def string_log(s):
    v = convert(s)
    return (log(v))


def main():
    print(convert(argv[1].split()))


if __name__ == "__main__":
    main()
