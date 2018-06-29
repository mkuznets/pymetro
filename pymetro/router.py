# coding=utf-8

from heapdict import heapdict

from .types import Route, Station

import data 
import copy
import math
from collections import defaultdict

class Router:

    def __init__(self):
        
        self.route = []
        self.time = []
        self.G = defaultdict(dict)
        
        for i in LINKS:
            self.G[Station(i[0])][Station(i[1])] = i[2]
            self.G[Station(i[1])][Station(i[0])]=  i[2]
            

    def make_route(self, source: Station, target: Station) -> Route:

        que = heapdict() 
        dist = {}

        print(source)

        for i in self.G:
   
            if i.id_ == source.id_:
                que[i] = 0
                dist[i] = 0
            else:
                que[i] = math.inf
                dist[i] = math.inf

        routes = defaultdict(list)
        routes[source] = []

        while que:
            
            item = que.popitem()

            if item[0] in self.G:
        
                for i in self.G[item[0]]:
       
                    if que.get(i):

                        if item[1] + self.G[item[0]][i] < que[i]:
    
                            que[i] = item[1] + self.G[item[0]][i]
                            dist[i] = item[1] + self.G[item[0]][i]
                            a = copy.copy(routes[item[0]])
                            a.append(i)
                            routes[i] = a

        path = [source] + routes[target]
        return Route(path, dist[target])




    
##
##
##source, target = Station(7), Station(10)
##a = Router()
##print(a.make_route(source, target).path)

                        

##        
##    def make_route(self, source: Station, target: Station):
##
##        s_id = source.id_
##        t_id = target.id_
##   
##        p_hood = defaultdict()
##        p_hood[source] = source
##
##        que = heapdict()  # 'A': {inf}
##        dist = {}
##
##        
##        routes = {source:[source]}
##        time = 0
##
##        for i in self.G:
##            if i == s_id:
##                que[i] = 0
##                dist[i] = 0
##            else:
##                que[i] = math.inf
##                dist[i] = math.inf
##        print(routes)
##        print(que)
##        print(dist)
##
##        while que:
##
##            item = que.popitem()  # ["B", 7]
##            if 1== 2:
##                1
##
####            if item[0] == t_id:
####                fg = Station(item[0])
####                route = [fg]
####                time = item[1]
####    
####                while not p_hood[fg] is None:
####                    fg = p_hood[fg]
####                    route.append(fg)
####                return Route(route[::-1], time)
##
##            else:
##                for i in self.G[item[0]]:
##                    print(i)
##                    if i[0] in que:
##                        print(i[1])
##                        if dist[i[0]] > i[1] + item[1]:
##                            que[i[0]] = i[1] + item[1]
##                            dist[i[0]] = i[1] + item[1]
##                            routes[i[0]] = routes[item[0]] + [i[0]]
####                            p_hood[Station(i[0])] = Station(item[0])
##                            
##                print(p_hood)
##
####               for i in G[v]:#sorted(G[v], key=lambda x: x[1]):
####                 if dist[i[0]] > dist[v] + i[1]:
####                    dist[i[0]] = dist[v] + i[1]
####                    que[i[0]] = i[1]
                        


##
##dist = defaultdict(int)
##
##for i in G:
##    if i == 'A':
##        dist[i] = 0
##    else:
##        dist[i] = math.inf
##
##
##def req(v, dist, G, parent=''):
##
##    all_ = len(G[v])
##
##    que = heapdict()
##    print(G[v])
##    print(dist)
##
##    for i in G[v]:#sorted(G[v], key=lambda x: x[1]):
##        if dist[i[0]] > dist[v] + i[1]:
##            dist[i[0]] = dist[v] + i[1]
##            que[i[0]] = i[1]
##    print(dist)
##    a = que.popitem()
##    print(a)
##
##    if a[0] != parent:
##        try:
##           a = que.popitem()
##        except:
##            return
####    print(dist[a[0]])
####    if dist[a[0]] > dist[v] + a[1]:
####        dist[a[0]] = dist[v] + a[1]
##    req(a[0], dist, G, v)
##    return
##
###print(dist)
##req('A', dist, G, parent='A')
##print(dist)
##

##
##def req(v, dist, G, parent=''):
##
##    all_ = len(G[v])
##
##    for i in sorted(G[v], key=lambda x: x[1]):
##        all_ -=1
##
##        if i[0] == parent:
##            continue
##        else:
##            if dist[i[0]] > i[1]:
##                dist[i[0]] = dist[v] + i[1]
##                req(i[0], dist, G, v)
##
##    if all_ <= 0:
##        return
