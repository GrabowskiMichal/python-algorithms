# *🔢 Sortowanie przez wybór (Selection Sort)* #
## **📜 Historia algorytmu** ##

Sortowanie przez wybór to jeden z najstarszych i najprostszych algorytmów sortowania. Chociaż jego dokładne pochodzenie nie jest znane, był on używany już w pierwszych implementacjach algorytmów sortujących, m.in. w edukacji i na komputerach wczesnej generacji. Jego idea jest intuicyjna i bliska „sortowaniu karteczek” przez ręczne wybieranie najmniejszego elementu i przesuwanie go na początek.
## **🧠 Idea algorytmu** ##

Algorytm sortowania przez wybór polega na wielokrotnym wyszukiwaniu najmniejszego (lub największego) elementu z nieposortowanej części tablicy i zamianie go z pierwszym elementem tej części. Proces ten powtarza się, przesuwając granicę posortowanej części tablicy o jeden w prawo.
## **⚙️ Działanie krok po kroku** ##

Podziel tablicę na dwie części: posortowaną (na początku pustą) i nieposortowaną.

Znajdź najmniejszy element w nieposortowanej części.

Zamień go miejscami z pierwszym elementem nieposortowanej części.
Rozszerz część posortowaną o jeden element.

Powtarzaj kroki 2–4 aż cała tablica będzie posortowana.

```python
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
```
## **📊 Złożoność obliczeniowa – Selection Sort** ##

| Rodzaj przypadku    | Złożoność czasowa           |
| ------------------- | --------------------------- |
| Najlepszy przypadek | O(n²)                       |
| Średni przypadek    | O(n²)                       |
| Najgorszy przypadek | O(n²)                       |
| Pamięciowa          | O(1) – sortowanie w miejscu |

## **⚒️ Modyfikacje i warianty** ##

Sortowanie malejąco – wystarczy zmienić warunek porównania z < na >.

Zamiana z ostatnim elementem – nieco inna implementacja, ale ta sama idea.

Wersja stabilna – domyślna wersja nie jest stabilna, ale można to poprawić przez odpowiednią manipulację przesuwaniem elementów.

## **🧬 Cechy charakterystyczne** ##

Prosty i intuicyjny do zrozumienia.

Nie wymaga dodatkowej pamięci.

Działa niezależnie od rozkładu danych wejściowych.

Niezbyt wydajny dla dużych zbiorów danych (złożoność O(n²)).

Wersja niestabilna (nie zachowuje kolejności równych elementów).

## **🧪 Od środka – co się dzieje?** ##

Algorytm przeszukuje całą nieposortowaną część tablicy, aby znaleźć najmniejszy element, a następnie umieszcza go na właściwym miejscu (na początku nieposortowanej części). Operacja ta jest powtarzana aż do końca tablicy.
### **🤔 Ciekawostki** ##

W praktyce rzadko stosowany w profesjonalnym oprogramowaniu ze względu na niską wydajność.

Nadal bardzo często pojawia się w materiałach edukacyjnych jako pierwszy kontakt z algorytmami sortującymi.

Ze względu na prostotę jest często wykorzystywany do sortowania danych na bardzo ograniczonych urządzeniach lub w systemach z ekstremalnie małą ilością pamięci RAM.

## **🔄 Alternatywne podejścia** ##

Bubble Sort – prostszy, ale jeszcze mniej wydajny.

Insertion Sort – zwykle szybszy niż selection sort dla małych zbiorów.

Merge Sort / QuickSort / HeapSort – znacznie bardziej efektywne dla większych danych.

Timsort – nowoczesny, hybrydowy algorytm używany m.in. w Pythonie (sorted()).

## **🧠 Podsumowanie** ##

Sortowanie przez wybór to:

edukacyjny, klasyczny algorytm sortowania,

łatwy do zaimplementowania i zrozumienia,

nieefektywny dla dużych danych,

ale bardzo dobry do nauki podstaw sortowania i analizy algorytmów.