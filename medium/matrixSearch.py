def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    left = 0
    right = len(matrix) - 1
    row = 0
    while left <= right:
        mid = (left + right) // 2
        # if matrix[row][col] == target:
        #     return True
        n = len(matrix[mid]) - 1
        if matrix[mid][0] > target and matrix[mid][n] > target:
            right = mid - 1
        elif matrix[mid][0] < target and matrix[mid][n] < target:
            left = mid + 1
        else:
            row = mid
            break

    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        if matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
# target = 10


# matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
# target = 15


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(searchMatrix(matrix, target))
