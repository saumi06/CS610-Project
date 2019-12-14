import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist('Wiki.csv', delimiter=',', create_using=nx.Graph())
print (nx.info(G))