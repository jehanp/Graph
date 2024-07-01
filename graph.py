
import random
from typing import List

from vertex import Vertex
from edge import Edge

class Graph:
    """Represents an undirected graph"""
    def __init__(self) -> None:
        self.vertices:Vertex=[]
        self.edges:Edge=[]

    def get_vertex_named(self, v:str)->Vertex:
        return [x for x in self.vertices if x.name==v][0]
    def get_vertex(self, v:int)->Vertex:
        return [x for x in self.vertices if x.id==v][0]

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

    #undirected edge related functions
    def degree(self, v:str)->int:
        vertex:Vertex = self.get_vertex_named(v)
        return len(vertex.i_in)+len(vertex.i_out)+len(vertex.i_undirected)
    def end_vertices(self, e:Edge)->tuple:
        return (self.get_vertex(e.u).name,self.get_vertex(e.v).name)
    def opposite(self, v:Vertex, e:Edge)->Vertex:
        for edge in self.incident_edges(v.name):
            if((edge.u==e.u and edge.v==e.v) or (edge.u==e.v and edge.v==e.u)):
                #valid vertex found
                if(edge.u==v.id):
                    return self.vertices[edge.v]
                elif(edge.v==v.id):
                    return self.vertices[edge.u]
                else:
                    return None
    def incident_edges(self, v:str)->List[Edge]:
        vertex:Vertex=self.get_vertex_named(v)
        return vertex.i_undirected+vertex.i_in+vertex.i_out
    def adjacent_vertices(self, v:str)->List[Vertex]:
        adjacentVertices:Vertex=[]
        vertex:Vertex=self.get_vertex_named(v)
        for edge in self.incident_edges(v):
            adjacentVertices.append(self.opposite(vertex,edge))
        return adjacentVertices
    def are_adjacent(self,v:str, w:str)->bool:
        vertexV:Vertex=self.get_vertex_named(v)
        vertexW:Vertex=self.get_vertex_named(w)
        return any([e for e in self.edges if ((e.u==vertexV.id and e.v==vertexW.id) or (e.v==vertexV.id and e.u==vertexW.id))])

    #directed edge related functions
    def in_degree(self, v:str)->int:
        vertex:Vertex = self.get_vertex_named(v)
        return len(vertex.i_undirected)+len(vertex.i_in)
    def out_degree(self, v:str)->int:
        vertex:Vertex = [x for x in self.vertices if x.name==v][0]
        return len(vertex.i_undirected)+len(vertex.i_out)
    def in_incident_edges(self, v:str)->List[Edge]:
        vertex:Vertex = self.get_vertex_named(v)
        return vertex.i_in+vertex.i_undirected
    def out_incident_edges(self, v:str)->List[Edge]:
        vertex:Vertex = self.get_vertex_named(v)
        return vertex.i_in+vertex.i_undirected
            
    #traversal algorithms
    def dfs(self, v:str):
        vertex:Vertex=self.get_vertex_named(v)
        vertex.is_explored=True
        print('current vertex: {}'.format(vertex.name))
        #print('{}->'.format(vertex.name),end='')
        for edge in self.incident_edges(v):
            if not edge.is_explored:
                w:Vertex=self.opposite(vertex, edge)
                print('\tnext vertex: {}'.format(w.name))
                if not w.is_explored:
                    print('\t\tnext vertex: {} not explored, moving to it'.format(w.name))
                    edge.is_discovery_edge=True
                    self.dfs(w.name)
                else:
                    print('\t\tnext vertex: {} already explored'.format(w.name))
                    edge.is_back_edge=True


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
    def create_test_graph():
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

        return g

    def print(self):
        print('vertices: ')
        for v in self.vertices:
            print(v.name, end=' --- ')
            for e in v.i_undirected:
                print('{}-{}'.format(self.vertices[e.u].name, self.vertices[e.v].name), end=', ')
            print()

    def print_edges(self, edge_list:List[Edge]=None)->None:
        el = edge_list if edge_list else self.edges
        print('edges: {}'.format(len(el)))
        for e in el:
            print('{}-{}'.format(self.get_vertex(e.u).name,self.get_vertex(e.v).name))
            
g=Graph.create_test_graph()

#g.print()
#g.print_edges()

#print('degree of A: {}'.format(g.degree('A')))
#print('end vertices of edge: {}'.format(g.end_vertices(g.get_vertex_named('A').i_undirected[0])))

#print('incident edges of A: ' ,end='')
#g.print_edges(g.incident_edges('A'))

#print(g.opposite(g.get_vertex_named('G'),g.incident_edges('G')[0]))
#print(g.opposite(g.get_vertex_named('K'),Edge(11,10)))

#print('adjacent vertices of G: {}'.format(g.adjacent_vertices('G')))

#print(g.are_adjacent('A','I'))

#print('indegree of A: {}'.format(g.in_degree('A')))
#print('indegree of G: {}'.format(g.in_degree('G')))

#print(len(g.in_incident_edges('G')))
#g.print_edges(g.in_incident_edges('G'))

g.dfs('A')