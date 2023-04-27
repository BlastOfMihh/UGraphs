import unittest
from Graph import Graph
from Graph import Edge



class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph=Graph([x for x in range(1,10)], [Edge(120, 1, 2), Edge(1233, 1, 3), Edge(30,3,2)])
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_has_edge(self):
        self.assertTrue(self.graph.has_edge(1,2))
        self.assertTrue(self.graph.has_edge(1,3))
        self.assertTrue(self.graph.has_edge(3,2))

    def test_add_edge(self):
        self.graph.add_edge(1, 1, 9)
        self.assertTrue(self.graph.has_edge(1,9))

    def test_degree(self):
        self.assertTrue(self.graph.degree_out(1)==2)
        self.assertTrue(self.graph.degree_in(1)==0)
        self.assertTrue(self.graph.degree_in(2)==2)

    def test_remove_edge(self):
        self.graph.remove_edge(1,2)
        self.assertTrue(self.graph.has_edge(1,2)==False)
        self.assertTrue(self.graph.has_edge(1,3))
        self.graph.remove_edge(3,2)
        self.assertTrue(self.graph.has_edge(3,2)==False)





if __name__=="__main__":
    graph=Graph([x for x in range(1,10)], [Edge(120, 1, 2), Edge(1233, 1, 3), Edge(30,3,2)])
    print(graph)
    unittest.main()
