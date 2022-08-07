def output(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(matrix[r][c], end=' ')
        print()


def input_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    for r in range(n):
        matrix[r] = input().split()
    return matrix


def transpose_matrix(matrix, n, m):
    n, m = m, n
    transp_matrix = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            transp_matrix[r][c] = matrix[c][r]
    return transp_matrix


def output_sqaure(matrix, n):
    for r in range(n):
        for c in range(n):
            print(matrix[r][c], end=' ')
        print()


def input_sqaure_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            matrix[r][c] = input()
    return matrix


def transpose_sqaure_matrix(matrix, n):
    transp_matrix = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            transp_matrix[r][c] = matrix[c][r]
    return transp_matrix


def matrix_trace(matrix, n):
    total = 0
    for r in range(n):
        total += int(matrix[r][r])
    return total


def turn_90_right(matrix, n):
    trans_matrix = transpose_matrix(matrix, n)
    res_matrix = [[0]*n for _ in range(n)]
    for r in range(n):
        res_matrix[r] = trans_matrix[r]
        res_matrix[r].reverse()
    return res_matrix


def mirror(matrix, n):  #отражение относительно цунтра по горизонтали
    temp_m = matrix.copy()
    for c in range(n):
        matrix[c] = temp_m[n - c - 1]
    return matrix


def magic_check(matrix, n):
    flag = False
    arr = []
    for r in range(n):
        for c in range(n):
            arr.append(matrix[c][r])
    arr.sort()
    if arr == [i for i in range(1, n ** 2 + 1)]:
        main_diag = matrix_trace(matrix, n)
        sub_diag = matrix_trace(turn_90_right(matrix, n), n)
        if sub_diag == main_diag:
            for i in range(n):
                if main_diag != sum(matrix[i]):
                    break
            else:
                temp_matrix = transpose_sqaure_matrix(matrix, n)
                for i in range(n):
                    if main_diag != sum(temp_matrix[i]):
                        break
                else:
                    flag = True
    return flag
