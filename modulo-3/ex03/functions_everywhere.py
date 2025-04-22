import sys

def shrink(s: str) -> str:
    return s[:8]

def enlarge(s: str) -> str:
    return s + 'Z' * (8 - len(s))

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
