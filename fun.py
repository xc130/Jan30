def main():
    """ Comments """
    add_two(1, 2)
    subtract_two(1, 2)
    bat = multiply_two(5, 5)
    print("This is the output of multiply two: {}".format(bat))


def add_two(v1, v2):
    """
    v1: number one
    v2: number two
    Returns: sum of number
    """
    p = v1 + v2
    return p


def subtract_two(v1, v2):
    """
    subtracts two numbers
    """
    p = v1 - v2
    return p


def multiply_two(v1, v2):
    """
    multiplies two numbers
    """
    return v1 * v2

if __name__ == "__main__":
    main()
