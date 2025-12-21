import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    total = 0

    for line in data:
        number = 0

        for i, c in enumerate(reversed(line)):
            if c == '=':
                digit = -2
            elif c == '-':
                digit = -1
            else:
                digit = int(c)
            number += digit * (5**i)

        total += number

    snafu = []

    while total > 0:
        remainder = total % 5
        total //= 5

        if remainder <= 2:
            snafu.append(str(remainder))
        elif remainder == 3:
            snafu.append('=')
            total += 1
        elif remainder == 4:
            snafu.append('-')
            total += 1

    print(''.join(reversed(snafu)))


if __name__ == "__main__":
    main()
