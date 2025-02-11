def probability(Y, W):
    max_roll = max(Y, W)
    favorable_outcomes = 6 - max_roll + 1
    fractions = {1: "1/6", 2: "1/3", 3: "1/2", 4: "2/3", 5: "5/6", 6: "1/1"}
    return fractions[favorable_outcomes]
Y, W = map(int, input().split())
print(probability(Y, W))
