# coding=utf-8

from .types import Route, Station
from heapdict import heapdict
from pymetro.types import Route, Station
from data import STATIONS, LINKS, LINES

from collections import defaultdict

class Router:

    def __init__(self):
        self.graph = defaultdict(heapdict)
        for s1, s2, time in LINKS:
            self.graph[Station(s1)][Station(s2)]=time
            self.graph[Station(s2)][Station(s1)]=time

    def make_route(self, source: Station, target: Station) -> Route:
        queue = heapdict({key:float('inf') for key in self.graph})
        dijkstra = {key:float('inf') for key in self.graph}
        queue[source] = 0
        dijkstra[source] = 0
        paths = {source:[source]}
        while queue:
            node, k = queue.popitem()
            if node in self.graph:
                for neighbor in self.graph[node]:
                    t = neighbor
                    if t in queue:
                        new = k + self.graph[node][neighbor]
                        if new < dijkstra[t]:
                            if t in queue: queue[t] = new
                            dijkstra[t] = new
                            paths[t] = paths[node]+[t]
        return Route(paths[target], dijkstra[target])