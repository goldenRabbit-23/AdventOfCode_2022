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

    print(yell("root"))


if __name__ == "__main__":
    main()
