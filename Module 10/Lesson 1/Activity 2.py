def linear_search(items, target):
    """Return (index of target or -1, number of checks made.)"""
    checks = 0
    for i in range(len(items)):
        checks = checks + 1
        if items[i] == target:
            return i, checks
    return -1, checks

scores = [3, 7, 2, 9, 4, 1, 8, 5, 6]
n = len(scores)
print("List:", scores, "  n =", n)
all_checks = []
for target in scores:
    index, checks = linear_search(scores, target)
    all_checks.append(checks)
    print(f"    search{target}: found at index {index} after {checks} check(s)")
missing = int(input("Pick a number that is not in the list."))
index, missing_checks = linear_search(scores, missing)
print(f"    search {missing}: index {index} (not in the list) after {missing_checks} checks")
print()
print("Best case :", min(all_checks), "check    (target is first)       -> Theta(1)")
print("Worst case:", max(all_checks + [missing_checks]), "checks    (target last or missing)        -> Theta(n)")
average = sum(all_checks) / n
print("Average  :", average, "checks    (every position equally likely) = (n + 1) / 2 =", (n + 1) / 2)
print("For every input: at most n checks -> O(n); atleast 1 check -> Omega(1).")      



