#! /usr/bin/env python3

from itertools import (islice, count, chain)

def take(count, iterable):
    counter = 0
    for item in iterable:
        if count == counter:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


def lucas():
    yield (2)
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def my_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def sum_thousand_prime():
    """Compute the sum of the first 1000 prime numbers using generators"""
    return (sum(islice((x for x in count() if my_prime(x)), 1000)))


def using_zip():
    saturday = [4, 16, 2, 9]
    sunday = [3, 12, 1, 10]
    monday = [2, 11, 3, 11]
    for sat, sun in zip(saturday, sunday):
        print(f"Saturday: {sat}, Sunday: {sun}")
    for sat, sun in zip(saturday, sunday):
        print(f"Avarage = {(sat + sun) / 2:.2f}")
    for temps in zip(saturday, sunday, monday):
        print(f"min = {min(temps):4.1f}, max = {max(temps):4.1f},"\
            " avarage = {sum(temps) / 3:4.1f}")
    # Using chain() will combine the 3 iterables as one stating
    # with the first and ending with the last
    print(all(x > 0 for x in chain(saturday, sunday, monday)))


def main():
    run_pipeline()


if __name__ == "__main__":
    # count = 0
    # iterator = lucas()
    # while count < 10:
    #     print(next(iterator))
    #     count += 1
    using_zip()

    # Check if there is a prime between 1328 and 1360 inclusive
    any(my_prime(x) for x in range(1328, 1361))
    # Check if all these cities have a capital letter at the beginning
    all(name == name.title() for name in ["Cairo", "London", "Berlin", "Hamburg", "Stockholm"])
