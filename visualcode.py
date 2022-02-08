import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
def visualize (filePath):
    G = nx.DiGraph()
    tree = ET.parse(filePath)
    root = tree.getroot()
    for user in root:
        id = user[0].text
        print("id :", id)
        G.add_node(id, name = user[1].text)
        for follower in user[3]:
            fid = follower[0].text
            print(fid)
            G.add_edge(fid, id)

    nx.draw(G, with_labels = True)
    plt.show()

# visualize("D:/David/Data Structures and Algorithms/project/sample.xml")