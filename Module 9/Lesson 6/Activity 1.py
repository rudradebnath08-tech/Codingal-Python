def sum_formula(n):
    """Plan: use the formula n * (n + 1) // 2. No Loop."""
    total = n * (n + 1) // 2
    steps = 1
    return total, steps

def sum_loop(n):
    """Plan: add each student's points, one student at a time."""
    total = 0
    steps = 0
    for student in range(1, n + 1):
        total = total + student
        steps = steps + 1
    return total, steps

def sum_double_loop(n):
    """Plan: count every single point, one point at a time(a loop inside a loop)"""
    total = 0
    steps = 0
    for student in range(1, n + 1):
        for point in range(1, student + 1):
            total = total + 1
            steps = steps + 1
    return total, steps

n = int(input("How many students are in the contest?"))
print("Contest with n =", n, "students (student k earns k points)")
print()
total, steps = sum_formula(n)
print("Formula      : total =", total, "    steps =", steps)
total, steps = sum_loop(n)
print("Loop         : total =", total, "    steps =", steps)
total, steps = sum_double_loop(n)
print("Double Loop  : total =", total, "    steps =", steps)
print()
print("Same total, different number of steps.")


    