import sys
from itertools import count, islice

def sequence():
    """Generate the Recaman's sequence"""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if (c < 0) or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    # f = open(filename, mode="wt", encoding="utf-8")
    # f.writelines(f"{x}\n" for x in islice(sequence(), num + 1))
    # f.close()
    # Refactoring :
    with open(filename, mode="wt", encoding="utf-8") as f:
        f.writelines(f"{x}\n" 
                    for x in islice(sequence(), num + 1))


def read_sequence(filename):
    # try :
    #     f = open(filename, mode="rt", encoding="utf-8")
    #     return [int(line.strip())  for line in f]
    # finally :
    #     f.close()
    # Refactoring :
    with open(filename, mode="rt", encoding="utf-8") as f:
        return [int(line.strip()) for line in f]


if __name__ == "__main__":
    write_sequence(sys.argv[1], int(sys.argv[2]))
    print(read_sequence(sys.argv[1]))
