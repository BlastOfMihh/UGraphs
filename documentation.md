
#Lab 1 : Documentation
 

## Specification
We shall define a class named *Graph* representing a directed 

In addition, there are defined the following classes :

Graph::Edge
Which is used for representing the information about the edges inside the graph.

The class Graph which has the following methods:

def __init__(self, vertecies:list, edges:list) -> None:
* Initializes the graph function 

@property
def vertecies(self):

@property
def vertecies_count(self):

@property
def edges(self):

def add_edge(self, weight, vertex_out, vertex_in):

def degree_in(self, vertex):

def degree_out(self, vertex):

def __str__(self) -> str:

def remove_edge(self, vertex_out, vertex_in):

def remove_vertex(self, vertex):

def out_edges(self, vertex):

def in_edges(self, vertex):

def add_vertex(self, vertex):

def get_edge(self, vertex_out, vertex_in):

def has_edge(self, vertex1, vertex2):

def get_copy(self):

def get_random(vertecies_no, edges_no, max_weight=100)->Graph:

