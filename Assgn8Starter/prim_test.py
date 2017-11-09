from undirected_graph import Graph
import heapq
import time

from Assgn8Starter.kruskal_mst_reference_implementation import initialize_disjoint_set


def write_tree_edges_to_file(edges, filename):
    # TODO write out the edges, one per line. The same format as produced by generate_mst_input
    pass


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

    g = Graph()
    with open("5000 input") as f:
        for line in f:
            try:
                v1, v2, w = line.split()
                g.add_edge(v1, v2, {'weight': int(w)})
            except:
                pass
    node_sets = initialize_disjoint_set(g.get_nodes())
    node_count = len(node_sets)
    #edges = [(g.attributes_of(v, u)['weight'], v, u) for u, v in g.get_edges()]
    #edges.sort()
    tree_edges = []

    #查看读取信息
    #print("node_sets is: ",node_sets)
    #print("node_count is: ",node_count)
    #print("edges is: ",edges)


    #put all the G's node in the queue
    queue=list(node_sets.keys())
    print("queue is: ",queue)

    #pick r, initinalize r_key = 0
    r=queue[0]
    queue.remove(r)
    #print("r is: ",r)

    start_time = time.process_time()
    weight=[]
    while queue:
        nei = g.neighbors(r)
        for i in nei:
            edge_weight = g.attributes_of(r, i)['weight']
            if i in queue:
                weight.append((edge_weight, r, i))
        weight = list(filter(lambda weight:weight[2] in queue,weight))
        weight.sort()
        tmp=weight[0][2]
        queue.remove(tmp)
        tree_edges.append((r,tmp,weight[0][0]))
        r=tmp

    print(tree_edges)
    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))
