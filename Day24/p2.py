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

    gsr, gsc = -1, 0
    ger, gec = H, W - 1

    def is_safe(r, c, t):
        # 1. Check bounds
        if (r, c) == (gsr, gsc) or (r, c) == (ger, gec):
            return True
        if not (0 <= r < H and 0 <= c < W):
            return False

        # 2. Check blizzards
        if ((r + t) % H, c) in u_blizz: return False
        if ((r - t) % H, c) in d_blizz: return False
        if (r, (c + t) % W) in l_blizz: return False
        if (r, (c - t) % W) in r_blizz: return False

        return True

    def bfs(sr, sc, er, ec, st):
        q = deque([(sr, sc, st)])
        visited = set([(sr, sc, st)])

        while q:
            cr, cc, ct = q.popleft()

            if (cr, cc) == (er, ec):
                return ct

            for dr, dc in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = cr + dr, cc + dc

                if is_safe(nr, nc, ct + 1) and (nr, nc, ct + 1) not in visited:
                    q.append((nr, nc, ct + 1))
                    visited.add((nr, nc, ct + 1))

    t1 = bfs(gsr, gsc, ger, gec, 0)
    t2 = bfs(ger, gec, gsr, gsc, t1)
    t3 = bfs(gsr, gsc, ger, gec, t2)

    print(t3)


if __name__ == "__main__":
    main()
