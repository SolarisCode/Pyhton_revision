#Display the nth root number in ordinal manner

def nth_root(radicand, n):
    return (radicand ** (1 / n))

def ordinal_suffix(value):
    if value.endswith("11"):
        return ("th")
    elif value.endswith("12"):
        return ("th")
    elif value.endswith("13"):
        return ("th")
    elif value.endswith("1"):
        return ("st")
    elif value.endswith("2"):
        return ("nd")
    elif value.endswith("3"):
        return ("rd")
    return ("th")

def ordinal(value):
    return (str(value) + ordinal_suffix(value))

def diplay_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(str(n)) + " root of " \
        + str(radicand) + " is " + str(root)
    print(message)
