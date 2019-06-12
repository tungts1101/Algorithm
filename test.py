import argparse
from dgraph import Graph
from dalgo import KosarajuCC

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fname',help="input file")
    args = parser.parse_args()

    graph = Graph()
    graph.insert(args.fname)

    KosarajuCC(graph)

if __name__=='__main__':
    Main()
