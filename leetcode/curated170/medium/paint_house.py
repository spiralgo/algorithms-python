import random

def minCost(costs: list[list[int]]) -> int:
        red, blue, green = 0,0,0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g
        return min(red, blue, green)

if __name__ == "__main__":
    costs = []
    for _ in range(20):
        l = []
        l.append(random.randint(1,20))
        l.append(random.randint(1,20))
        l.append(random.randint(1,20))
        costs.append(l)
    print(costs)
    print(minCost(costs))

