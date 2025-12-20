import sys
import re


def wrap_cube(r, c, facing):
    """
    . 1 2
    . 3 .
    4 5 .
    6 . .
    """
    # Region 1
    if 0 <= r < 50 and 50 <= c < 100:
        if facing == 2: return (149 - r, 0, 0)
        if facing == 3: return (c + 100, 0, 0)
    # Region 2
    if 0 <= r < 50 and 100 <= c < 150:
        if facing == 0: return (149 - r, 99, 2)
        if facing == 1: return (c - 50, 99, 2)
        if facing == 3: return (199, c - 100, 3)
    # Region 3
    if 50 <= r < 100 and 50 <= c < 100:
        if facing == 0: return (49, r + 50, 3)
        if facing == 2: return (100, r - 50, 1)
    # Region 4
    if 100 <= r < 150 and 0 <= c < 50:
        if facing == 2: return (149 - r, 50, 0)
        if facing == 3: return (c + 50, 50, 0)
    # Region 5
    if 100 <= r < 150 and 50 <= c < 100:
        if facing == 0: return (149 - r, 149, 2)
        if facing == 1: return (c + 100, 49, 2)
    # Region 6
    if 150 <= r < 200 and 0 <= c < 50:
        if facing == 0: return (149, r - 100, 3)
        if facing == 1: return (0, c + 100, 1)
        if facing == 2: return (0, r - 100, 1)

def main():
    raw_map, raw_path = open(sys.argv[1]).read().split("\n\n")

    lines = raw_map.splitlines()
    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width) for line in lines]
    H, W = len(grid), len(grid[0])
    path = re.findall(r'(\d+|[LR])', raw_path)

    r, c = 0, 0
    while grid[r][c] == ' ':
        c += 1

    facing = 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for instruction in path:
        if instruction == 'L':
            facing = (facing - 1) % 4
        elif instruction == 'R':
            facing = (facing + 1) % 4
        else:
            steps = int(instruction)

            for _ in range(steps):
                dr, dc = dirs[facing]
                nr, nc = r + dr, c + dc
                new_facing = facing

                if not (0 <= nr < H and 0 <= nc < W) or grid[nr][nc] == ' ':
                    nr, nc, new_facing = wrap_cube(r, c, facing)

                if grid[nr][nc] == '#':
                    break

                r, c = nr, nc
                facing = new_facing

    print(1000 * (r + 1) + 4 * (c + 1) + facing)


if __name__ == "__main__":
    main()
