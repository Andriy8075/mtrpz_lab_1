from quadratic_equation_solver import solve_quadratic_equation

def validate_input(prompt):
    try:
        replaced_commas = prompt.replace(',', '.')
        return float(replaced_commas)
    except ValueError:
        print(f"Error. Expected a valid real number, got \"{prompt}\" instead")
        exit(1)

def interactive():
    a = validate_input(input("a = "))
    if a == 0:
        print("a can not be 0")
        return
    b = validate_input(input("b = "))
    c = validate_input(input("c = "))

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    solve_quadratic_equation(a, b, c)
