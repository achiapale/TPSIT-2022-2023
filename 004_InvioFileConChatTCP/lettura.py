import sys

def read_file_and_print(f):
    go_on = True
    while go_on:
        data = f.read(10)
        if data:
            print(data)
        else:
            go_on = False

def main(args):
    if len(args) < 2:
        print(f"Usage: {args[0]} nomefile")
        sys.exit(-1)

    nomefile = args[1]

    try:
        f = open(nomefile, "rb")
    except FileNotFoundError as e:
        print(e)
        sys.exit(-1)

    try:
        read_file_and_print(f)
    except IOError as e:
        print(e)
    finally:
        f.close()


if __name__ == "__main__":
    main(sys.argv)
