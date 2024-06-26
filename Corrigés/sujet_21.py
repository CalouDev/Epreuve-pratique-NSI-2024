# Exercice 1

def recherche_motif(motif, texte):
    resultat = []
    for i in range(len(texte)-len(motif)+1):
        if texte[i:i+len(motif)] == motif:
            resultat.append(i)
    
    return resultat

assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]

# Exercice 2

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc

assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0) == [0, 1, 2, 3]
assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4) == [4, 5]
