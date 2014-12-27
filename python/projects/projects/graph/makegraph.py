#from networkx import nx

def parse(links):
    print links
    edges = links.split(',')

    nodes = {}
    for edge in edges:
        left, right = edge.split('-')
        if not left in nodes:
            nodes[left] = [right]
        elif right not in nodes[left]:
            nodes[left].append(right)

    return nodes

def show(nodes):
    print nodes # TODO: DiGraph library

# Input should be in the form
# A-B,B-C,C-D,D-A
# 
# A---B
# |   |
# D---C
def main(args):
    nodes = parse(''.join(args))
    show(nodes)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])