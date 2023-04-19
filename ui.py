from Graph import *


class UI:
    def __init__(self, graph:Graph) -> None:
        self.graph=graph

    @staticmethod
    def print_menu():
        print("\nMenu:")
        print("\t1. Get number of vertices")
        print("\t2. Get number of edges")
        print("\t3. Show all vertices")
        print("\t4. Check if edge")
        print("\t5. In degree and out degree of a vertex")
        print("\t6. Show outbound and inbound edges of a vertex")
        print("\t7. Get cost of an edge")
        print("\t8. Modify cost of an edge")
        print("\t9. Add vertex")
        print("\t10. Remove vertex")
        print("\t11. Add edge")
        print("\t12. Remove edge")
        print("\t13. Replace current graph with a random graph")
        print("\t14. Read graph from file")
        print("\t15. Write the current graph to a file")
        print("\t16. Make a copy of the graph")
        print("\t17. Revert graph ")
        print("\t18. Shortest path from one edge to another")
        print("\t0. EXIT")

    def handle_user_option(self, user_option):
        GET_VERTICES_COUNT = '1'; GET_EDGES_COUNT = '2'; SHOW_VERTICES = '3';
        CHECK_IF_EDGE = '4'; IN_OUT_DEGREE_VERTEX = '5'; IN_OUT_EDGES = '6'; GET_EDGE_COST = '7';
        MODIFY_COST = '8'; ADD_VERTEX = '9'; REMOVE_VERTEX = '10'; ADD_EDGE = '11';
        REMOVE_EDGE = '12'; RANDOM_GRAPH = '13'; READ_GRAPH = '14'; WRITE_GRAPH = '15';
        COPY_GRAPH = '16'; REVERT_TO_LAST_COPY = '17'; SHORTEST_PATH = '18'

        if user_option == GET_VERTICES_COUNT:
            print(f"The vertecies number is:{self.graph.vertecies_count}")
        elif user_option == GET_EDGES_COUNT:
            print(f"Edge number is {len(self.graph.edges)}")
        elif user_option == SHOW_VERTICES:
            vertecies=self.graph.vertecies
            for vertex in vertecies:
                print(vertex)
        elif user_option == CHECK_IF_EDGE:
            outVert=int(input("Out-vertex:"))
            inVert=int(input("In-vertex:"))
            print(f"{self.graph.has_edge(outVert, inVert)}")
        elif user_option == IN_OUT_DEGREE_VERTEX:
            vertex=int(input("Enter vertex:"))
            print("The out degree is ", self.graph.degree_out(vertex))
            print("The in degree is ", self.graph.degree_in(vertex))
        elif user_option == IN_OUT_EDGES:
            vertex=input("Vertex:")
            edges_out=self.graph.out_edges(vertex)
            edges_in=self.graph.out_edges(vertex)
            print("In-going edges")
            for edge in edges_in:
                print(edge)
            print("Out-going edges")
            for edge in edges_out:
                print(edge)
        elif user_option == GET_EDGE_COST:
            out_vertex=input("Enter the out vertex:")
            in_vertex=input("Enter the in vertex:")
            edge=self.graph.get_edge(out_vertex, in_vertex)
            if edge is not None:
                print(edge.cost)
            else:
                print("The edge does not exist")
        elif user_option == MODIFY_COST:
            pass
        elif user_option == ADD_VERTEX:
            self.graph.add_vertex(int(input("Vertex:")))
        elif user_option == REMOVE_VERTEX:
            self.graph.remove_vertex(int(input("Vertex:")))
        elif user_option == ADD_EDGE:
            self.graph.add_edge(int(input("Weight")), int(input("Vertex 1:")), int(input("Vertex 2:")))
        elif user_option == REMOVE_EDGE:
            self.graph.remove_edge(int(input("Vertex 1:")), int(input("Vertex2:")))
        elif user_option == RANDOM_GRAPH:
            pass
        elif user_option == READ_GRAPH:
            pass
        elif user_option == WRITE_GRAPH:
            pass
        elif user_option == COPY_GRAPH:
            pass
        elif user_option == REVERT_TO_LAST_COPY:
            pass
        else:
            print("Unknown command.")
        print("\n", self.graph)
        input("Press ENTER")

def start():
    ui=UI( Graph([x for x in range(1,10)], [Edge(1, 1,2), Edge(69, 1,5), Edge(80 ,2,8)] ))
    while True:
        ui.print_menu()
        user_option=input("Enter a command > ")
        ui.handle_user_option(user_option)


if __name__=="__main__":
    start()
