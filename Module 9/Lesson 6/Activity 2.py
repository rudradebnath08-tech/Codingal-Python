def formula_steps(n):
    total = n * (n + 1) // 2
    return 1

def loop_steps(n):
    total, steps = 0, 0
    for students in range(1, n + 1):
        total = total + students
        steps = steps + 1
    return steps

def double_loop_steps(n):
    total, steps = 0, 0
    for students in range(1, n + 1):
        for point in range(1, students + 1):
            total = total + 1
            steps = steps + 1
    return steps

print("     n   Formula     Loop        Double Loop")
for n in[4, 10, 100, 1000, 2000]:
    formula_count = formula_steps(n)
    loop_count = loop_steps(n)
    double_loop_count = double_loop_steps(n)
    print(f"{n:>6} {formula_count:>9} {loop_count:>9} {double_loop_count:>13}")
print()
print("n doubles from 1000 to 2000. How many times more steps?")
print("     Formula     x", formula_steps(2000) / formula_steps(1000))
print("     Loop        x", loop_steps(2000) / loop_steps(1000))
print("     Double Loop x", round(double_loop_steps(2000) / double_loop_steps(1000), 2))

