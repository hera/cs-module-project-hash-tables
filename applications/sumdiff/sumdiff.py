"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = (1, 3, 4, 7, 12)
# q = tuple(range(1, 10))
# q = tuple(range(1, 200))

def sumdiff(q):
    def f(x):
        return x * 4 + 6

    converted = [f(x) for x in q]

    # [(sum, index_1, index_2), ...]
    sums = []

    # [(diff, index_1, index_2), ...]
    diffs = []

    for i in range(len(converted)):
        for j in range(len(converted)):
            sums.append((converted[i] + converted[j], i, j))

    for i in range(len(converted)):
        for j in range(len(converted)):
            diffs.append((converted[i] - converted[j], i, j))

    for s in sums:
        for d in diffs:
            if s[0] == d[0]:
                left_part = "f(%d) + f(%d) = f(%d) - f(%d)" % (q[s[1]], q[s[2]], q[d[1]], q[d[2]])
                right_part = "%d + %d = %d - %d" % (converted[s[1]], converted[s[2]], converted[d[1]], converted[d[2]])
                
                print(left_part + "\t" + right_part)


if __name__ == "__main__":
    sumdiff(q)