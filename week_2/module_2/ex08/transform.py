import sys

def square_even_numbers(nums: list[int]) -> list[int]:
    """Return a list of even numbers squared"""
    return [even**2 for even in nums if even % 2 == 0]

args = sys.argv
if __name__ == "__main__":
    if len(args) != 2:
        print("No arguments")
    else:
        str_numbers = args[1].split()
        int_numbers = list(map(int, str_numbers))
        res = square_even_numbers(int_numbers)
        print(f"Squared evens: {res}")

