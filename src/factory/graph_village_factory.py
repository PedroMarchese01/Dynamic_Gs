import networkx as nx
import random

def generate(village):
    graph = nx.Graph()

    graph.add_nodes_from(village)

    homes = list(village)
    random.shuffle(homes)

    for i in range(1, len(homes)):
        home = homes[i]
        connection = random.choice(homes[:i])
        graph.add_edge(home, connection)

    for home in homes:
        for other in homes:
            if home != other and random.random() < 0.2:
                graph.add_edge(home, other)

    return graph