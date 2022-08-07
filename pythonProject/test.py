def init_matrix(n, m):
    matrix = [[0]*m for _ in range(n)]
    k = 1
    for r in range(0, n):
        for c in range(0, m):
            matrix[r][c] = str(k)
            k += 1
        if r % 2 == 1:
            matrix[r].reverse()
    return matrix


def output(matrix, n, m):
    for r in range(n):
        for c in range(m):
            print(matrix[r][c].ljust(3), end=' ')
        print()


def main():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    matrix = init_matrix(n, m)
    output(matrix, n, m)


if __name__ == "__main__":
    main()
