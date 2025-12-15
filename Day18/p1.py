import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    cubes = set()

    for line in data:
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

    directions = [
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1)
    ]

    print(sum(1 if (x + dx, y + dy, z + dz) not in cubes else 0
              for x, y, z in cubes
              for dx, dy, dz in directions))


if __name__ == "__main__":
    main()
