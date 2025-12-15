def decomposition_primaire(n) :
    resultat = {}
    diviseur = 2
    while n != 1 :
        resultat[diviseur] = 0
        while n % diviseur == 0 :
            resultat[diviseur] += 1
            n = n / diviseur
        diviseur += 1
    return resultat

print(decomposition_primaire(12))

def euler(n) :
    resultat = 1
    d = decomposition_primaire(n)
    for k in d.keys() :
        resultat *= k ** d[k] - k ** (d[k] - 1)
    return resultat

print(euler(12))

def euclyde(n, d) :
    resultat = []

