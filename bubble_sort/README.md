# *🧩 Bubble Sort – Sortowanie bąbelkowe* #
## **📜 Historia i kontekst** ##

Bubble Sort to jeden z najstarszych i najprostszych algorytmów sortowania, znany już od lat 50. XX wieku. Jego nazwa pochodzi od sposobu działania – największe (lub najmniejsze) elementy "wypływają" na koniec listy niczym bąbelki w wodzie.

Choć nie jest najwydajniejszy, świetnie nadaje się do nauki podstaw sortowania i analizy algorytmów.

## **🧠 Idea algorytmu** ##

Bubble Sort działa na zasadzie porównywania par sąsiadujących ze sobą elementów i zamiany ich miejscami, jeśli są w złej kolejności.

Każde przejście przez tablicę "przesuwa" największy element na koniec. Proces powtarza się, aż cała tablica zostanie posortowana.

## **⚙️ Działanie krok po kroku** ##

Przejdź przez całą listę.

Porównuj każdą parę sąsiednich elementów.

Jeśli element z lewej strony jest większy – zamień je miejscami.

Powtarzaj proces aż do momentu, gdy żadne zamiany nie będą już potrzebne.

## **🧪 Kod źródłowy (Python)** ##

```python
# Funkcja sortująca tablicę za pomocą sortowania bąbelkowego (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Ostatnie i elementów jest już na miejscu, nie trzeba ich porównywać
        for j in range(0, n - i - 1):
            # Jeśli elementy są w złej kolejności – zamień je
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Przykładowe użycie
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print(array)
```

## **📊 Złożoność obliczeniowa** ##

| Przypadek | Złożoność czasowa |
| --------- | ----------------- |
| Najlepszy | O(n)              |
| Średni    | O(n²)             |
| Najgorszy | O(n²)             |
| Pamięć    | O(1)              |


Najlepszy przypadek występuje, gdy tablica jest już posortowana – wtedy możemy dodać optymalizację z flagą swapped, by przerwać pętlę wcześniej.

## **⚒️ Zastosowania i modyfikacje** ##

Stosowany głównie w celach edukacyjnych.

Pomocny do nauki debugowania i podstaw algorytmiki.

W mniejszych zbiorach danych działa poprawnie, choć nieefektywnie.

## **🧬 Cechy charakterystyczne** ##

Prosty w implementacji – bardzo czytelny kod.

Stabilny – zachowuje kolejność równych elementów.

Sortowanie w miejscu (in-place) – nie wymaga dodatkowej pamięci.

Nieefektywny dla dużych danych – powolny przy dużych tablicach.

## **🤔 Ciekawostki** ##

Jest często pierwszym algorytmem sortowania, jaki poznaje się na zajęciach z programowania.

Choć niepraktyczny dla dużych danych, jego prosta struktura ułatwia analizę algorytmów.

Posiada wiele odmian (np. Cocktail Sort – sortowanie dwukierunkowe).

## **🧠 Podsumowanie** ##

Bubble Sort to klasyka w świecie algorytmów. Mimo swojej prostoty i niskiej wydajności, jest doskonałym wprowadzeniem do tematu sortowania. Łatwy do zrozumienia i zaimplementowania – idealny na początek nauki algorytmiki.
