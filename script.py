def decomposition_primaire(n):
    resultat = {}
    diviseur = 2
    while n > 1:
        if n % diviseur == 0:
            resultat[diviseur] = 0
            while n % diviseur == 0:
                resultat[diviseur] += 1
                n = n // diviseur
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

def euclide_etendu(a, b) :
    resultats = []
    r = a % b
    resultats.append({'a' : a, 'b' : b, 'r' : r})
    while r > 1 :
        a = b
        b = r
        r = a % b
        resultats.append({'a': a, 'b': b, 'r': r})
    return resultats

print(euclide_etendu(40, 33))


def coefficients_bezout(algo_euclide_etendu):
    if not algo_euclide_etendu or algo_euclide_etendu[-1]['r'] != 1:
        raise ValueError("Les nombres ne sont pas premiers entre eux (PGCD != 1)")
    derniere_etape = algo_euclide_etendu[-1]
    q = derniere_etape['a'] // derniere_etape['b']
    u = 1
    v = -q
    for i in range(len(algo_euclide_etendu) - 2, -1, -1):
        etape = algo_euclide_etendu[i]
        q = etape['a'] // etape['b']
        ancien_u = u
        ancien_v = v
        u = ancien_v
        v = ancien_u - (ancien_v * q)
    return u, v


def inverse(e, m):
    algo_euclide_etendu = euclide_etendu(m, e)
    u, v = coefficients_bezout(algo_euclide_etendu)
    return v % m

print(inverse(33, 40))


def exp_modulaire(x, p, n):
    r = 1
    x = x % n
    while p > 0:
        if p % 2 == 1:
            r = (r * x) % n
        x = (x * x) % n
        p = p // 2
    return r

def rsa_dechiffrer(p1, p2, e, M) :
    N = p1 * p2
    phi_N = euler(N)
    d = inverse(e, phi_N)
    return exp_modulaire(M, d, N)

def rsa_chiffrer(p1, p2, e, M) :
    N = p1 * p2
    return exp_modulaire(M, e, N)

# --- TEST RSA ---

premier_1 = 11
premier_2 = 5
e = 33
M = 2

M_dechiffre = rsa_dechiffrer(premier_1, premier_2, e, M)

print(f"MESSAGE CHIFFRE = {M}\nMESSAGE DECHIFFRE = {M_dechiffre}\n")
print(f"MESSAGE DECHIFFRE = {M_dechiffre}\nMESSAGE CHIFFRE = {rsa_chiffrer(premier_1, premier_2, e, M_dechiffre)}")