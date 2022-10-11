def firstBadVersion(n):
    m = n // 2
    l = 0
    r = n

    while l != m:
        if isBadVersion(m) == 0:
            l = m
            m = (l + r) // 2
        else:
            r = m
            m = (l + r) // 2

    return (m + 1)
