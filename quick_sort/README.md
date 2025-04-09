# **🔍 Czym jest Quick Sort?** #
Quick Sort, czyli szybkie sortowanie, to rekurencyjny algorytm sortowania, który działa w oparciu o zasadę dziel i zwyciężaj (ang. divide and conquer). Jest to jeden z najszybszych i najczęściej używanych algorytmów sortujących w praktyce.

## **📜 Historia algorytmu** ##
Quick Sort został wynaleziony w 1960 roku przez Tony'ego Hoare'a, który pracował wtedy nad automatycznym tłumaczeniem w Związku Radzieckim. Potrzebował szybkiego sposobu na sortowanie słów – i tak powstał Quick Sort.

Tony Hoare sam mówił, że nie spodziewał się, iż jego algorytm zyska taką popularność. Co ciekawe, nie miał wtedy dostępu do komputera – cały algorytm opracował na papierze.

## **🧠 Jak działa Quick Sort – krok po kroku** ##
Wybierz element zwany pivotem (element odniesienia).

Podziel tablicę na dwie części:

elementy mniejsze od pivota,

elementy większe od pivota.

Rekurencyjnie sortuj obie części.

Scal wszystko w jedną całość.

Przykład (intuicyjnie):
Mamy listę: [7, 2, 1, 6, 8, 5, 3, 4]

Pivot = 4

Dzielimy:

mniejsze: [2, 1, 3]

większe: [7, 6, 8, 5]

Rekurencyjnie sortujemy mniejsze i większe.

Sklejamy: sort(mniejsze) + [pivot] + sort(większe)

## **🧾 Kod Quick Sort w Pythonie** ##

```python
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
```

## **📊 Złożoność obliczeniowa** ##

| Rodzaj przypadku                                     | Złożoność czasowa  |
|------------------------------------------------------|--------------------|
| Najlepszy (pivot dzieli równo)                       | O(n log n)         |
| Przeciętny                                           | 	O(n log n)       |
| Najgorszy (np. już posortowana tablica i zły pivot)  | 	O(n²)            |

## **⭐ Cechy charakterystyczne** ##
Szybki w praktyce (lepszy niż Merge Sort czy Bubble Sort).

Niestabilny – nie zachowuje kolejności elementów o tej samej wartości.

Działa rekurencyjnie.

Można łatwo modyfikować strategię wyboru pivota.

Często używany w bibliotekach standardowych (np. C, C++ – jako część qsort()).

## **🧠 Ciekawostki** ##
Algorytm Quick Sort był używany w systemach UNIX-owych jako domyślna metoda sortowania.

W Pythonie standardowa funkcja sort() wykorzystuje Timsort, ale Quick Sort był rozważany wcześniej jako alternatywa.

W praktyce bardzo często hybrydyzuje się Quick Sort z innymi algorytmami, np. Merge Sort lub Insertion Sort.

Użycie złego pivota może całkowicie zrujnować wydajność (dlatego np. Quick Sort nie nadaje się bezpośrednio do danych prawie posortowanych).

## **✅ Podsumowanie** ##
Quick Sort to algorytm:

wydajny,

elegancki,

bardzo dobrze nadający się do implementacji rekurencyjnej,

z prostą strukturą, ale potężnymi możliwościami optymalizacji.

Jego znajomość – łącznie z wariantami implementacyjnymi i modyfikacjami – pokazuje zrozumienie zasad działania sortowania oraz programowania rekurencyjnego i optymalizacji algorytmów.
