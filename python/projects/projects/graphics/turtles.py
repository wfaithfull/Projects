import turtle

def drawsq(x, y, size):
    turtle.setx(x)
    turtle.sety(y)

    turtle.forward(size)

def main(args):
    drawsq(50,50,100)
    print('Hit any key to exit')
    raw_input()

if __name__ == '__main__':
    import sys
    main(sys.argv)