from graph import Graph


def graph_from_edgelist(E, directed=False):
    """Kreira graf od ivica.

        Dozvoljeno je dva načina navođenje ivica:
            (origin,destination)
            (origin,destination,element).
        Podrazumeva se da se labele čvorova mogu hešovati.
    """
    g = Graph(directed)
    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])

    vertices = {}  # izbegavamo ponavljanje labela između čvorova
    for v in V:
        vertices[v] = g.insert_vertex(v)

    for e in E:
        src = e[0]
        dest = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(vertices[src], vertices[dest], element)

    return g


def figure_14_3():
    """Vraća neusmeren graf."""
    E = (
        ('BOS', 'SFO'), ('BOS', 'JFK'), ('BOS', 'MIA'), ('JFK', 'BOS'),
        ('JFK', 'DFW'), ('JFK', 'MIA'), ('JFK', 'SFO'), ('ORD', 'DFW'),
        ('ORD', 'MIA'), ('LAX', 'ORD'), ('DFW', 'SFO'), ('DFW', 'ORD'),
        ('DFW', 'LAX'), ('MIA', 'DFW'), ('MIA', 'LAX'),
    )
    return graph_from_edgelist(E, True)


def figure_14_9():
    """Vraća neusmeren graf."""
    E = (
        ('A', 'B'), ('A', 'E'), ('A', 'F'), ('B', 'C'), ('B', 'F'),
        ('C', 'D'), ('C', 'G'), ('D', 'G'), ('D', 'H'), ('E', 'F'),
        ('E', 'I'), ('F', 'I'), ('G', 'J'), ('G', 'K'), ('G', 'L'),
        ('H', 'L'), ('I', 'J'), ('I', 'M'), ('I', 'N'), ('J', 'K'),
        ('K', 'N'), ('K', 'O'), ('L', 'P'), ('M', 'N'),
    )
    return graph_from_edgelist(E, False)


def figure_14_12():
    """Vraća neusmeren graf.
    """
    E = (
        ('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'F'), ('C', 'D'), ('C', 'E'),
        ('C', 'H'), ('D', 'F'), ('E', 'G'), ('F', 'G'), ('F', 'H'), ('G', 'H')
    )
    return graph_from_edgelist(E, True)


def figure_14_14():
    """Vraća težinski, neusmeren graf."""
    E = (
        ('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
        ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
        ('DFW', 'ORD', 802), ('DFW', 'MIA', 1121), ('ORD', 'BOS', 867),
        ('ORD', 'JFK', 740), ('MIA', 'JFK', 1090), ('MIA', 'BOS', 1258),
        ('JFK', 'BOS', 187),
    )
    return graph_from_edgelist(E, False)


def figure_14_15():
    """Vraća težinski, neusmeren graf."""
    E = (
        ('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
        ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
        ('DFW', 'ORD', 802), ('DFW', 'JFK', 1391), ('DFW', 'MIA', 1121),
        ('ORD', 'BOS', 867), ('ORD', 'PVD', 849), ('ORD', 'JFK', 740),
        ('ORD', 'BWI', 621), ('MIA', 'BWI', 946), ('MIA', 'JFK', 1090),
        ('MIA', 'BOS', 1258), ('BWI', 'JFK', 184), ('JFK', 'PVD', 144),
        ('JFK', 'BOS', 187),
    )
    return graph_from_edgelist(E, False)
