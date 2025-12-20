import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    monkeys = {}

    for line in data:
        name, job = line.split(": ")
        monkeys[name] = int(job) if job.isdigit() else job.split(" ")

    def yell(name):
        job = monkeys[name]

        if isinstance(job, int):
            return job

        left_monkey, op, right_monkey = job
        left, right = yell(left_monkey), yell(right_monkey)
        return {"+": left + right, "-": left - right, "*": left * right, "/": left // right}[op]

    def has_humn(name):
        if name == "humn":
            return True

        job = monkeys[name]

        if isinstance(job, int):
            return False

        left, _, right = job
        return has_humn(left) or has_humn(right)

    def solve(name, target):
        if name == "humn":
            return target

        left_monkey, op, right_monkey = monkeys[name]

        if has_humn(left_monkey):
            right = yell(right_monkey)
            new_target = {"+": target - right, "-": target + right, "*": target // right, "/": target * right}[op]
            return solve(left_monkey, new_target)
        else:
            left = yell(left_monkey)
            new_target = {"+": target - left, "-": left - target, "*": target // left, "/": left // target}[op]
            return solve(right_monkey, new_target)

    root_left, _, root_right = monkeys["root"]
    print(solve(root_left, yell(root_right))
          if has_humn(root_left)
          else solve(root_right, yell(root_left)))


if __name__ == "__main__":
    main()
