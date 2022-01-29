from primeri_graf import *
from dfs import *
from bfs import *

if __name__ == '__main__':
    graph = figure_14_14()
    print('-------------- DFS --------------')
    forest = dfs_complete(graph)
    for vertex in forest.keys():
        print('Vertex: ' + str(vertex))
        if forest[vertex]:
            print('Edge: ' + str(forest[vertex]))
        else:
            print('Edge: None')

    print('\n\n-------------- BFS --------------')
    forest = bfs_complete(graph)
    for vertex in forest.keys():
        print('Vertex: ' + str(vertex))
        if forest[vertex]:
            print('Edge: ' + str(forest[vertex]))
        else:
            print('Edge: None')


