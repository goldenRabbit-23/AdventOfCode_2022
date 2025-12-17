import sys
import re


def main():
    data = open(sys.argv[1]).read().splitlines()
    total_quality_level = 0

    for line in data:
        # ID, OreCost, ClayCost, ObsCost(Ore, Clay), GeoCost(Ore, Obs)
        bp, a, b, c, d, e, f = list(map(int, re.findall(r'\d+', line)))

        costs = [
            (a, 0, 0),  # Ore robot
            (b, 0, 0),  # Clay robot
            (c, d, 0),  # Obsidian robot
            (e, 0, f),  # Geode robot
        ]

        max_bots = [max(a, b, c, e), d, f, float('inf')]
        max_geodes = 0

        def dfs(time, bots, resources):
            nonlocal max_geodes

            # 1. Pruning
            potential = resources[3] + bots[3] * time + (time * (time - 1) // 2)
            if potential <= max_geodes:
                return

            max_geodes = max(max_geodes, resources[3] + bots[3] * time)

            # 2. Try building each type of robot
            for i in range(3, -1, -1):
                ore_cost, clay_cost, obs_cost = costs[i]

                # Resource saturation check
                if bots[i] >= max_bots[i]:
                    continue

                # Resource availability check
                if (ore_cost > 0 and bots[0] == 0) or (clay_cost > 0 and bots[1] == 0) or (obs_cost > 0 and bots[2] == 0):
                    continue

                ore_wait = max(0, (ore_cost - resources[0] + bots[0] - 1) // bots[0]) if ore_cost > resources[0] else 0
                clay_wait = max(0, (clay_cost - resources[1] + bots[1] - 1) // bots[1]) if clay_cost > resources[1] else 0
                obs_wait = max(0, (obs_cost - resources[2] + bots[2] - 1) // bots[2]) if obs_cost > resources[2] else 0

                wait = max(ore_wait, clay_wait, obs_wait)
                rem_time = time - wait - 1

                if rem_time <= 0:
                    continue

                dfs(
                    rem_time,
                    tuple(b + 1 if x == i else b for x, b in enumerate(bots)),
                    (
                        resources[0] + bots[0] * (wait + 1) - ore_cost,
                        resources[1] + bots[1] * (wait + 1) - clay_cost,
                        resources[2] + bots[2] * (wait + 1) - obs_cost,
                        resources[3] + bots[3] * (wait + 1)
                    )
                )

        dfs(24, (1, 0, 0, 0), (0, 0, 0, 0))
        total_quality_level += bp * max_geodes

    print(total_quality_level)


if __name__ == "__main__":
    main()
