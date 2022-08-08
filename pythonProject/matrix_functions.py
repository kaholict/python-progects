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


def transpose_sqaure_matrix(matrix, n):
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


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


def spiral_matrix(n, m):
    matrix = [[0]*m for _ in range(n)]
    s = m * n
    k = 0
    if n == m and n % 2 == 1:
        matrix[n // 2][m // 2] = s
    if m == 1:
        for r in range(n):
            k += 1
            matrix[r][0] = k
    elif n == 1:
        for c in range(m):
            k += 1
            matrix[0][c] = k
    else:
        while k < s and m > 0:
            if k == 0:
                r_start = 0
                c_start = 0
                r_end = n - 1
                c_end = m - 1
            for c in range(c_start, c_end):
                k += 1
                matrix[r_start][c] = k
            for r in range(r_start, r_end):
                k += 1
                matrix[r][c_end] = k
            for c in range(c_end, c_start, -1):
                k += 1
                matrix[r_end][c] = k
            for r in range(r_end, r_start, -1):
                k += 1
                matrix[r][c_start] = k
            m -= 2
            n -= 2
            if m > 0:
                c_start += 1
                c_end -= 1
            if n > 0:
                r_start += 1
                r_end -= 1
    return matrix


def create_snow_matrix(n):
    matrix = [['.']*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if r == c or r == n - c - 1 or c == n // 2 or r == n // 2:
                matrix[r][c] = '*'
    return matrix


def check_symmetry(matrix, n):
    flag = True
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != matrix[c][r]:
                flag = False
                break
        if not flag:
            break
    return flag
