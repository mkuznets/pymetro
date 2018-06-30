# coding=utf-8

from heapdict import heapdict
from collections import defaultdict
from pymetro.types import Route, Station
from pymetro.data import STATIONS, LINKS


class Router:

    def __init__(self):
        self.graph = defaultdict(heapdict)
        for i in LINKS:
            self.graph[Station(i[0])][Station(i[1])]=i[2]
            self.graph[Station(i[1])][Station(i[0])]=i[2]

    def make_route(self, source: Station, target: Station) -> Route:
        queue = heapdict()
        for i in self.graph:
            queue[i] = float('inf')
        parent = {}
        for i in self.graph:
            parent[i] = float('inf')
        queue[source], parent[source] = 0, 0
        visited = {source:[source]}
        while len(queue):
        	#print(len(queue)
            nearest, nearest_dist = queue.popitem()
            for connection in self.graph[nearest]:
                if connection in queue:
                    updated = self.graph[nearest][connection] + nearest_dist
                    if parent[connection] > updated:
                        if connection in queue: 
                            queue[connection] = updated
                        parent[connection] = updated
                        visited[connection] = visited[nearest] + [connection]
                        #print(visited[connection])
        #print(visited)
        self.time = parent[target]
        self.path = visited[target]
        return self

