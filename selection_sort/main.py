# Funkcja wykonująca sortowanie przez wybór (Selection Sort) na tablicy 'arr'
def selection_sort(arr):
    n = len(arr)  # długość tablicy

    # Przechodzimy przez każdy element tablicy
    for i in range(n):
        min_index = i  # zakładamy, że bieżący indeks to najmniejszy

        # Szukamy najmniejszego elementu w pozostałej (nieposortowanej) części tablicy
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # aktualizacja indeksu najmniejszego elementu

        # Zamieniamy miejscami bieżący element z najmniejszym znalezionym
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Przykładowa tablica do posortowania
arr = [22, 11, 88, 66, 55, 77, 33, 44]

# Wywołanie funkcji selection_sort dla całej tablicy
selection_sort(arr)

# Wyświetlenie posortowanej tablicy
print(arr)
