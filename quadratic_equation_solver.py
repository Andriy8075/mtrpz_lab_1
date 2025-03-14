import math

def solve_quadratic_equation(a, b, c):
    if a == 0:
        print("a can not be 0")

    D = b*b - 4*a*c

    if D < 0:
        print("There are 0 roots")
    elif D == 0:
        x = -b/(2*a)
        print(f"There are 1 roots:\nx1 = {x}")
    else:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(f'There are 2 roots:\nx1 = {x1}\nx2 = {x2}')