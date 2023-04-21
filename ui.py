from Graph import *


class Menu:
    class MenuEntry:
        def __init__(self, ui, text, function):
            self.text=text
            self.function=function
            self._ui=ui
        def execute(self):
            self.function(self._ui)

    def __init__(self) -> None:
        self._menu_entries={}

    def add_entry(self, ui, text, function):
        self._menu_entries[str(len(self._menu_entries))]=self.MenuEntry(ui, text, function)

    def print_menu(self)->None:
        for i in self._menu_entries:
            entry=self._menu_entries[i]
            print(f"\t{i}){entry.text}")
    
    def _execute_menu_entry(self, entry):
        try:
            self._menu_entries[entry].execute()
        except GraphError as e:
            print("\n\tERROR ",str(e))

    def _read_menu_entry(self):
        return input("Chose a menu entry > ")

    def start(self):
        print("You can choose one of the following:")
        while True:
            self.print_menu()
            menu_entry=self._read_menu_entry()
            self._execute_menu_entry(menu_entry)
            if menu_entry=="0":
                break


class UI:
    def __init__(self, graph:Graph) -> None:
        self.graph=graph

    def print_graph(self):
        print(self.graph)

    # print("\t1. Get number of vertices")
    def vertecies_count(self):
        print(f"The vertecies number is:{self.graph.vertecies_count}")

    # print("\t2. Get number of edges")
    def edge_count(self):
        print(f"Edge number is {len(self.graph.edges)}")

    # print("\t3. Show all vertices")
    def show_vertecies(self):
        vertecies=self.graph.vertecies
        for vertex in vertecies:
            print(vertex)

    # print("\t4. Check if edge")
    def check_edge(self):
        outVert=int(input("Out-vertex:"))
        inVert=int(input("In-vertex:"))
        print(f"{self.graph.has_edge(outVert, inVert)}")

    # print("\t5. In degree and out degree of a vertex")
    def in_out_degree_vertex(self):
        vertex=int(input("Enter vertex:"))
        print("The out degree is ", self.graph.degree_out(vertex))
        print("The in degree is ", self.graph.degree_in(vertex))

    # print("\t6. Show outbound and inbound edges of a vertex")
    def in_out_edges(self):
        vertex=input("Vertex:")
        edges_out=self.graph.out_edges(vertex)
        edges_in=self.graph.out_edges(vertex)
        print("In-going edges")
        for edge in edges_in:
            print(edge)
        print("Out-going edges")
        for edge in edges_out:
            print(edge)

    # print("\t7. Get cost of an edge")
    def get_edge_cost(self):
        out_vertex=input("Enter the out vertex:")
        in_vertex=input("Enter the in vertex:")
        edge=self.graph.get_edge(out_vertex, in_vertex)
        if edge is not None:
            print(edge.cost)
        else:
            print("The edge does not exist")


    # print("\t8. Modify cost of an edge")
    def modify_edge_cost(self):
        in_vertex=int(input("Enter the in-bound:"))
        out_vertex=int(input("Enter the out-bound:"))
        new_cost=int(input("Enter new edge cost:"))
        self.graph.remove_edge(out_vertex, in_vertex)
        self.graph.add_edge(new_cost, out_vertex, in_vertex)

    # print("\t9. Add vertex")
    def add_vertex(self):
        self.graph.add_vertex(int(input("Vertex:")))
    # print("\t10. Remove vertex")
    def remove_vertex(self):
        self.graph.remove_vertex(int(input("Vertex:")))
    # print("\t11. Add edge")
    def add_edge(self):
        self.graph.add_edge(int(input("Weight")), int(input("Vertex 1:")), int(input("Vertex 2:")))
    # print("\t12. Remove edge")
    def remove_edge(self):
        self.graph.remove_edge(int(input("Vertex 1:")), int(input("Vertex2:")))

    # print("\t13. Replace current graph with a random graph")
    def get_random_graph(self):
        pass

    # print("\t14. Read graph from file")
    def get_file_graph(self):
        pass

    # print("\t15. Write the current graph to a file")
    def write_to_file_graph(self):
        pass

    # print("\t16. Make a copy of the graph")
    # print("\t17. Revert graph ")
    # print("\t18. Shortest path from one edge to another")
    # print("\t0. EXIT")


def start():
    ui=UI( Graph([x for x in range(1,10)], [Edge(1, 1,2), Edge(69, 1,5), Edge(80 ,2,8)] ))
    menu=Menu()
    menu.add_entry(ui, "Exit", UI.vertecies_count)
    menu.add_entry(ui, "Show graph", UI.print_graph)
    menu.add_entry(ui, "Get number of vertices", UI.vertecies_count)
    menu.add_entry(ui, "Get number of edges", UI.edge_count)
    menu.add_entry(ui, "Show all vertices", UI.show_vertecies)
    menu.add_entry(ui, "Check if edge", UI.check_edge)
    menu.add_entry(ui, "In degree and out degree of a vertex", UI.in_out_degree_vertex)
    menu.add_entry(ui, "Show outbound and inbound edges of a vertex", UI.in_out_edges)
    menu.add_entry(ui, "Get cost of an edge", UI.get_edge_cost)
    menu.add_entry(ui, "Modify cost of an edge", UI.modify_edge_cost)
    menu.add_entry(ui, "Add vertex", UI.add_vertex)
    menu.add_entry(ui, "Remove vertex", UI.remove_vertex)
    menu.add_entry(ui, "Add edge", UI.add_edge)
    menu.add_entry(ui, "Replace current graph with a random graph", UI.get_random_graph)
    # menu.add_entry(ui, "Read graph from file", UI.get_file_graph)
    # menu.add_entry(ui, "Write the current graph to a file", UI.write_to_file_graph)
    # menu.add_entry(ui, "Make a copy of the graph")
    # menu.add_entry(ui, "Revert graph ")
    # menu.add_entry(ui, "Shortest path from one edge to another")
    # print("\t0. EXIT")
    menu.start()


if __name__=="__main__":
    start()
