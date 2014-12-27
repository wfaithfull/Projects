def closestpair(points):
    if len(points) == 2:
        return (dist(points[0],points[1]), points)

    # sort by x
    sortedpoints = sorted(points, key=lambda x: x[0])

    left = sortedpoints[:len(sortedpoints)/2]
    right = sortedpoints[len(sortedpoints)/2:]

    # each pair is a tuple of (distance, [p1, p2])
    pair1 = closestpair(left)
    pair2 = closestpair(right)

    return min([pair1,pair2], key=lambda x: x[0])

def dist(p1, p2):
    from math import hypot
    return hypot(p2[0] - p1[0], p2[1] - p1[1])

def main(args):
    print closestpair([[1,1],[3,3],[3,4],[0,0]])

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])