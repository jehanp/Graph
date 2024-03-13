
import random

from vertex import Vertex
from edge import Edge

class Graph:
    """Represents an undirected graph"""
    def __init__(self) -> None:
        self.vertices:Vertex=[]
        self.edges:Edge=[]

    def add_vertices(self, vertices)->None:
        for v in vertices:
            self.add_vertex(v)
    def add_vertex(self, name:str)->None:
        self.vertices.append(Vertex(name))
    
    def add_edge_named(self, u:str, v:str)->None:
        vertex_u:Vertex= [x for x in self.vertices if x.name==u][0]
        vertex_v:Vertex= [x for x in self.vertices if x.name==v][0]
        self.add_edge(vertex_u.id,vertex_v.id)

    def add_edge(self, u:int, v:int):
        if(not any(x.u==u and x.v==v for x in self.edges) and
           not any(x.u==v and x.v==u for x in self.edges)):
            self.edges.append(Edge(u,v))

            vertex_u:Vertex = self.vertices[u]
            vertex_u.add_undirected_edge(Edge(u,v))
        
            vertex_v:Vertex = self.vertices[v]
            vertex_v.add_undirected_edge(Edge(v,u))
                

    def random_init(self, vertexCount:int, edgeCount:int)->None:
        for number in range(vertexCount):
            self.vertices.append(Vertex(number))

        for number in range(edgeCount):
            u=random.randrange(vertexCount)
            v=random.randrange(vertexCount)
            if(u!=v):
                edge=Edge(u,v)
                self.edges.append(edge)
                
                if(not any(x for x in self.vertices[u].i_undirected if x.u==u and x.v==v)):
                    vertex_u:Vertex = self.vertices[u]
                    vertex_u.add_undirected_edge(Edge(u,v))

                if(not any(x for x in self.vertices[v].i_undirected if x.u==v and x.v==u)):
                    vertex_v:Vertex = self.vertices[v]
                    vertex_v.add_undirected_edge(Edge(v,u))

    

    def print(self):
        print('vertices: ')
        for v in self.vertices:
            print(v.name, end=' --- ')
            for e in v.i_undirected:
                print('{}-{}'.format(self.vertices[e.u].name, self.vertices[e.v].name), end=', ')
            print()

    def print_edges(self)->None:
        print('edges: {}'.format(len(self.edges)))
        for e in self.edges:
            print(e)
            
            
        

g=Graph()
#g.random_init(5,8)
g.add_vertices(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'])
g.add_edge_named('A','B')
g.add_edge_named('A','E')
g.add_edge_named('A','F')

g.add_edge_named('B','A')
g.add_edge_named('B','C')
g.add_edge_named('B','F')

g.add_edge_named('C','B')
g.add_edge_named('C','D')
g.add_edge_named('C','G')

g.add_edge_named('D','C')
g.add_edge_named('D','G')
g.add_edge_named('D','H')

g.add_edge_named('E','A')
g.add_edge_named('E','F')
g.add_edge_named('E','I')

g.add_edge_named('F','A')
g.add_edge_named('F','B')
g.add_edge_named('F','E')
g.add_edge_named('F','I')

g.add_edge_named('G','C')
g.add_edge_named('G','D')
g.add_edge_named('G','J')
g.add_edge_named('G','K')
g.add_edge_named('G','L')

g.add_edge_named('H','D')
g.add_edge_named('H','L')

g.add_edge_named('I','E')
g.add_edge_named('I','F')
g.add_edge_named('I','J')
g.add_edge_named('I','M')
g.add_edge_named('I','N')

g.add_edge_named('J','I')
g.add_edge_named('J','G')
g.add_edge_named('J','K')

g.add_edge_named('K','G')
g.add_edge_named('K','J')
g.add_edge_named('K','N')
g.add_edge_named('K','O')

g.add_edge_named('L','G')
g.add_edge_named('L','H')
g.add_edge_named('L','P')

g.add_edge_named('M','I')
g.add_edge_named('M','N')

g.add_edge_named('N','I')
g.add_edge_named('N','K')
g.add_edge_named('N','M')

g.add_edge_named('O','K')
g.add_edge_named('O','P')

g.add_edge_named('P','L')
g.add_edge_named('P','O')

g.print()
g.print_edges()