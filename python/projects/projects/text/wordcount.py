def words(s):
    return len(str(s).split())

def main(args):
    import os.path
    if len(args) >= 1:
        input = args[1]
    else:
        sys.exit()

    data = input
    if os.path.exists(input):
        with open(input) as f:
            data = f.readlines()

    print words(data)

if __name__ == '__main__':
    import sys
    main(sys.argv)