#!/usr/bin/env python3
from copy import deepcopy

# https://www.cs.ubbcluj.ro/~rlupsa/edu/grafe/lab1.html
# Problem number 1 for next lab

class GraphError(Exception):
    pass

class Edge:
    def __init__(self, weight, vertex1, vertex2) -> None:
        self._weight=weight
        self._vertex_out=vertex1
        self._vertex_in=vertex2

    @property
    def weight(self):
        return self._weight

    @property
    def vertex_in(self):
        return self._vertex_in

    @property
    def vertex_out(self):
        return self._vertex_out

    def __le__(self, leftEdge):
        if leftEdge is not Edge:
            raise Exception("Not an edge!!")
        return (self._weight <= leftEdge.weight)

    def __str__(self) -> str:
        return "Cost"+str(self.weight)+" "+str(self.vertex_in)+" "+str(self.vertex_out)

    def reverse(self):
        self._vertex_out, self._vertex_in = self._vertex_in, self._vertex_out

class Graph:
    def __init__(self, vertecies:list, edges:list) -> None:
        self._vertecies=vertecies
        self._edges=[]
        self._adjacency_list={}
        self._radjacency_list={}
        for edge in edges:
            self.add_edge(edge.weight, edge.vertex_out, edge.vertex_in)

    @property
    def vertecies(self):
        return deepcopy(self._vertecies)

    @property
    def vertecies_count(self):
        return len(self._vertecies)

    @property
    def edges(self):
        return deepcopy(self._edges)


    def add_edge(self, weight, vertex_out, vertex_in):
        if vertex_in not in self._vertecies or vertex_out not in self._vertecies:
            raise GraphError()
        def add_edge_list(adjacency_list, vertex_out, vertex_in, weight):
            if vertex_out not in adjacency_list:
                adjacency_list[vertex_out]=[]
            adjacency_list[vertex_out].append((weight, vertex_in))
        add_edge_list(self._adjacency_list, vertex_out, vertex_in, weight)
        add_edge_list(self._radjacency_list, vertex_in, vertex_out, weight)
        self._edges.append(Edge(weight, vertex_out, vertex_in))


    def _degree(self, adjacency_list, vertex):
        if vertex not in self.vertecies:
            raise GraphError()
        if vertex not in adjacency_list:
            return 0
        return len(adjacency_list[vertex])

    def degree_in(self, vertex):
        return self._degree(self._radjacency_list, vertex)

    def degree_out(self, vertex):
        return self._degree(self._adjacency_list, vertex)

    def __str__(self) -> str:
        ans=""
        for vertex in self._vertecies:
            if vertex in self._adjacency_list:
                ans+=str(vertex)+": "
                for weight,vertex_in in self._adjacency_list[vertex]:
                    ans+=f"(weight:{weight}, neighbor:{vertex_in}) "
                ans+="\n"
        return ans

    def remove_edge(self, vertex_out, vertex_in):
        def remove_from_edges():
            deleted=False
            for i in range(len(self._edges)):
                edge = self._edges[i]
                if edge.vertex_in==vertex_in and edge.vertex_out==vertex_out:
                    del self._edges[i]
                    deleted=True
                    break
            if not deleted:
                raise GraphError("")
        def remove_from_adjacency(adjacency_list, vertex_out, vertex_in):
            if vertex_out not in adjacency_list:
                return
            for i in range(len(adjacency_list[vertex_out])):
                weight, neighbor = adjacency_list[vertex_out][i]
                if neighbor==vertex_in:
                    del adjacency_list[vertex_out][i]
                    break

        remove_from_edges()
        remove_from_adjacency(self._adjacency_list, vertex_out, vertex_in)
        remove_from_adjacency(self._radjacency_list, vertex_in, vertex_out)

    def remove_vertex(self, vertex):
        old_edges=self.edges
        for edge in old_edges:
            if edge.vertex_in == vertex or edge.vertex_out == vertex:
                self.remove_edge(edge.vertex_out, edge.vertex_in)
        for i in range(len(self._vertecies)):
            if self._vertecies[i]==vertex:
                del self._vertecies[i]
                break

    def _edges_from_adjacency_list(self, adjacency_list, vertex):
        edges=[]
        for weight, vertex_in in adjacency_list[vertex]:
            edges.append(Edge(weight, vertex, vertex_in))
        return edges

    def out_edges(self, vertex):
        return self._edges_from_adjacency_list(self._adjacency_list, vertex)

    def in_edges(self, vertex):
        return self._edges_from_adjacency_list(self._radjacency_list, vertex)


    def add_vertex(self, vertex):
        if vertex not in self._vertecies:
            self._vertecies.append(vertex)


    def get_edge(self, vertex_out, vertex_in):
        if vertex_out not in self.vertecies or vertex_in not in self.vertecies:
            raise GraphError()
        for edge in self.edges:
            if edge.vertex_out==vertex_out and edge.vertex_in==vertex_in:
                return deepcopy(edge)
        return None

    def has_edge(self, vertex1, vertex2):
        return self.get_edge(vertex1, vertex2) is not None
