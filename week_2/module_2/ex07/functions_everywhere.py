import sys

def shrink(arg: str) -> str:
    """Returns the first 8 characteres"""
    return arg[:8]

def enlarge(arg: str) -> str:
    """Returns a string filled with `Z` to complete 8 characteres"""
    while len(arg) < 8:
        arg += "Z"
    return arg

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("None")
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                print(shrink(arg))
            elif len(arg) < 8:
                print(enlarge(arg))
            else:
                print(arg)
