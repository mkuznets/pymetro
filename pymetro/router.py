# coding=utf-8

from heapdict import heapdict

from pymetro.types import Route, Station
from pymetro.data import STATIONS, LINKS


class Router:
    def __init__(self):
        self.neighbours = dict()
        for i in LINKS:
            if i[0] in self.neighbours:
                self.neighbours[i[0]].append((i[1], i[2]))
            else:
                self.neighbours[i[0]] = [(i[1], i[2])]
        for i in LINKS:
            if i[1] in self.neighbours:
                self.neighbours[i[1]].append((i[0], i[2]))
            else:
                self.neighbours[i[1]] = [(i[0], i[2])]

    def make_route(self, source: Station, target: Station) -> Route
    idx_s = source.id_
    idx_c = source.id_

    inf = float('Inf')
    visited = list()

    distances = heapdict({key: inf for key in STATIONS.keys()})
    distances[idx_s] = 0

    distances_topop = heapdict({key: inf for key in STATIONS.keys()})
    distances_topop[idx_s] = 0

    pathes = {key: [] for key in STATIONS.keys()}

    while len(visited) != len(STATIONS):
        v = distances_topop.popitem()
        visited.append(v[0])

        if v[0] in self.neighbours:

            for station in self.neighbours[v[0]]:
                if not station[0] in visited:
                    if distances[station[0]] > distances[v[0]] + station[1]:
                        distances[station[0]] = distances[v[0]] + station[1]
                        distances_topop[station[0]] = distances[v[0]] + station[1]
                        pathes[station[0]] = pathes[v[0]] + [Station(v[0])]

    pathes[target.id_].append(Station(target.id_))
    return Route(pathes[target.id_], distances[target.id_])
