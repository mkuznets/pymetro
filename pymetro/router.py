# coding=utf-8

from heapdict import heapdict

from .types import Route, Station

from .data import LINKS


class Router:

    def __init__(self):
        self.graph = dict()
        for el in LINKS:
            if not el[0] in self.graph:
                self.graph[el[0]] = dict()
            self.graph[el[0]][el[1]] = el[2]
            
            if not el[1] in self.graph:
                self.graph[el[1]] = dict()
            self.graph[el[1]][el[0]] = el[2]

    def make_route(self, source: Station, target: Station) -> Route:
        #print(source, target)
        parent={source:None}
        d=heapdict()
        for i in self.graph:
            d[i]=float('inf')
        d[source.id_]=0
        #print(list(d.items()))
        while True:
            u = d.popitem()
            #print(u, target)
            if u[0] == target.id_:
                #print(parent)
                fg = Station(u[0])
                route = [fg]
                time = u[1]
                while not parent[fg] is None:
                    fg = parent[fg]
                    route.append(fg)
                return Route(route[::-1], time)
            
            for el in self.graph[u[0]]:
                if el in d:
                    if d[el] >= u[1] + self.graph[u[0]][el]:
                        d[el] = u[1] + self.graph[u[0]][el]
                        parent[Station(el)] = Station(u[0])
