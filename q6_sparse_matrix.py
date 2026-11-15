"""
CCS 2214 - Task 3
Question 6: Represent a sparse matrix using arrays

Uses the triplet (row, column, value) representation: only non-zero
elements are stored. The first row of the triplet array holds the matrix
dimensions and the number of non-zero elements.
"""


def to_sparse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    sparse = [[rows, cols, 0]]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
    sparse[0][2] = len(sparse) - 1
    return sparse


def main():
    rows, cols = map(int, input("Enter number of rows and columns: ").split())
    print("Enter the matrix elements row by row:")
    matrix = [list(map(int, input().split())) for _ in range(rows)]

    sparse = to_sparse(matrix)

    print("\nSparse matrix (triplet representation):")
    print("Row\tCol\tValue")
    for r, c, v in sparse:
        print(f"{r}\t{c}\t{v}")


if __name__ == "__main__":
    main()
