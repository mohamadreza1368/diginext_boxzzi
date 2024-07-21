def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
   
    rows = len(matrix)
    cols = len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
   
    return False



a = [[1, 3, 5], [7, 8, 10], [12, 15, 18]]
b = 60
result = search_matrix(a, b)
print(result)