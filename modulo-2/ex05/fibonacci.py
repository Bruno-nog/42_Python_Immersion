import sys

def fibonacci(nbr: int) -> int:
    if nbr == 0:
        return 0
    previous, curr = 0, 1
    index = 1
    while index < nbr:
        previous, curr = curr, previous + curr
        index += 1
    return curr

if __name__ == '__main__':
    nbr = int(sys.argv[1])
    print(fibonacci(nbr))
