import sys
from collections import deque


def main():
    grid = open(sys.argv[1]).read().splitlines()
    R, C = len(grid), len(grid[0])
    H, W = R - 2, C - 2

    u_blizz = set()
    d_blizz = set()
    l_blizz = set()
    r_blizz = set()

    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if ch == '^': u_blizz.add((r - 1, c - 1))
            elif ch == 'v': d_blizz.add((r - 1, c - 1))
            elif ch == '<': l_blizz.add((r - 1, c - 1))
            elif ch == '>': r_blizz.add((r - 1, c - 1))

    sr, sc = -1, 0
    er, ec = H, W - 1

    def is_safe(r, c, t):
        # 1. Check bounds
        if (r, c) == (sr, sc) or (r, c) == (er, ec):
            return True
        if not (0 <= r < H and 0 <= c < W):
            return False

        # 2. Check blizzards
        if ((r + t) % H, c) in u_blizz: return False
        if ((r - t) % H, c) in d_blizz: return False
        if (r, (c + t) % W) in l_blizz: return False
        if (r, (c - t) % W) in r_blizz: return False

        return True

    q = deque([(sr, sc, 0)])
    visited = set([(sr, sc, 0)])

    while q:
        cr, cc, ct = q.popleft()

        if (cr, cc) == (er, ec):
            print(ct)
            break

        for dr, dc in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc

            if is_safe(nr, nc, ct + 1) and (nr, nc, ct + 1) not in visited:
                q.append((nr, nc, ct + 1))
                visited.add((nr, nc, ct + 1))


if __name__ == "__main__":
    main()
