import sys

def square_even_nbrs_new_trans(nbrs: list[int]) -> list[int]:
    """Square of just even numbers in list comprehension"""
    return [x * x for x in nbrs if x % 2 == 0]

n = sys.argv
if __name__ == "__main__":
    if len(n) > 1:
        nbrs = list(map(int, n[1].split()))
        res = square_even_nbrs_new_trans(nbrs)
        print(f"Squared evens new trans: {res}")
    else:
        print("Error, please provide a list of numbers.")