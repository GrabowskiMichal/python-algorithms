# *Sito Eratostenesa* #
## **📜 Historia algorytmu** ##
Sito Eratostenesa to jeden z najstarszych znanych algorytmów do znajdowania liczb pierwszych. Został opisany przez greckiego matematyka Eratostenesa z Cyreny około 200 r. p.n.e. Eratostenes był nie tylko matematykiem, ale też geografem i filozofem — znany jest m.in. z wyznaczenia obwodu Ziemi z dużą dokładnością.

## **🧠 Idea algorytmu** ##
Algorytm pozwala znaleźć wszystkie liczby pierwsze mniejsze lub równe danemu n. Jego działanie polega na eliminowaniu (czyli „skreślaniu”) wielokrotności każdej liczby pierwszej, zaczynając od 2. Po przetworzeniu wszystkich liczb do pierwiastka z n, pozostają tylko liczby pierwsze.

## **⚙️ Działanie krok po kroku** ##
Tworzymy listę liczb od 2 do n.

Zaczynamy od pierwszej liczby z listy (czyli 2).

Skreślamy wszystkie wielokrotności tej liczby większe niż ona sama.

Przechodzimy do kolejnej nieskreślonej liczby i powtarzamy krok 3.

Kończymy, gdy aktualna liczba przekroczy pierwiastek z n.

```python
def sito_eratostenesa(n):
    """
    Funkcja zwraca listę wszystkich liczb pierwszych mniejszych lub równych n,
    używając algorytmu Sita Eratostenesa.
    """

    # Jeżeli n < 2, nie ma żadnych liczb pierwszych
    if n < 2:
        return []

    # Tworzymy listę o długości n+1 i zakładamy, że każda liczba jest na początku pierwsza (True)
    # Indeksy odpowiadają liczbom od 0 do n
    sito = [True] * (n + 1)

    # 0 i 1 nie są liczbami pierwszymi
    sito[0] = False
    sito[1] = False

    # Sprawdzamy liczby od 2 do pierwiastka z n
    for i in range(2, int(n ** 0.5) + 1):
        if sito[i]:  # Jeśli liczba i jest pierwsza
            # Skreślamy wszystkie wielokrotności liczby i (zaczynamy od i*i)
            for j in range(i * i, n + 1, i):
                sito[j] = False  # Nie jest pierwsza

    # Tworzymy listę liczb, które są nadal oznaczone jako True
    liczby_pierwsze = []
    for i in range(2, n + 1):
        if sito[i]:
            liczby_pierwsze.append(i)

    return liczby_pierwsze

print(sito_eratostenesa(36))
```

## 📊 Złożoność obliczeniowa – Sito Eratostenesa ##

| Rodzaj przypadku | Złożoność czasowa |
|------------------|-------------------|
| Zawsze           | O(n log(log(n))    |

## **⚒️ Modyfikacje i warianty** ##
Zwracanie samego sita (czyli tablicy booli) – przydatne przy częstych zapytaniach o pierwszość liczby.

Użycie typu bitarray lub numpy.array – oszczędność pamięci i przyspieszenie.

Segmentowane sito – pozwala na generowanie liczb pierwszych w dużych zakresach, np. od 10⁹ do 10⁹+10⁶.

Zastosowanie optymalizacji:

zaczynanie wewnętrznej pętli od i*i, bo wcześniejsze wielokrotności zostały już przetworzone.

iterowanie tylko po liczbach nieparzystych (po 2).

unikanie powtórnych obliczeń np. używając pętli range(i*i, n+1, i) zamiast range(2*i, n+1, i).

## **🧬 Cechy charakterystyczne** ##
Złożoność czasowa: O(n log log n)

Złożoność pamięciowa: O(n) – dla prostego sita

Deterministyczny algorytm – zawsze daje ten sam wynik

Bardzo szybki i efektywny dla stosunkowo dużych n

Nadaje się do modyfikacji – np. w celu zliczania liczby pierwszych, znajdowania największej liczby pierwszej ≤ n, itp.

## **🧪 Od środka – co się dzieje?** ##
Główna idea to oznaczanie „nie-pierwszych” jako False.

Zamiast sprawdzać każdą liczbę oddzielnie (co byłoby wolne), masowo skreślamy wielokrotności.

To jest różnica między "sprawdzaniem pierwszości" a "generowaniem zbioru pierwszych" – sito nie testuje pierwszości jednej liczby, tylko tworzy całą tablicę.

## **🤔 Ciekawostki** ##
"Sito" w nazwie pochodzi od metafory przesiewania piasku — liczby niepierwsze są „odsiewane”.

Istnieje różnica w działaniu sita i testów pierwszości: sito generuje liczby, testy sprawdzają konkretną liczbę.

Współczesne wersje są często zaimplementowane w bibliotekach do obliczeń liczbowych, np. w SymPy, NumPy, SageMath.

Segmentowane sito Eratostenesa było używane w rekordowych obliczeniach liczb pierwszych w dużych zakresach, np. do przeszukiwania liczb pierwszych > 10^12.

Algorytm nie wymaga dzielenia – używa jedynie dodawania i indeksowania.

## **🔄 Alternatywne podejścia** ##
Sito Sundarama – alternatywa dla sita Eratostenesa, mniej popularne.

Testy probabilistyczne (np. Miller-Rabin) – nie służą do generowania liczb pierwszych, ale do testowania pierwszości.

Algorytmy oparte na matematyce modularnej i teorii liczb – np. AKS primality test (złożoność wielomianowa, ale wolny).

## **🧠 Podsumowanie** ##
Sito Eratostenesa to:

klasyczny, prosty i genialny algorytm,

bardzo szybki i nadający się do wielu zastosowań,

świetna baza do dalszego rozszerzania wiedzy o liczbach pierwszych i algorytmice.