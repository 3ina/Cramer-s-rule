import numpy as np


def print_intro():
    print("""
          ______ .______          ___      .___  ___.  _______ .______      __     _______.   .______       __    __   __       _______ 
         /      ||   _  \        /   \     |   \/   | |   ____||   _  \    (_ )   /       |   |   _  \     |  |  |  | |  |     |   ____|
        |  ,----'|  |_)  |      /  ^  \    |  \  /  | |  |__   |  |_)  |    |/   |   (----`   |  |_)  |    |  |  |  | |  |     |  |__   
        |  |     |      /      /  /_\  \   |  |\/|  | |   __|  |      /           \   \       |      /     |  |  |  | |  |     |   __|  
        |  `----.|  |\  \----./  _____  \  |  |  |  | |  |____ |  |\  \----.  .----)   |      |  |\  \----.|  `--'  | |  `----.|  |____ 
         \______|| _| `._____/__/     \__\ |__|  |__| |_______|| _| `._____|  |_______/       | _| `._____| \______/  |_______||_______|

                                                                                                    made by SinaRoydel
          """)

    print("""
           a1X + b1Y + ... + c1Z = N1
           a1X + b2Y + ... + c2Z = N2
           .
           .
           anX + bnY + ... + cnZ = Nn
       """)
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_coefficient_matrix(R):
    input_matrix = []
    print("Enter the coefficients row-wise:")
    for i in range(R):
        row = []
        for j in range(R):
            row.append(get_float_input(f"Enter coefficient for equation {i + 1}, variable {j + 1}: "))
        input_matrix.append(row)
    return np.matrix(input_matrix)


def solve_equations(matrix, NxN):
    results = []
    det_A = np.linalg.det(matrix)
    if det_A == 0:
        print("The coefficient matrix is singular. The system may have no solution or infinite solutions.")
        return results
    for i in range(len(NxN)):
        A1_matrix = matrix.copy()
        A1_matrix[:, i] = np.reshape(NxN, (-1, 1))
        det_A1 = np.linalg.det(A1_matrix)
        result = det_A1 / det_A
        results.append(result)
    return results


def main():
    print_intro()
    is_continue = True
    while is_continue:
        R = get_integer_input("Enter the number of equations: ")
        coefficient_matrix = get_coefficient_matrix(R)
        print("Coefficient Matrix (A):")
        print(coefficient_matrix)

        NxN = []
        for i in range(R):
            NxN.append(get_float_input(f"Enter N{i + 1}: "))

        results = solve_equations(coefficient_matrix, NxN)
        for i, result in enumerate(results):
            print(f"X{i + 1} = {result:.2f}")

        while True:
            continue_prog = input("Do you want to continue? 'y' or 'n': ").lower()
            if continue_prog == 'y':
                break
            elif continue_prog == 'n':
                is_continue = False
                break
            else:
                print("Please enter 'y' or 'n.'")


if __name__ == "__main__":
    main()