import csv
import itertools


KART_PENALTY = 0.58


def find_route(village, data):
    n = len(data)

    permutations = itertools.permutations(range(1, n))
    routes = {}
    for p in permutations:
        if p.index(1) < 3:
            continue

        p = (0,) + p
        path_length = 0
        for i in range(1, n):
            cost = data[p[i - 1]][p[i]]
            path_length += cost if cost > 0 else 1e99

        if village == "caveman" and p.index(2) < min([p.index(3), p.index(4)]):
            path_length += KART_PENALTY

        routes[path_length] = p

    return dict(sorted(routes.items(), key=lambda item: item[0]))


if __name__ == "__main__":
    villages = ["sailor", "cossack", "caveman", "inca"]
    for village in villages:
        try:
            with open(f"INPUTS/{village}.csv") as f:
                data = [list(map(float, row)) for row in csv.reader(f, delimiter=",")]
        except Exception as e:
            print(e)
            continue
        print(f"{village}: {list(find_route(village, data).items())[0:5]}")
