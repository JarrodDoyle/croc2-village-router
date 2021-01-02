import csv
import itertools


def find_route(village, data):
    n = len(data)

    permutations = itertools.permutations(range(1, n))
    routes = {}
    for permutation in permutations:
        if permutation.index(1) < 3:
            continue

        permutation = (0,) + permutation
        path_length = 0
        for i in range(1, n):
            cost = data[permutation[i - 1]][permutation[i]]
            path_length += cost if cost > 0 else 1e99

        routes[path_length] = permutation

    shortest_path_length = min(routes.keys())
    shortest_path = routes[shortest_path_length]
    return (shortest_path_length, shortest_path)


if __name__ == "__main__":
    villages = ["sailor", "cossack", "caveman", "inca"]
    for village in villages:
        try:
            with open(f"INPUTS/{village}.csv") as f:
                data = list(csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC))
        except:
            print(f"No {village}.csv found")
            continue
        print(f"{village}: {find_route(village, data)}")
