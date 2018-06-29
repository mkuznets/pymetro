# coding=utf-8

from heapdict import heapdict

from .types import Route, Station

from data import LINES, STATIONS, LINKS

class Router:

    def __init__(self):
        graph = {}
        for source, target, time in LINKS:
            source, target = Station(source), Station(target)
            if source not in graph:
                graph[source] = {target: time}
            else:
                graph[source][target] = time
            if target not in graph:
                graph[target] = {source: time}
            else:
                graph[target][source] = time
        self.graph = graph

    def make_route(self, source: Station, target: Station) -> Route:
        queue = heapdict()
        parent = {}
        visited = {}
        queue[source] = 0
        parent[source] = False
        while queue:
            u, length = queue.popitem()
            visited[u] = True
            for v in self.graph[u].keys():
                if v not in visited:
                    if v in queue:
                        nxt = queue[v]
                    else:
                        nxt = float('inf')
                    new_length = length + self.graph[u][v]
                    if new_length < nxt:
                        queue[v], parent[v] = new_length, u
            if u == target: 
                path = []
                while u:
                    path.append(u)
                    u = parent[u]
                return Route([number for number in list(reversed(path))], length)