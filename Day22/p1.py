import sys
import re


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

                if not (0 <= nr < H and 0 <= nc < W) or grid[nr][nc] == ' ':
                    if facing == 0:
                        nr, nc = r, 0
                        while grid[nr][nc] == ' ':
                            nc += 1
                    elif facing == 1:
                        nr, nc = 0, c
                        while grid[nr][nc] == ' ':
                            nr += 1
                    elif facing == 2:
                        nr, nc = r, W - 1
                        while grid[nr][nc] == ' ':
                            nc -= 1
                    elif facing == 3:
                        nr, nc = H - 1, c
                        while grid[nr][nc] == ' ':
                            nr -= 1

                if grid[nr][nc] == '#':
                    break

                r, c = nr, nc

    print(1000 * (r + 1) + 4 * (c + 1) + facing)


if __name__ == "__main__":
    main()
