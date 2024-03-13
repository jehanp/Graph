from edge import Edge

class Vertex:
    """Represents a vertex of a graph"""
    id_counter:int=0

    def __init__(self, name:str) -> None:
        self._id=Vertex.id_counter
        self._name=name

        self.i_undirected:Edge=[]
        self.i_in:Edge=[]
        self.i_out:Edge=[]

        Vertex.id_counter+=1

    @property 
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    def add_undirected_edge(self, e:Edge)->None:
        if(not any(x for x in self.i_undirected if x.u==e.u and x.v==e.v)):
            self.i_undirected.append(e)

    def print_simple(self):
        return '{}'.format(self._name)
    
    def print_detail(self):
        return '{}-{}, incident undirected edges:{}, incoming directed edges:{}, outgoing directed edges:{}'.format(self._id, self._name, len(self.i_undirected), len(self.i_in), len(self.i_out))

    def __str__(self) -> str:
        return self.print_simple()

    def __repr__(self) -> str:
        return str(self)
