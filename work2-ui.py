#!/bin/python
from ctypes import c_longlong
from Graph import *
from ui import *


class UiFunctions:
    def __init__(self, graph) -> None:
        self._graph=graph

    def print_graph(self):
        print(self._graph)

    def get_file_graph(self):
        file_name = input("Enter the file name:")
        file=open(file_name, "r")
        file_input=file.read()
        file_lines=file_input.splitlines()
        tkns=file_lines[0].split(" ")
        vertecies_no=int(tkns[0])
        # edges_no=int(file_lines[1])
        graph=Graph([x for x in range(vertecies_no)], [])
        file_lines=file_lines[1:]
        for line in file_lines:
            tkns=line.split(" ")
            x=int(tkns[0])
            y=int(tkns[1])
            cost=int(tkns[2])
            graph.add_edge(cost, x, y)
        self._graph=graph

    def print_connected_components(self):
        connected_components = get_connected_components(self._graph)
        for key in connected_components:
            print(key,":", end="\t")
            for vertex in connected_components[key]:
                print(vertex, end=" ")
            print()



def start():
    ui=UiFunctions(UnidirectedGraph(
        [0,1,2,3,4,5,6,7],
        [Edge(100, 1, 2),
         Edge(200, 2, 3),
         Edge(300, 1, 4),
         Edge(100, 4, 5),
         Edge(50, 6, 7)]
    ))

    """
        [0,1,2,3,4,5,6,7],
        1 2 100
        2 3 200
        1 4 300
        4 5 100
        6 7 50
    """
    menu=Menu()
    menu.add_entry(ui, "Exit", UiFunctions.print_graph)
    menu.add_entry(ui, "Print graph", UiFunctions.print_graph)
    menu.add_entry(ui, "Read graph from file", UiFunctions.get_file_graph)
    menu.add_entry(ui, "Print connected components", UiFunctions.print_connected_components)
    menu.start()

start()
