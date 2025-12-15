import sys


SHAPE_H_LINE = [(0, 0), (1, 0), (2, 0), (3, 0)]
SHAPE_PLUS = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
SHAPE_L = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
SHAPE_V_LINE = [(0, 0), (0, 1), (0, 2), (0, 3)]
SHAPE_SQUARE = [(0, 0), (1, 0), (0, 1), (1, 1)]

ROCKS = [SHAPE_H_LINE, SHAPE_PLUS, SHAPE_L, SHAPE_V_LINE, SHAPE_SQUARE]

def main():
    jet_pattern = open(sys.argv[1]).read()
    chamber = set()
    top_y = 0
    jet_idx = 0

    dirs = {'>': 1, '<': -1}
    num_jets = len(jet_pattern)

    def is_valid(shape, pos_x, pos_y):
        for dx, dy in shape:
            nx, ny = pos_x + dx, pos_y + dy

            if nx < 0 or nx >= 7:
                return False

            if ny <= 0:
                return False

            if (nx, ny) in chamber:
                return False

        return True

    for rock_idx in range(2022):
        # 1. Spawn rock
        current_rock = ROCKS[rock_idx % 5]
        x = 2
        y = top_y + 4

        while True:
            # 2. Jet push
            jet_dir = jet_pattern[jet_idx]
            jet_idx = (jet_idx + 1) % num_jets
            dx = dirs[jet_dir]

            if is_valid(current_rock, x + dx, y):
                x += dx

            # 3. Fall down
            if is_valid(current_rock, x, y - 1):
                y -= 1
            else:
                # Settle rock
                for dx, dy in current_rock:
                    nx, ny = x + dx, y + dy
                    chamber.add((nx, ny))
                    top_y = max(top_y, ny)
                break

    print(top_y)


if __name__ == "__main__":
    main()
