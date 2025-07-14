def diagonalDifference(arr):
    n = len(arr)
    First_diagonal = 0  #left to right
    Second_diagonal = 0 # right to left
    for i in range(n):
        First_diagonal += arr[i][i]
        Second_diagonal += arr[i][n - 1 -i]
    return abs(First_diagonal - Second_diagonal)
    # Write your code here

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(diagonalDifference(arr))