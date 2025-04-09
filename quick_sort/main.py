# Funkcja wykonująca sortowanie szybkie (QuickSort) na tablicy 'arr' w zakresie indeksów od 'left' do 'right'
def quicksort(arr, left, right):
    # Sprawdzenie, czy zakres zawiera więcej niż jeden element
    if left < right:
        # Podział tablicy - znalezienie indeksu elementu pivot po podziale
        partition_pos = partition(arr, left, right)

        # Rekurencyjne wywołanie quicksorta dla lewej części tablicy (przed pivotem)
        quicksort(arr, left, partition_pos - 1)

        # Rekurencyjne wywołanie quicksorta dla prawej części tablicy (po pivocie)
        quicksort(arr, partition_pos + 1, right)

# Funkcja dokonująca podziału tablicy względem pivota
def partition(arr, left, right):
    i = left  # wskaźnik od lewej strony
    j = right - 1  # wskaźnik od prawej strony (jeden element przed pivotem)
    pivot = arr[right]  # pivot to ostatni element w danym zakresie

    # Pętla wykonuje się, dopóki wskaźnik i nie przetnie się z j
    while i < j:
        # Przesuwanie wskaźnika i w prawo, dopóki elementy są mniejsze niż pivot
        while i < right and arr[i] < pivot:
            i += 1
        # Przesuwanie wskaźnika j w lewo, dopóki elementy są większe lub równe pivotowi
        while j > left and arr[j] >= pivot:
            j -= 1

        # Jeśli wskaźniki się nie minęły, zamień elementy miejscami
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Na koniec, jeśli aktualny element wskazywany przez i jest większy niż pivot,
    # zamień go z pivotem, aby pivot znalazł się w odpowiednim miejscu
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    # Zwróć nową pozycję pivota
    return i

# Przykładowa tablica do posortowania
arr = [22, 11, 88, 66, 55, 77, 33, 44]

# Wywołanie funkcji quicksort dla całej tablicy
quicksort(arr, 0, len(arr) - 1)

# Wyświetlenie posortowanej tablicy
print(arr)
