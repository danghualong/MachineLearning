#encoding=utf-8


class Graph(object):
    def __init__(self):
        self._vertexes=[]
        self._edges=[]

    def addVertex(self,vertex):
        self._vertexes.append(vertex)
    def addEdge(self,vFrom,vTo,weight=1):
        self._edges.append((vFrom,vTo,weight))
    def getVertexes(self):
        return self._vertexes
    def getEdges(self):
        return self._edges
    def getEdges(self,vHead):
        result=[]
        for edge in self._edges:
            if edge[0]==vHead:
                result.append(edge)
        return result

    def output(self):
        for v in self._vertexes:
            edges=self.getEdges(v)
            Graph._output(edges)

    @staticmethod
    def _output(edges):
        head="";
        if len(edges)>0:
            head=edges[0][0]
        head=head+" : "
        for edge in edges:
            head+= ("%s(%d),"%(edge[1],edge[2]))
        print head



if __name__=="__main__":
    graph=Graph()
    graph.addVertex("A")
    graph.addVertex("B")
    graph.addVertex("C")
    graph.addVertex("D")
    graph.addEdge("A","B")
    graph.addEdge("A","C")
    graph.addEdge("B","D")
    graph.addEdge("D","A")
    graph.addEdge("C","D")

    graph.output()


