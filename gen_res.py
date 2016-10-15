import xml.etree.ElementTree
import pandas as pd
import csv
import math


def gen_shortest():
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

    with open("dist.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(arr)

gen_shortest()
