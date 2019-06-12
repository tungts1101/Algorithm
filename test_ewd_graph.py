import argparse
from ewdgraph import EdgeWeightedDigraph as ewd,DijkstraSP as dsp

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fname',help="input file")
    args = parser.parse_args()

    graph = ewd()
    graph.insert(args.fname)
    s = 0
    sp = dsp(graph,s)

    for v in range(graph.V):
        print(str(s) + " to " + str(v),end = ' ')
        print("{:.2f}:".format(sp.distTo[v]),end = ' ')
        if sp.hasPathTo(v):
            path = sp.pathTo(v)
            while not path.empty():
                e = path.get()
                print(e,end = ' ')
        print()

if __name__=='__main__':
    Main()
