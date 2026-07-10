def descending(n):
    if n == 0:
        return

    print(n)
    descending(n-1)

descending(5)

def ascending(n):
    if n == 6:
        return

    print(n)
    ascending(n+1)

ascending(1)

def ascending1(n):
    if n == 0:
        return

    ascending1(n - 1)
    print(n)

ascending1(5)