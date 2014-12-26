def tilecost(price, width, height):
    return (width * height) * price;

if __name__ == '__main__':
    from decimal import Decimal
    import sys
    import locale

    locale.setlocale(locale.LC_ALL, 'uk')

    price = Decimal(sys.argv[1])
    width = int(sys.argv[2])

    if sys.argv.count == 3:
        height == int(sys.argv[3])
    else:
        height = width

    print locale.currency(tilecost(price, width, height))