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