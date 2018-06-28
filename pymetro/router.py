# coding=utf-8

from heapdict import heapdict

from .types import Route, Station
from . import data
from math import inf


class Router:

    def __init__(self):
        self.LINKS = data.LINKS + [(l[1], l[0], l[2]) for l in data.LINKS]
        self.ADJ_DICT = self.__build_adj_dict()
    
    def __build_adj_dict(self):
        adj = dict()
        for s in data.STATIONS:
            adj[s] = []
            for l in self.LINKS:
                if l[0] == s:
                    adj[s].append((l[1], l[2]))
        
        return adj
        
    
    def __relax(self, station, hd):
        for s in self.ADJ_DICT[station[0]]:
            if hd.get(s[0]) is not None:
                if station[1] + s[1] < hd[s[0]]:
                    hd[s[0]] = station[1] + s[1]
        
    def __get_dists(self, source):
        dists = {s: False for s in data.STATIONS}
    
        hd = heapdict()

        for s in data.STATIONS:
            hd[s] = inf

        hd[source.id_] = 0

        while hd:
            station = hd.popitem()
            dists[station[0]] = station[1]
            self.__relax(station, hd)
            
        return dists
    
    def __get_route(self, source, target, dists, dists_rev):
        route = [source.id_]
        time = [0]

        station = source.id_

        while station != target.id_:
            adj = [s[0] for s in self.ADJ_DICT[station] if s[0] not in route]

            if target.id_ in adj:
                route.append(target.id_)
                time.append([s[1] for s in self.ADJ_DICT[station] if s[0] == target.id_][0])
                station = target.id_

            else:
                next_station = min(adj, key=lambda x: dists[x] + dists_rev[x])
                _time = [s[1] for s in self.ADJ_DICT[station] if s[0] == next_station][0]
                route.append(next_station)
                time.append(_time)
                station = next_station

        return [Station(s) for s in route], sum(time)
        
    def make_route(self, source: Station, target: Station) -> Route:
        if not isinstance(source, Station) or not isinstance(target, Station):
            raise TypeError('Invalid input')
        
        dists = self.__get_dists(source)
        dists_rev = self.__get_dists(target)
        
        route, time = self.__get_route(source, target, dists, dists_rev)
        
        return Route(route, time)

