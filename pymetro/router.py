# coding=utf-8

from heapdict import heapdict

from .types import Route, Station
from .data import  LINKS
from copy import copy


class Router:

    def __init__(self):
        self.vertexes = {}
        for link in LINKS:
            station_1 = Station(link[0])
            station_2 = Station(link[1])
            weight = link[2]
            self.vertexes.setdefault(station_1, []).append((station_2, weight))
            self.vertexes.setdefault(station_2, []).append((station_1, weight))


    def make_route(self, source: Station, target: Station) -> Route:
        hd = heapdict()
        visited = {}
        path = {}
        hd[source] = 0
        path[source] = []
        while True:
            station, priority = hd.popitem()
            visited[station] = priority
            if station == target:
                break
            for edge in self.vertexes[station]:
                edge_target, weight = edge
                if edge_target not in visited:
                    concurrent_priority = weight + priority
                    if hd.get(edge_target):
                        if concurrent_priority < hd[edge_target]:
                            hd[edge_target] = concurrent_priority
                            path[edge_target] = path[station] + [station]
                    else:
                        hd[edge_target] = concurrent_priority
                        path[edge_target] = path[station] + [station]
        final_path = path[target] + [target]
        final_weight = visited[target]
        return Route(final_path, final_weight)