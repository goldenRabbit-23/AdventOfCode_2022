import sys
from collections import defaultdict


def main():
    data = open(sys.argv[1]).read().splitlines()
    elves = set()

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == '#':
                elves.add((r, c))

    move_offsets = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1),
    }

    check_dirs = {
        'N': [(-1, -1), (-1, 0), (-1, 1)],
        'S': [(1, -1), (1, 0), (1, 1)],
        'W': [(-1, -1), (0, -1), (1, -1)],
        'E': [(-1, 1), (0, 1), (1, 1)],
    }

    proposal_order = ['N', 'S', 'W', 'E']

    all_neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for _ in range(10):
        proposals = defaultdict(list)

        # Phase 1: Propose moves
        for r, c in elves:
            if all((r + dr, c + dc) not in elves for dr, dc in all_neighbors):
                continue

            for direction in proposal_order:
                if all((r + dr, c + dc) not in elves for dr, dc in check_dirs[direction]):
                    dr, dc = move_offsets[direction]
                    proposals[(r + dr, c + dc)].append((r, c))
                    break

        # Phase 2: Execute moves
        new_elves = set()
        moving_elves = set()

        for target, proposers in proposals.items():
            if len(proposers) == 1:
                new_elves.add(target)
                moving_elves.add(proposers[0])

        for r, c in elves:
            if (r, c) not in moving_elves:
                new_elves.add((r, c))

        elves = new_elves
        proposal_order.append(proposal_order.pop(0))

    min_r = min(r for r, c in elves)
    max_r = max(r for r, c in elves)
    min_c = min(c for r, c in elves)
    max_c = max(c for r, c in elves)

    print((max_r - min_r + 1) * (max_c - min_c + 1) - len(elves))


if __name__ == "__main__":
    main()
