
class Edge:
    """Represents an undirected edge of a graph"""

    id_counter:int=0

    def __init__(self, u: int, v: int, is_directed:bool=False) -> None:
        self._id=Edge.id_counter
        self._u:int=u
        self._v:int=v
        self._is_directed:bool=is_directed

        Edge.id_counter+=1

    @property
    def id(self):
        return self._id

    @property
    def u(self)->int:
        return self._u
    
    @property
    def v(self)->int:
        return self._v
    
    @property
    def is_directed(self)->bool:
        return self._is_directed

    def __str__(self) -> str:
        if(self._is_directed):
            return '{}->{}'.format(self._u, self._v)
        return '{}-{}'.format(self._u, self._v)

    def __repr__(self) -> str:
        return str(self)

    

