from math import sqrt
from itertools import islice, count

def is_prime(x):
    if x < 2:
        return (False)
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return (False)
    return (True)

prime_list = [x for x in range(101) if is_prime(x)]
print(prime_list)

def my_prime(x):
    if x < 2:
        return (False)
    for i in range(2, x):
        if x % i == 0:
            return (False)
    return (True)

my_list = [x for x in range(101) if my_prime(x)]
print(my_list)

def first(iterable):
    iterator = iter(iterable)
    try :
        return (next(iterator))
    except StopIteration:
        raise ValueError("Iterable is Empty")


def sum_thousand_prime():
    """Compute the sum of the first 1000 prime numbers using generators"""
    return (sum(islice((x for x in count() if is_prime(x)), 1000)))

if __name__ == "__main__":
    print(sum_thousand_prime())
