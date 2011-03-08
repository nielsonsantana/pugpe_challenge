"""
Desafio PUG-PE  
ID: 2
Semana: 19/02/2011
Formulado por : Daker Fernandes e Marcel Caraciolo

Problema:

    Grafos sao redes consistindo de nos conectados por arcos. Em grafos direcionados, as conexoes entre os nos tem uma direcao;
    diferente de grafos nao direcionados, onde nao ha uma direcao. Neste problema vamos focar em grafos direcionados. O nosso problema envolve
    em descobrir o menor caminho entre dois nos dentro desse grafo. 

    A REPRESENTACAO DE UM GRAFO NO NOSSO PROBLEMA:
     GRAFO graph com 6 nos (A-F) e 8 arcos representado como um dicionario.
    
     graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
    
    Seu trabalho eh construir uma funcao shortest_path que receba um grafo como representado acima, o no de partida e o no de chegada e retorne
    uma lista ordenada do menor caminho a seguir a partir do no de partida ate o no de chegada. 
    
    Voce pode adicionar novos parametros a esta funcao se desejar (parametros opcionais que ajudem a resolver seu problema).
    
    >>> graph = {'A': ['B', 'C'],
                 'B': ['C', 'D'],
                 'C': ['D'],
                 'D': ['C'],
                 'E': ['F'],
                 'F': ['C']}
    >>> 

    >>> ret = short_path(graph,'A','E')
    >>> ret
    []
    >>> ret = short_path(graph,'A','D')
    >>> ret
    ['A','C', 'D']
    >>> ret = short_path(graph,'A','Z')
    >>> ret
    None
    >>> ret = short_path({}, 'A','Z')
    >>> ret
    None
    >>> ret = short_path(graph,'A','B')
    >>> ret
    ['A','B']

     
  Seu trabalho eh construir essa funcao.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""

def shortestpath(graph,start,end,path,pathes=[]):
    path = path[:]
    path+= [start]      
    
    if start == end:
        return path
       
    shortest = None
    for neighbor in graph[start]:
        if neighbor not in path:
            newPath = shortestpath(graph,neighbor,end,path)
            if newPath:
                if not shortest or len(newPath) <= len(shortest):
                    shortest = newPath[:]
                    pathes.append(tuple(shortest))  
    return shortest


def short_path(graph,start,end):
    if not graph or (start not in graph) or (end not in graph): return None   
    pathes = []
    shortestpath(graph,start,end,[],pathes)
    return pathes
    
    
    
import unittest


class Desafio2(unittest.TestCase):


    def test_empty_graph(self):
        graph = {}
        self.assertEqual(None,
                    short_path(graph,'A','B'))

    def test_unknown_node(self):
        graph = {'A': ['B', 'C'],
                     'B': ['C', 'D'],
                     'C': ['D'],
                     'D': ['C'],
                     'E': ['F'],
                     'F': ['C']}
        self.assertEqual(None, short_path(graph,'A','Z'))


    def test_inexistent_path(self):
        graph = {'A': ['B', 'C'],
                     'B': ['C', 'D'],
                     'C': ['D'],
                     'D': ['C'],
                     'E': ['F'],
                     'F': ['C']}
        self.assertEqual([], short_path(graph,'A','E'))

    def test_simple_path(self):
        graph = {'A': ['B', 'C'],
                     'B': ['C', 'D'],
                     'C': ['D'],
                     'D': ['C'],
                     'E': ['F'],
                     'F': ['C']}
        self.assertEqual([('A','B')], short_path(graph,'A','B'))

    def test_complex_path(self):    
        graph = {'A': ['B', 'C'],
               'B': ['D', 'E'],
               'C': ['D'],
               'D': ['E'],
               'E': []}
        self.assertEqual([('A','B','E')], short_path(graph,'A','E')) 
   

    def test_multiple_path(self):
        graph = {'A': ['B', 'C'],
                     'B': ['C', 'D'],
                     'C': ['D'],
                     'D': ['C'],
                     'E': ['F'],
                     'F': ['C']}
        sp = short_path(graph,'A','D')
        sp.sort()
        self.assertEqual([ ('A','B','D'),('A','C','D')],sp)


if __name__ == '__main__':
    unittest.main()    
