def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return iterations, upper_bound

arr = [1.2, 2.5, 3.7, 4.1, 5.8, 6.3, 7.9]
target = 4.5

iterations, upper_bound = binary_search(arr, target)

print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)