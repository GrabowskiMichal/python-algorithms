# Funkcja sortująca tablicę za pomocą sortowania przez wstawianie (Insertion Sort)
def insertion_sort(arr):
    # Przechodzimy przez całą tablicę, zaczynając od drugiego elementu
    for i in range(1, len(arr)):
        key = arr[i]      # Element do wstawienia
        j = i - 1

        # Przesuwamy elementy większe od 'key' o jedno miejsce w prawo
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Wstawiamy 'key' w odpowiednie miejsce
        arr[j + 1] = key

# Przykładowa tablica do posortowania
arr = [22, 11, 88, 66, 55, 77, 33, 44]

# Wywołanie funkcji sortującej
insertion_sort(arr)

# Wyświetlenie posortowanej tablicy
print(arr)
