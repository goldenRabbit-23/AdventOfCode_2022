import sys
from collections import defaultdict
from itertools import count


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

    for round_num in count(1):
        proposals = defaultdict(list)
        any_elf_considered_moving = False

        # Phase 1: Propose moves
        for r, c in elves:
            if all((r + dr, c + dc) not in elves for dr, dc in all_neighbors):
                continue

            for direction in proposal_order:
                if all((r + dr, c + dc) not in elves for dr, dc in check_dirs[direction]):
                    dr, dc = move_offsets[direction]
                    proposals[(r + dr, c + dc)].append((r, c))
                    any_elf_considered_moving = True
                    break

        if not any_elf_considered_moving:
            print(round_num)
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


if __name__ == "__main__":
    main()
