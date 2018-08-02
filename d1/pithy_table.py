import sys


def pithy_table():
    for y in range(1, 10):
        for x in range(1, y+1):
            print("%d + %d = %d" % (x, y, x+y), end="   ")
        print()


def pithy_table_align():
    for y in range(1, 10):
        for x in range(1, y+1):
            print("%d + %d = %-2d" % (x, y, x+y), end="   ")
        print()


def pithy_table_align_n(n):
    for y in range(1, n+1):
        for x in range(1, y+1):
            print("%d + %d = %-2d" % (x, y, x+y), end="   ")
        print()


def pithy_table_align_n_file(n, f=sys.stdout):
    for y in range(1, n+1):
        for x in range(1, y+1):
            print("%d + %d = %-2d" % (x, y, x+y), end="   ", file=f)
        print(file=f)
    print(file=f)


def pithy_table_align_n_file_max(n, f=sys.stdout):
    for y in range(1, n+1):
        row = ""
        for x in range(1, y+1):
            row += "%d + %d = %-2d   " % (x, y, x+y)
        row += "\n"
        f.write(bytes(row, "utf8"))
    f.write(bytes("\n", "utf8"))
