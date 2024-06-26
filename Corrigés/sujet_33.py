# Exercice 1

def renverse(mot):
    resultat = ""
    for lettre in mot:
        resultat = lettre + resultat

    return resultat # mot[::-1]

assert renverse("") == ""
assert renverse("abc") == "cba"
assert renverse("informatique") == "euqitamrofni"

# Exercice 2

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = i
            while multiple < n:
                tab[multiple] = False
                multiple += i
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]