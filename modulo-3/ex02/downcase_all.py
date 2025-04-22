import sys

low = str(sys.argv[1])

def downcase_it(string: str) -> str:
    """Transform an string in lower"""
    return string.lower()

if len(sys.argv) == 1:
    print("None")
else:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))
