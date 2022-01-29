def bfs(g, s, discovered):
    """Primenjuje DFS za neotkriven deo grafa(Graph) g počevši od čvora(Vertex) s.

        discovered je rečnik koji mapira svaki čvor na ivicu koja je koriščen za njegovo pronalaženje
        prilikom BFS (prvobitno treba da bude mapiran na None).
        Nove ivice se dodaju u ovaj rečnik.
    """

    level = [s]                        # prvi nivo uključuje samo s
    while len(level) > 0:
        next_level = []                  # priprema za skupljanje novih čvorova
        for u in level:
            for e in g.incident_edges(u):  # za svaki odlazni čvor iz u
                v = e.opposite(u)
                if v not in discovered:      # v je neposećen čvor
                    discovered[v] = e          # e je ivica preko koje je otkriven čvor v
                    next_level.append(v)       # v će biti razmotreno u sledećem prolazu
        level = next_level               # menjamo oznaku 'next' sledećeg nivoa da postane trenutni


def bfs_complete(g):
    """Primenjuje DFS nad celim grafom i vraća šumu kao rečnik.

        Rezultat mapira svaki čvor v na ivicu koja je korišćena za njegovo otkrivanje.
        (Čvorovi koji su koreni BFS stabla su mapirani na None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None            # u će biti koren stabla
            bfs(g, u, forest)
    return forest
