# coding=utf-8

from heapdict import heapdict

from .types import Route, Station


class Router:

    def __init__(self):
        ...

    def make_route(self, source: Station, target: Station) -> Route:
        ...
