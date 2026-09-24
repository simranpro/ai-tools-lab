.github/workflows/python-package.yml
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

bubble_sort(arr)

print("Sorted array:", arr)
