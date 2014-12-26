def words(s):
    return len(str(s).split())

if __name__ == '__main__':
    import sys, os.path
    if len(sys.argv) >= 1:
        input = sys.argv[1]
    else:
        sys.exit()

    data = input
    if os.path.exists(input):
        with open(input) as f:
            data = f.readlines()

    print words(data)