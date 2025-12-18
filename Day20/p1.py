import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    numbers = [int(x) for x in data]
    mixed = list(enumerate(numbers))
    n = len(mixed)

    for original_idx in range(n):
        for i in range(n):
            if mixed[i][0] == original_idx:
                current_idx = i
                val = mixed[i][1]
                break

        mixed.pop(current_idx)
        new_idx = (current_idx + val) % (n - 1)
        mixed.insert(new_idx, (original_idx, val))

    zero_idx = next(i for i, (_, v) in enumerate(mixed) if v == 0)

    n1 = mixed[(zero_idx + 1000) % n][1]
    n2 = mixed[(zero_idx + 2000) % n][1]
    n3 = mixed[(zero_idx + 3000) % n][1]

    print(n1 + n2 + n3)


if __name__ == "__main__":
    main()
