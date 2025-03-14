from quadratic_equation_solver import solve_quadratic_equation

def read_coefficients_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            coefficients = content.split()

            if len(coefficients) != 3:
                raise ValueError("invalid file format")

            a = float(coefficients[0])
            b = float(coefficients[1])
            c = float(coefficients[2])

            return a, b, c
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as e:
        print("invalid file format")
        return None

def noninteractive(file_path):

    coefficients = read_coefficients_from_file(file_path)

    if coefficients:
        a, b, c = coefficients
        solve_quadratic_equation(a, b, c)