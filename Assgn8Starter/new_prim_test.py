from undirected_graph import Graph
import heapq
import time

from Assgn8Starter.kruskal_mst_reference_implementation import initialize_disjoint_set

def initialize_disjiont_set(items):
    re = {item: (-1, "") for item in items}
    return re

def write_tree_edges_to_file(edges, filename):
    with open(filename, mode='w') as f:
        total=0
        for v1, v2, w in edges:
            f.write("{} {} {}\n".format(v1, v2, w))
            total=total + int(w)
        f.write("total=%d\n"%total)


# Do not change this function's name or the arguments it takes. Also, do not change
# that it writes out the results at the end.
# This is the full contract of you code (this function in this file). Otherwise,
# please feel free to create helpers, modify provided code, create new helper files, etc.
# Whatever you turn in is what we will grade (ie we won't provide any files or overwrite
# any of yours)
# Have fun!
def compute_mst(filename):
    '''Use Prim's algorithm to compute the minimum spanning tree of the weighted undirected graph
    described by the contents of the file named filename.'''
    tree_edges = []
    # TODO compute the edges of a minimum spanning tree
    write_tree_edges_to_file(tree_edges, filename + '.mst')

if __name__ == '__main__':
    #读取信息
    #时间换空间 保存当前最优解

    start_time = time.process_time()
    g = Graph()
    with open("5 input") as f:
        for line in f:
            try:
                v1, v2, w = line.split()
                g.add_edge(v1, v2, {'weight': int(w)})
            except:
                pass
    node_dist=initialize_disjiont_set(g.get_nodes())
    print(g.get_nodes())
    print(node_dist) # O(n)
    first_node=list(g.get_nodes())[0] #O(1)
    node_sets = set([first_node]) #O(1)


    tree_edges = []
    print(g.neighbors(first_node))
    for node in g.neighbors(first_node): # O(n)
        if node_dist[node][0] == -1 or g.attributes_of(first_node,node).get('weight')<node_dist[node][0]:
            node_dist[node]=(g.attributes_of(first_node,node)["weight"],first_node)

    for i in range(len(g.get_nodes())-1):# O(n)
        min_node=None
        for node in g.get_nodes():#O(n)
            if node not in node_sets and node_dist[node][0] != -1 and (min_node == None or node_dist[node][0] < node_dist[min_node][0]):
                min_node=node
        node_sets.add(min_node)
        tree_edges.append((node_dist[min_node][1],min_node,node_dist[min_node][0]))
        for node in g.neighbors(min_node):# O(n)
            if node_dist[node][0] == -1 or g.attributes_of(min_node, node)['weight'] < node_dist[node][0]:
                node_dist[node] = (g.attributes_of(min_node, node)["weight"], min_node)
    print(tree_edges)




    #put all the G's node in the queue

    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))

    write_tree_edges_to_file(tree_edges,"5.mst")