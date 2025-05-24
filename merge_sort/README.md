# *🧩 Merge Sort – Sortowanie przez scalanie* #
## **📜 Historia i kontekst** ##

Sortowanie przez scalanie (Merge Sort) to klasyczny przykład algorytmu dziel i zwyciężaj, zaproponowany przez Johna von Neumanna już w 1945 roku. Choć może być nieco bardziej złożony niż prostsze metody (jak sortowanie przez wstawianie), wyróżnia się gwarantowaną wydajnością i stabilnością działania nawet dla dużych zbiorów danych.

## **🧠 Idea algorytmu** ##

Algorytm dzieli tablicę na coraz mniejsze części (aż do pojedynczych elementów), po czym rekurencyjnie scala je z powrotem w sposób uporządkowany.

To jak układanie dwóch już posortowanych talii kart w jedną dużą, też posortowaną.

## **⚙️ Działanie krok po kroku** ##

Jeśli tablica ma więcej niż jeden element:

Podziel ją na dwie równe części.

Rekurencyjnie posortuj każdą z części (za pomocą Merge Sorta).

Scal dwie posortowane części w jedną uporządkowaną całość.

## **🧪 Kod źródłowy (Python)** ##
```python
# Funkcja sortująca tablicę za pomocą sortowania przez scalanie (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dzielenie tablicy na dwie połowy
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Scalanie dwóch posortowanych połówek
    return merge(left_half, right_half)

# Funkcja scalająca dwie posortowane listy
def merge(left, right):
    merged = []
    i = j = 0

    # Porównywanie elementów z lewej i prawej części
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

# Przykładowe użycie
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
```

## **📊 Złożoność obliczeniowa** ##

| Przypadek | Złożoność czasowa                    |
| --------- | ------------------------------------ |
| Najlepszy | O(n log n)                           |
| Średni    | O(n log n)                           |
| Najgorszy | O(n log n)                           |
| Pamięć    | O(n) – dodatkowe miejsce na scalanie |

## **⚒️ Zastosowania i modyfikacje** ##

Sprawdza się doskonale w pracy z dużymi zbiorami danych.

Często wykorzystywany w zewnętrznym sortowaniu (np. na dysku), gdzie dane nie mieszczą się w pamięci RAM.

Może być bazą dla hybrydowych algorytmów (np. Timsort).

## **🧬 Cechy charakterystyczne** ##

Stabilny algorytm – zachowuje kolejność równych elementów.

Nie działa w miejscu (non-in-place) – wymaga dodatkowej pamięci.

Rekurencyjna struktura – elegancka, ale może prowadzić do głębokich wywołań rekurencyjnych.

Deterministyczna wydajność – zawsze O(n log n), niezależnie od danych wejściowych.

## **🤔 Ciekawostki** ##

Merge Sort był jednym z pierwszych algorytmów sortujących, które wykorzystywały rekurencję i podejście dziel i zwyciężaj.

Jest popularnym wyborem w systemach, gdzie wymagana jest wysoka stabilność i przewidywalność działania.

Często pojawia się w wywiadach technicznych jako przykład optymalnego sortowania.

## **🧠 Podsumowanie** ##

Merge Sort to potężne narzędzie w świecie algorytmów sortowania – wydajne, stabilne i niezawodne. Choć może wymagać więcej pamięci niż inne metody, jego niezależność od danych wejściowych czyni go idealnym wyborem w wielu zastosowaniach praktycznych i teoretycznych.
