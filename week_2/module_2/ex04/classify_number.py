import sys

def is_positive(i: int) -> bool:
    """Takes a number and see if its positive or not"""
    if (i > 0):
        return True
    else:
        return False

if __name__ == "__main__":
    nb = int(sys.argv[1])
    print(is_positive(nb))