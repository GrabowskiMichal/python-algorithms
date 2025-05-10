# *🧩 Insertion Sort – Sortowanie przez wstawianie* #
## **📜 Historia i kontekst** ##

Sortowanie przez wstawianie to jeden z najprostszych i najstarszych algorytmów sortujących. Jest intuicyjny i często używany jako wprowadzenie do algorytmiki sortowania. Działa dobrze na małych i prawie posortowanych zbiorach danych.
## **🧠 Idea algorytmu** ##

Podobnie jak w układaniu kart w ręku – wybieramy kolejną kartę (element), znajdujemy dla niej odpowiednie miejsce w posortowanej części zbioru i wstawiamy ją tam, przesuwając inne karty (elementy), jeśli trzeba.
## **⚙️ Działanie krok po kroku** ##

Uznaj pierwszy element za posortowany.

Weź następny element jako key.

Cofaj się w lewo po liście, przesuwając większe elementy w prawo.

Gdy znajdziesz właściwe miejsce, wstaw tam key.

Powtarzaj kroki 2–4 dla każdego kolejnego elementu.

## **🧪 Kod źródłowy (Python)** ##

```python
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
```

## **📊 Złożoność obliczeniowa** ##

| Przypadek                              | Złożoność czasowa           |
| -------------------------------------- | --------------------------- |
| Najlepszy (dane już posortowane)       | O(n)                        |
| Średni                                 | O(n²)                       |
| Najgorszy (dane posortowane odwrotnie) | O(n²)                       |
| Pamięć                                 | O(1) (sortowanie w miejscu) |


## **⚒️ Zastosowania i modyfikacje** ##

Działa bardzo dobrze na małych zbiorach danych.

Może być używany jako część bardziej złożonych algorytmów hybrydowych (np. Timsort).

Łatwy do zaimplementowania i debugowania.

Stabilny (nie zmienia kolejności równych elementów).

## **🧬 Cechy charakterystyczne** ##

Stabilny algorytm

Sortowanie w miejscu (in-place)

Łatwy do zaimplementowania

Niewydajny dla dużych zbiorów danych

Działa dobrze na prawie posortowanych danych

## **🤔 Ciekawostki** ##

Algorytm Insertion Sort jest używany w bibliotekach sortujących jako metoda pomocnicza (np. w Pythonie lub JDK).

Jest analogią do sposobu, w jaki ludzie często sortują rzeczy ręcznie – np. karty do gry.

Dzięki prostocie często jest wybierany do zastosowań edukacyjnych lub wbudowanych systemów o ograniczonej mocy obliczeniowej.

## **🧠 Podsumowanie** ##

Sortowanie przez wstawianie to prosty, elegancki i skuteczny algorytm dla małych lub prawie uporządkowanych zbiorów. Choć nie skalowalny dla dużych danych, pozostaje świetnym narzędziem edukacyjnym i pomocniczym w praktyce.