def recursive(depth, start, path):
    if depth == 6:
        print(*path)
        return
    for i in range(start, len(lis)):
        if lis[i] not in path and path[-1] <= lis[i]:
            path.append(lis[i])
            recursive(depth+1, start, path)
            path.pop()



while True:
    inp = list(map(int, input().split(" ")))

    if inp[0] == 0:
        break

    n, lis = inp[0], inp[1:]

    for start in range(len(lis) - 6 + 1):
        recursive(1, start,[lis[start]])
    print()