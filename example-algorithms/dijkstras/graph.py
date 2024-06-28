import itertools
from collections import namedtuple

class Graph:

	Edge = namedtuple("Edge", ["node1", "node2", "weight"])
	AdjcentNode = namedtuple("AdjcentNode", ["node", "weight"])

	def __init__(self, *args, **kwargs):
		self.graph = {}
		self.heuristicGraph = {}
		self.description = ""

	def _insertToGraph(self, fromNode, toNode=None, weight=None, heuristic=0)-> None:
		if weight!=None:
			if (not heuristic) and fromNode not in self.graph:
				self.graph[fromNode] = {}

			elif heuristic and fromNode not in self.heuristicGraph:
				self.heuristicGraph[fromNode] = {}

			if toNode!=None:
				if heuristic:
					self.heuristicGraph[fromNode][toNode] = weight
				else:
					self.graph[fromNode][toNode] = weight
		
		else:
			if fromNode not in self.graph:
				self.graph[fromNode] = set()

			if toNode!=None:
				self.graph[fromNode].add(toNode)

	def add(self, fromNode: object, toNodes: iter=None, weights: iter=None, edgeType: int=0, heuristic: int=0)-> None:
		"""
		formNode:	a immutable object (str, int, etc)

		toNodes:	an iterable object

		weights:	an iterable object

		edgeType: {0: undirected, 1: directed}
		"""

		if weights!=None:
			assert len(toNodes)==len(weights), "numbers weights does not match to the numbers of edges"
			
			if edgeType:
				for node, weight in zip(toNodes, weights):
					if heuristic:
						self._insertToGraph(fromNode, node, weight, heuristic=1)
					else:
						self._insertToGraph(fromNode, node, weight)
						
			else:
				for node, weight in zip(toNodes, weights):
					if heuristic:
						self._insertToGraph(node, fromNode, weight, heuristic=1)
						self._insertToGraph(fromNode, node, weight, heuristic=1)
					else:
						self._insertToGraph(node, fromNode, weight)
						self._insertToGraph(fromNode, node, weight)

		elif toNodes!=None:
			if edgeType:
				for node in toNodes:
					self._insertToGraph(fromNode, node)
			else:
				for node in toNodes:
					self._insertToGraph(node, fromNode)
					self._insertToGraph(fromNode, node)
		else:
			self._insertToGraph(fromNode)

	def addFromDict(self, fromNode:object, nodesDict: dict, edgeType: int=0)-> None:
		"""
		Used when, edges have weights to them

		formNode:	a immutable object (str, int, etc)

		nodesDict:	dict(node:weight)
		weight between node fromNode and node(the key)

		edgeType: {0: undirected, 1: directed}
		"""
		toNodes = [key for key in nodesDict.keys()]
		weights = [key for key in nodesDict.values()]
		self.add(fromNode, toNodes, weights, edgeType)

	def addHeuristicFromDict(self, fromNode: object, nodesDict: dict, edgeType: int=0)-> None:
		"""
		Used when, edges have weights to them

		formNode:	a immutable object (str, int, etc)

		nodesDict:	dict(node:heuristic)
		weight between node fromNode and node(the key)

		edgeType: {0: undirected, 1: directed}
		"""
		toNodes = [key for key in nodesDict.keys()]
		heuristics = [key for key in nodesDict.values()]
		self.add(fromNode, toNodes, heuristics, edgeType=0, heuristic=1)

	def __str__(self)-> str:
		return "\n".join([self.description]+[f"{node}:{edge}" for node, edge in self.graph.items()])


	def getHeuristic(self, fromNode: object, toNode: object)-> int:
		"""
		returns the stored heuristic between the from-node to to-node
		if theirs nothing returns None
		"""
		return self.heuristicGraph.get(fromNode, {}).get(toNode, None)


	def getWeight(self, fromNode: object, toNode: object)-> int:
		"""
		returns the stored weight of edge between the from-node to to-node
		if theirs nothing returns None
		"""
		return self.graph.get(fromNode, {}).get(toNode, None)

	def getPathCost(self, path: list)-> int:
		"""
		returns the cost of traversing the path
  
		path: list (e.g. [start-node, n2, n3, ... end-node])
		"""
		cost = 0
		start = path[0]
		for n in itertools.islice(path, 1, len(path)):
			cost+=self.getWeight(start, n)
			start=n
		return cost

	@property
	def nodes(self)-> "generator":
		"returns Nodes of graph as iterable"
		seen = set()
		for root, nodes in self.graph.items():
			if root not in seen:
				yield root
				seen.add(root)

			for node in nodes:
				if node not in seen:
					yield node
					seen.add(node)

	@property
	def edges(self)-> "generator":
		"""
		returns tuple (from-node, to-node, edge-weight) as 
		iterable edge weight: None if weight are not given
		"""
		for root, nodes in self.graph.items():
			if type(nodes)==set:
				for node in nodes:
					yield self.Edge(root, node, None)
			else:
				for node, weight in nodes.items():
					yield self.Edge(root, node, weight)

	def getAdjacentNodes(self, node: object)-> "namedtuple(node, weight)":
		"""
		returns tuple (to-node, edge-weight) as 
		iterable edge weight: None if weight are not given
		"""
		adjNodes = self.graph.get(node, [])
		if type(adjNodes)==set:
			for n in adjNodes:
				yield self.AdjcentNode(n, None)

		elif type(adjNodes)==dict:
			for node, weight in adjNodes.items():
				yield self.AdjcentNode(node, weight)

	def isEdgeBetweenNodes(self, parentNode: object, node: object)-> bool:
		'return boolean, if edge between "parentNode" and "node"'
		return parentNode in self.graph and node in self.graph[parentNode]

