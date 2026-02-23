import sys

word = sys.argv[1]

if __name__ == "__main__":
    print("São maiusculas?", word.isupper())
    print("É numérico?", word.isdigit())
    print("É ascii?", word.isascii())
    print("É alfanumérico?", word.isalnum())