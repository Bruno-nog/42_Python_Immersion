import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 read_file.py <filename>")
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Error: File not found.")
        except IsADirectoryError:
            print("Error: The argument provided is a directory.")
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__}")
