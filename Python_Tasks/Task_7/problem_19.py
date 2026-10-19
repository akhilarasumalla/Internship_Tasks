def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    count = 0

    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch

        weights.add((ord(ch) - ord('a') + 1) * count)

    return ["Yes" if q in weights else "No" for q in queries]


if __name__ == '__main__':
    s = input().strip()
    queries_count = int(input().strip())

    queries = []
    for _ in range(queries_count):
        queries.append(int(input().strip()))

    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
