import sys

def gen_table(num: int) -> list[int]:
    table = []
    for i in range(11):
        table.append(num * i)
    return table

if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        table = gen_table(n)
        print(f"Table of {n}:", " ".join(map(str, table)))
    else:
        for num in range(10):
            table = gen_table(num)
            print(f"Table of {num}:", " ".join(map(str, table)))
