"""
Desafio PUG-PE  
ID: 1
Semana: 11/02/2011

Problema:

    Dado uma lista de elementos, o objetivo eh converter esta lista em uma lista de sub-listas de elementos consecutivos duplicados.
    Assim que um elemento subsequente for diferente do anterior, a sublista eh gerada e passa para o proximo elemento. Entao 
    no exemplo abaixo dado 5 a's quando encontrar um b ele gera a sublista de 5 a's e comeca a gerar a sublista de b's ate encontrar um
    elemento que nao seja b, e assim sucessivamente. 
    >>> x = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
    >>> ret = pack(x)
    >>> ret
    >>> [['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']]
    >>> x = ['a', 'b', 'c']
    >>> ret = pack(x)
    >>> ret 
    >>>[['a'], ['b'], ['c']]
    >>> x = []
    >>> ret = pack(x)
    >>> ret
    >>> []
     
  Seu trabalho eh construir essa lista de elementos.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""

import unittest


class Desafio1(unittest.TestCase):
	def test_pack_duplicates(self):
		sampleList = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
		self.assertEqual([['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']],
					pack(sampleList))
	def test_pack_duplicates2(self):
		sampleList = ['a','b','c','c','a','a','d','e','e','a']
		self.assertEqual([['a'],['b'],['c','c'],['a','a'],['d'],['e','e'],['a']],
					pack(sampleList))
	def test_pack_zero(self):
		sampleList = []
		self.assertEqual([],
					pack(sampleList))
	def test_lista_um_elemento(self):
		self.assertEquals([[1]], pack([1]))
	def test_lista_dois_elementos_iguais(self):
		self.assertEquals([[1, 1]], pack([1, 1]))


#Minha funcao para a competicao
def pack(list):
	result = []
	inic = 0 #Inicio de cada sub Lista
	list.append(0)

	for fim, elem in enumerate(list[1:]):
		if list[fim] != elem:
			result.append(list[inic:fim+1])
			inic = fim+1
	return result


def pack1(list):
	char = '' if(not list) else list[0]
	result = []
	inic = fim = 0 #Inicio e o fim de cada sub Lista

	for elem in list[1:]:
		fim += 1
		if(char != elem):
			result.append(list[inic:fim])
			char = elem
			inic = fim
	if(list):
		result.append(list[inic:])
	return result


if __name__ == '__main__':
    unittest.main()    
