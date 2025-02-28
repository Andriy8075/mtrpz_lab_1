import math

a = 1
b = 12
c = 36

def solve_quadratic_equation(a, b, c):
    if a == 0:
        print("a can not be 0")

    D = b*b - 4*a*c

    if D < 0:
        print("No solution")
    elif D == 0:
        x = -b/(2*a)
        print(f"1 solution:\n{x}")
    else:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(f'2 solutions:\n{x1}, {x2}')

solve_quadratic_equation(a, b, c)