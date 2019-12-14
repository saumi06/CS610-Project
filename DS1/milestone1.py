import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist('soc-sign-bitcoinalpha.csv', delimiter=',', create_using=nx.DiGraph(),data=[('rating',int),('att1',int)])
print (nx.info(G))