import sys
from collections import deque


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

    min_x = min(x for x, y, z in cubes) - 1
    max_x = max(x for x, y, z in cubes) + 1
    min_y = min(y for x, y, z in cubes) - 1
    max_y = max(y for x, y, z in cubes) + 1
    min_z = min(z for x, y, z in cubes) - 1
    max_z = max(z for x, y, z in cubes) + 1

    start = (min_x, min_y, min_z)
    q = deque([start])
    visited = set([start])

    exterior_surface_area = 0

    while q:
        x, y, z = q.popleft()

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz

            if not (
                min_x <= nx <= max_x and
                min_y <= ny <= max_y and
                min_z <= nz <= max_z
            ):
                continue

            if (nx, ny, nz) in cubes:
                exterior_surface_area += 1
            elif (nx, ny, nz) not in visited:
                visited.add((nx, ny, nz))
                q.append((nx, ny, nz))

    print(exterior_surface_area)


if __name__ == "__main__":
    main()
