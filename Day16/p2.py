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
    path_scores = defaultdict(int)

    @cache
    def dfs(valve, time, mask, pressure):
        path_scores[mask] = max(path_scores[mask], pressure)

        for neighbor in flow_valves:
            bit = 1 << valve_to_bit[neighbor]

            if not (mask & bit):
                dist = dists[valve, neighbor]
                remaining = time - dist - 1

                if remaining > 0:
                    dfs(
                        neighbor,
                        remaining,
                        mask | bit,
                        pressure + (remaining * valves[neighbor]),
                    )

    dfs('AA', 26, 0, 0)

    best = 0

    for mask1, score1 in path_scores.items():
        for mask2, score2 in path_scores.items():
            if mask1 & mask2 == 0:
                best = max(best, score1 + score2)

    print(best)


if __name__ == "__main__":
    main()
