
app = None

session = None

redis = None


def print_hello():
    if redis is not None:
        print("Hello")
        return 1
    print("Is none")
    return 0
