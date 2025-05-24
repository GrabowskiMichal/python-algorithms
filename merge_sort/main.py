def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Podział listy na dwie połowy
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Scalanie posortowanych połówek
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Porównywanie elementów i scalanie w posortowaną listę
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Dodanie pozostałych elementów z lewej i prawej listy
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Przykład użycia
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Posortowana tablica:", sorted_arr)
