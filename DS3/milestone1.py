import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist('musae_facebook_edges.csv', delimiter=',', create_using=nx.Graph())
print (nx.info(G))

