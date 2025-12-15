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

    cache = {}
    target_rocks = 10**12
    added_height = 0
    rock_count = 0

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

    while rock_count < target_rocks:
        if added_height == 0 and rock_count > 2000:
            skyline = []
            for c in range(7):
                depth = 0
                while (c, top_y - depth) not in chamber and depth < 30:
                    depth += 1
                skyline.append(depth)
            skyline = tuple(skyline)

            state_key = (rock_count % 5, jet_idx, skyline)

            if state_key in cache:
                # Cycle detected
                prev_rock_count, prev_top_y = cache[state_key]

                cycle_length = rock_count - prev_rock_count
                cycle_height = top_y - prev_top_y

                remaining_rocks = target_rocks - rock_count
                num_cycles_to_skip = remaining_rocks // cycle_length

                added_height = num_cycles_to_skip * cycle_height
                rock_count += num_cycles_to_skip * cycle_length
            else:
                cache[state_key] = (rock_count, top_y)

        # --- Standard simulation step ---
        current_rock = ROCKS[rock_count % 5]
        x = 2
        y = top_y + 4

        while True:
            jet_dir = jet_pattern[jet_idx]
            jet_idx = (jet_idx + 1) % num_jets
            dx = dirs[jet_dir]

            if is_valid(current_rock, x + dx, y):
                x += dx

            if is_valid(current_rock, x, y - 1):
                y -= 1
            else:
                for dx, dy in current_rock:
                    nx, ny = x + dx, y + dy
                    chamber.add((nx, ny))
                    top_y = max(top_y, ny)
                break

        rock_count += 1

    print(top_y + added_height)


if __name__ == "__main__":
    main()
