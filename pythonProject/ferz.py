def output_sqaure(matrix, n):
    for r in range(n):
        for c in range(n):
            print(matrix[r][c], end=' ')
        print()


def input_sqaure_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            matrix[r][c] = abs(r - c)
    return matrix


def main():
    n = int(input())
    matrix = input_sqaure_matrix(n)
    output_sqaure(matrix, n)


if __name__ == "__main__":
    main()
