# coding=utf-8

from heapdict import heapdict

from .types import Route, Station

from . import data


class Router:

    def __init__(self):
        self.__queue = heapdict()
        for station in data.STATIONS:
            self.__queue[station] = (float('Inf'), station, [])

    def __get_all_links(self, source):
        id_ = source.id_
        links = []
        for link in data.LINKS:
            if link[0] == id_ or link[1] == id_:
                links.append(link)
        return sorted(links, key=lambda link: link[2])

    def __compute_new_distance(self, between_dist, source):
        dist_to_source = self.__queue[source.id_][0]
        return between_dist + dist_to_source

    def __update_target_path(self, new_dist, source, target_id):
        if new_dist < self.__queue[target_id][0]:
            path = self.__queue[source.id_][2]
            target_station = Station(target_id)
            self.__queue[target_id] = (new_dist, target_id, path + [target_station])

    def __recompute_distance(self, link, source):
        if link[0] == source.id_:
            target_id = link[1]
        else:
            target_id = link[0]
        if target_id in self.__queue:
            new_dist = self.__compute_new_distance(link[2], source)
            self.__update_target_path(new_dist, source, target_id)

    def __compute_distances(self, source):
        links = self.__get_all_links(source)
        for link in links:
            self.__recompute_distance(link, source)

    def __get_path(self, target):
        source = self.__queue.peekitem()
        while source[0] != target.id_:
            self.__compute_distances(Station(source[0]))
            self.__queue.popitem()
            source = self.__queue.peekitem()
        return source[1]

    def make_route(self, source: Station, target: Station) -> Route:
        self.__queue[source.id_] = (0, source.id_, [source]) # (time, costyl', path)
        route = self.__get_path(target)
        return Route(route[2], route[0])
