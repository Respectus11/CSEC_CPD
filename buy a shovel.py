def minimum_shovels(k, r):
    for n in range(1, 10):
        cost = n * k
        if cost % 10 == 0 or cost % 10 == r:
            return n
    return 10
k, r = map(int, input().split())
print(minimum_shovels(k, r))

  
