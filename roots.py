from sys import stderr

def sqrt(x):
    """Compute the square root using the method of
    Heron of Alexandria.

    Args:
        x: The number for which the squre root to be computed.

    Return:
        The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Can't compute the square root of "
                        f"a negative number {x}")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return (guess)


def main():
    try :
        print(sqrt(9))
        print(sqrt(16))
        print(sqrt(-1))
        print("Never got printed")
    except ValueError as e:
        print(e, file=stderr)
    finally :
        print("Runs anyways")
    print("Program excution "
         "continues normally here.")


if __name__ == "__main__":
    main()
