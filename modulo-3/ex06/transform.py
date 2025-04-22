import sys

def square_even_numbers(nbrs: list[int]) -> list[int]:
    """Square of just even numbers"""
    evens = filter(lambda x: x % 2 == 0, nbrs)
    squared = map(lambda x: x * x, evens)
    return list(squared)

n = sys.argv
if __name__ == "__main__":
    if len(n) != 2:
        print("No arguments")
    else:
        str_numbers = n[1].split()
        int_numbers = list(map(int, str_numbers))
        res = square_even_numbers(int_numbers)
        print(f"Squared evens: {res}")  