# https://www.youtube.com/watch?v=zaBhtODEL0w
# BFS: Breadth First Search

import math
from collections import deque

class Graph:
    def __init__(self):
        self.hashMap = {} # maps the node ID to the node

    def addEdge(self, source, destination):
        d = self.getNode(destination)
        self.getNode(source).adjacent.append(d)

    def getNode(self, id):
        return self.hashMap[id]

    def getNodes(self):
        return self.hashMap.values()

    def hasPathDFS(self, source, destination):
        s = self.getNode(source)
        d = self.getNode(destination)
        visited = {}
        return hasPathDFS_dp(s, d, visited)

    def hasPathDFS_dp(self, source, destination, visited):
        if source.id in visited: return False
        visited.append(source.id)
        if source == destination: return True
        for child in source.adjacent:
            if hasPathDFS_dp(child, destination, visited): return True
        return False

    def hasPathDFS(self, source, destination):
        nextToVisit = deque(source)
        visited = {}
        while len(nextToVisit) > 0:
            node = nextToVisit.popleft()
            if node == destination: return True
            if node.id in visited: continue
            visited.append(node.id)
            for child in node.adjacent:
                nextToVisit.append(child)
        return False

class Node:
    def __init__(self, id = None):
        self.id = name
        self.adjacent = deque() # an efficient linked list
    




def calculateShortestPathFromSource(graph, source):
    source.setDistance(0)

    settledNodes = []
    unsettledNodes = []
    unsettledNodes.append(source)

    while len(unsettledNodes) != 0:
        currentNode = getLowestDistanceNode(unsettledNodes)
        unsettledNodes.remove(currentNode)


