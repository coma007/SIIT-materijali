def dfs(g, u, discovered):
    """ Primenjuje DFS na neotkriven deo grafa(Graph) g počevši od čvora(Vertex) u.

    discovered je rečnik koji mapira svaki čvor na ivicu koja je koriščen za njegovo pronalaženje
    prilikom DFS.
    Nove ivice se dodaju u ovaj rečnik.
    """
    for e in g.incident_edges(u):    # za svaku odlaznu granu iz u
        v = e.opposite(u)
        if v not in discovered:        # provera da li je čvor već posećen
            discovered[v] = e            # e je ivica kojom je otkriven čvor v
            dfs(g, v, discovered)        # rekurzivna pretraga od v


def construct_path(u, v, discovered):
    """
    Rekonstrukcija puta. Vraća listu čvorova koje čine direktan put od u do v,
    ili prazna lista ako se do v ne može doći iz u.

    discovered je rezultujući rečnik iz prethodnog poziva DFS sa početkom u u.
    """
    path = []                        # počinje s od prazne putanje
    if v in discovered:
        # formiramo listu od v do u i onda je na kraju obrnemo
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()                 # obrtanje putanje
    return path


def dfs_complete(g):
    """Primenjuje DFS nad celim grafom i vraća šumu kao rečnik.

    Rezultat mapira svaki čvor v na ivicu koja je korišćena za njegovo otkrivanje.
    (Čvorovi koji su koreni DFS stabla su mapirani na None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None             # u će biti koren stabla
            dfs(g, u, forest)
    return forest
