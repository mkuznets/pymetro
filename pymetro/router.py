# coding=utf-8

from heapdict import heapdict
from .data import *
from collections import defaultdict
from .types import Route, Station


class Router:

    def __init__(self):
        self.structure = defaultdict(list)

        for elem in LINKS:
            self.structure[elem[0]].append((elem[1], elem[2]))
            self.structure[elem[1]].append((elem[0], elem[2]))

    def make_route(self, source: Station, target: Station) -> Route:

        weight = heapdict()
        for elem in self.structure:
            weight[elem] = float('inf')

        weight[source.id_] = 0
        not_visited = [True] * len(STATIONS)
        previous_stations = defaultdict(list)

        time = 0
        current_v = source.id_

        while not_visited[target.id_]:

            current_v, time = weight.popitem()
            not_visited[current_v] = False

            for v in self.structure[current_v]:

                if not_visited[v[0]] and time + v[1] < weight[v[0]]:
                    weight[v[0]] = time + v[1]
                    previous_stations[v[0]] = previous_stations[current_v] + [current_v]

        return Route([Station(elem) for elem in previous_stations[current_v] + [target.id_]], time)
    
