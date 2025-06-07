# Funkcja sortująca tablicę za pomocą sortowania bąbelkowego (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Ostatnie i elementów jest już na właściwym miejscu
        for j in range(0, n - i - 1):
            # Zamiana miejscami, jeśli element jest większy od następnego
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Przykład użycia Bubble Sort
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print(array)
