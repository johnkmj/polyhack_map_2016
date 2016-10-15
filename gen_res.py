import xml.etree.ElementTree
import pandas as pd
import csv
import math
import sys
import itertools


class Vertex:

    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:

    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq


def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                    % (current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                    % (current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v)
                           for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


def read_nodes():
    with open('lib/names.csv', 'r') as csvfile:
        reader = list(csv.reader(csvfile, delimiter='\n'))
        return list(itertools.chain.from_iterable(reader))


def gen_graph(arr):
    g = Graph()

    nodes = read_nodes()

    for vertex in nodes:
        g.add_vertex(vertex)

    for y in range(0, len(arr)):
        for x in range(0, len(arr)):
            if arr[x][y] != 0:
                g.add_edge(nodes[x], nodes[y], arr[x][y])


def gen_shortest_path(point_1, point_2)
    dijkstra(g, g.get_vertex(point_1), g.get_vertex(point_2))

    target = g.get_vertex(point_2)
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' % (path[::-1])
    return path


def generate_graph():
    adj = pd.read_csv("lib/adj.csv", sep=',')
    rooms = pd.read_csv("lib/names.csv", sep='\n')
    import csv

    adj = []
    with open('lib/adj.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            adj.append(row)

    locations = []
    with open('lib/locations.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            locations.append(row)

    N = len(adj)

    w, h = N, N
    arr = [[0 for x in range(w)] for y in range(h)]

    for i in range(N):
        for j in range(i, N):
            if(adj[i][j] != ''):
                arr[i][j] = math.sqrt(math.pow(
                    (float(locations[i][0])-float(locations[j][0])), 2) +
                    math.pow((float(locations[i][1])-float(locations[j][1])), 2))

    # with open("dist.csv", "wb") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(arr)
    gen_graph(arr)
