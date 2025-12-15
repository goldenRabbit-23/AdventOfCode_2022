import sys
import re
from collections import defaultdict
from functools import cache


def main():
    data = open(sys.argv[1]).read().splitlines()
    valves = {}
    tunnels = {}

    for line in data:
        parts = re.match(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        valve = parts.group(1)
        flow = int(parts.group(2))
        leads = [x for x in parts.group(3).split(', ')]

        valves[valve] = flow
        tunnels[valve] = leads

    dists = defaultdict(lambda: float('inf'))

    for valve, neighbors in tunnels.items():
        dists[valve, valve] = 0
        for neighbor in neighbors:
            dists[valve, neighbor] = 1

    all_valves = list(valves.keys())
    for k in all_valves:
        for i in all_valves:
            for j in all_valves:
                dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])

    flow_valves = [v for v in valves.keys() if valves[v] > 0]
    valve_to_bit = {v: i for i, v in enumerate(flow_valves)}

    @cache
    def dfs(valve, time, mask):
        max_pressure = 0

        for neighbor in flow_valves:
            bit = 1 << valve_to_bit[neighbor]

            if not (mask & bit):
                dist = dists[valve, neighbor]
                remaining = time - dist - 1

                if remaining > 0:
                    pressure = (remaining * valves[neighbor]) + dfs(neighbor, remaining, mask | bit)
                    max_pressure = max(max_pressure, pressure)

        return max_pressure

    print(dfs('AA', 30, 0))


if __name__ == "__main__":
    main()
