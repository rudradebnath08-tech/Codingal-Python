def linear_search(items, target):
    """Check items one by one from left (the method from the last lesson)."""
    checks = 0
    for i in range(len(items)):
        checks = checks + 1
        if items[i] == target:
            return i, checks
    return -1, checks

def report(checks, low, mid, high, value):
    """Print one round of binary search."""
    print(" check", checks, ":  low =", low, "  mid =", mid, "  high =", high, "    value =", value)

def binary_search(items, target, show=False):
    """Return (index of target or -1, number of checks). Items must be sorted."""
    low = 0
    high = len(items) - 1
    checks = 0
    while low <= high:
        mid = (low + high) // 2
        checks = checks + 1
        if show:
            report(checks, low, mid, high, items[mid])
        if items[mid] == target:
            return mid, checks
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, checks

scores = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print("Sorted list:", scores, " n = ", len(scores))
present = int(input("Search for a number that IS in the lists: "))
absent = int(input("Search for a number that is NOT in the lists: "))
for target in [present, absent]:
    print()
    print("Binary search for", target)
    index, checks = binary_search(scores, target, True)
    if index == -1:
        print(f"Result: {target} is not in the list {checks} checks")
    else:
        print(f"Result {target} found at index {index} ({checks} checks)")

print()
print("target | linear checks | binar checks")
for target in [1, 9, 17, 4]:
    print(f"{target:>6} | {linear_search(scores, target)[1]:>13} | {binary_search(scores, target)[1]:>13}")

print()
print("Worse case: search for a number bigger than every item.")
for n in [9, 100, 1000, 1000000]:
    items = list(range(n))
    checks = binary_search(items, n)[1]
    print(f"    n = {n:>9,}     binary search checks = {checks}")
