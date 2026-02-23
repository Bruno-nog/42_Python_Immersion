import sys

args = sys.argv

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Only one arguments is valid.")
    else:
        try:
            num = float(args[1])
            print(num)
        except ValueError:
            print("conversion impossible")
