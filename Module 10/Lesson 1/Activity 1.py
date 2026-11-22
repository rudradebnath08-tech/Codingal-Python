def first_middle_last(scores):
    """Read three scores: 3 operations, whatever n is."""
    if len(scores) == 0:
        return None, 0
    picks = [scores[0], scores[len(scores) // 2], scores[-1]]
    steps = 3
    return picks, steps


def sum_biggest_average(scores):
    """2 set-up operations, 2 per score, 1 at the end: 2n + 3 operations."""
    if len(scores) == 0:
        return None, 0
    total = 0
    biggest = scores[0]
    steps = 2
    for score in scores:
        total = total + score
        if score > biggest:
            biggest = score
        steps = steps + 2
    average = total / len(scores)
    steps = steps + 1
    return average, steps

def compare_with_earlier(scores):
    """Compare each score with itself and every score before it: n(n + 1)/2 operation."""
    not_bigger = 0
    steps = 0
    for i in range(len(scores)):
        for j in range(i + 1):
            if scores[j] <= scores[i]:
                not_bigger = not_bigger + 1
            steps = steps + 1
    return not_bigger, steps

print("     n |  0(1): steps    /1 |    0(n): steps     /n |    0(n^2): steps       /n^2")
for n in [10, 100, 1000, 2000]:
    scores = list(range(1, n + 1))
    o1_steps = first_middle_last(scores)[1]
    on_steps = sum_biggest_average(scores)[1]
    on2_steps = compare_with_earlier(scores)[1]
    ratio_o1 = o1_steps / 1
    ratio_on = on_steps / n
    ratio_on2 = on2_steps / (n * n)
    print(f"{n:>6} | {o1_steps:>11} | {ratio_o1:>4.0f} | {on_steps:>11} {ratio_on:>:>6.3f} | {on2_steps:>13} {ratio_on2:>8.4f}")
print()
print("Exact count: 3, 2n + 3 and n(n + 1)/2 = n^2/2 + n/2.")
print("Divided by the dominant term (1, n, n^2) they settle to 3, 2 and 0.5.")
print("drop the constant and smaller terms -> 0(1), O(n), O(n^2).")