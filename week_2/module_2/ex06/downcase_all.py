import sys

def downcase_it(args: str) -> str:
    return args.lower()

if __name__ == "__main__":
    args = sys.argv
    if (len(args) == 1):
        print("None")
    else:
        for i in args:
            print(downcase_it(i))
