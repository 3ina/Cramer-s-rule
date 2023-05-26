import numpy

print("""

  ______ .______          ___      .___  ___.  _______ .______      __     _______.   .______       __    __   __       _______ 
 /      ||   _  \        /   \     |   \/   | |   ____||   _  \    (_ )   /       |   |   _  \     |  |  |  | |  |     |   ____|
|  ,----'|  |_)  |      /  ^  \    |  \  /  | |  |__   |  |_)  |    |/   |   (----`   |  |_)  |    |  |  |  | |  |     |  |__   
|  |     |      /      /  /_\  \   |  |\/|  | |   __|  |      /           \   \       |      /     |  |  |  | |  |     |   __|  
|  `----.|  |\  \----./  _____  \  |  |  |  | |  |____ |  |\  \----.  .----)   |      |  |\  \----.|  `--'  | |  `----.|  |____ 
 \______|| _| `._____/__/     \__\ |__|  |__| |_______|| _| `._____|  |_______/       | _| `._____| \______/  |_______||_______|
                                                                                                                                
                                                                                            made by SinaRoydel

""")


def change_col(matrix, col_n, value_list):
    matrix_res = matrix.copy()
    for i in range(len(value_list)):
             matrix_res[i,col_n] = value_list[i]

    return matrix_res

is_continue = True

while is_continue:
    print("""
        a1X + b1Y + ... + c1Z = N1
        a1X + b2Y + ... + c2Z = N2
        .
        .
        anX + bnY + ... + cnZ = Nn
    """)
    flag = True
    while flag:
        try:
            R = int(input("Enter the number of equations :"))
            flag = False
        except:
            print("please inter number")

    input_matrix = []
    print("Enter the entries Coefficients rowwise:")

    for i in range(R):
        a = []
        for j in range(R):
            a.append(float(input()))
        input_matrix.append(a)

    matrix = numpy.matrix(input_matrix)
    print(matrix)
    print("Enter the entries N1 , N2 , N3 ... , Nn:")
    NxN = []
    for i in range(R):
        NxN.append(float(input()))

    for i in range(R):
        matrix = numpy.matrix(input_matrix)
        dat_A = numpy.linalg.det(matrix)
        A1_matrix = change_col(matrix,i,NxN)
        dat_A1 = numpy.linalg.det(A1_matrix)
        try:
            print("A"+str(i)+" : "+str(round(dat_A1/dat_A,2)))
        except ZeroDivisionError:
            print("The equation has no answer")


    while True:
        continue_prog = input("Do you want to continue? 'y' or 'n' : ").lower()
        if continue_prog == 'y':
            break
        elif continue_prog == 'n':
            is_continue = False
            break
        else:
            print("please inter 'y' or 'n'")




















