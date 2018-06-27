# coding=utf-8

from heapdict import heapdict
from data import *
from collections import defaultdict
from .types import Route, Station


class Router:

    def __init__(self):
        self.links = defaultdict(list)

        for link in LINKS:
            self.links[link[0]].append((link[1], link[2]))
            self.links[link[1]].append((link[0], link[2]))


    def make_route(self, source: Station, target: Station) -> Route:

        time = heapdict()
        path = defaultdict(list)

        for node in self.links:
            time[node] = 10000

        time[source.id_] = 0
        start = source.id_

        currtime = 0
        while time:
            neighbors = self.links[start]

            for neighbor in neighbors:
                if neighbor[0] in time and neighbor[1] + currtime < time[neighbor[0]]:
                    time[neighbor[0]] = neighbor[1] + currtime
                    path[neighbor[0]] = path[start] + [Station(start)]

            start, currtime = time.popitem()
            if start == target.id_:
                break

        r = Route(path[start] + [Station(start)], currtime)

        return r
