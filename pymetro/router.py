# coding=utf-8

from .types import Route, Station

from heapdict import heapdict
from pymetro.types import Route, Station
from data import STATIONS, LINKS, LINES

from collections import defaultdict, deque

class Router:

    def __init__(self):
        self.graph = defaultdict(list)
        for s1, s2, time in LINKS:
            self.graph[Station(s1)].append(Route([Station(s1),Station(s2)], time))
            self.graph[Station(s2)].append(Route([Station(s2),Station(s1)], time))
        self.time = 0
        self.path = []

    def make_route(self, source: Station, target: Station) -> Route:
        dijkstra = {key:float('inf') for key in self.graph}
        dijkstra[source] = 0
        queue = deque([source])
        seen = set([source])
        paths = {source:[source]}
        while queue:
            node = queue.popleft()
            seen.update([node])
            if node in self.graph:
                for route in self.graph[node]:
                    if route.path[0] == node: s, t = route.path[0], route.path[1]
                    else: s, t = route.path[1], route.path[0]
                    if t not in seen:
                        new = dijkstra[node] + route.time
                        if new < dijkstra[t]:
                            dijkstra[t] = new
                            paths[t] = paths[node]+[t]
                        queue.append(t)
        self.time = dijkstra[target]
        self.path = paths[target]
        return self