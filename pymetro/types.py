# coding=utf-8

from typing import List

from . import data


class Station:

    def __init__(self, id_):

        if id_ not in data.STATIONS:
            raise ValueError('Invalid station id')

        self.id_ = id_

    def __eq__(self, other: 'Station'):
        return self.id_ == other.id_

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        station = data.STATIONS[self.id_]

        return '<Station: %s (line %s)>' % (station['name'], station['line'])


class Route:

    def __init__(self, path: List[Station], time: int):

        if not path:
            raise ValueError('no stations')

        self.path = path
        self.time = time

    def __repr__(self):
        return '<Route: from %s to %s>' % (self.path[0], self.path[-1])
