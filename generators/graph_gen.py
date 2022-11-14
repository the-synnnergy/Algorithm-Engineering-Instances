import networkx as nx
from random import random,randrange



def networkx_graph_to_ae_format(graph : nx.Graph,instance_id,top_nodes):
    lines = []
    number_nodes = graph.number_of_nodes()
    number_edges = graph.number_of_edges()
    terminalString = ""
    sorted_list = sorted(graph.degree(), key= lambda x : x[1])
    set_terminals = set()
    max_nodes = int(top_nodes *number_nodes) + 2
    for index,obj in enumerate(reversed(sorted_list)):
        if index > max_nodes:
            break
        set_terminals.add(obj[0])
    print(max_nodes)
    print(sorted_list)
    print(set_terminals)
    for i in range(number_nodes):
        if i in set_terminals:
            terminalString = terminalString + "1"
            continue
        terminalString = terminalString + "0"
    lines.append(str(instance_id))
    lines.append(str(number_nodes))
    lines.append(terminalString)
    lines.append(str(number_edges))
    for line in nx.generate_edgelist(graph,data=False):
        lines.append(line + " 1")
    file = open("./"+str(instance_id),"x")
    lines = "\n".join(lines)
    file.writelines(lines)
    file.close()
for i in range(20):
    instance_id = "Instanz_" + str(i)
    prob = random()/10.0
    instance_id = instance_id +"_prob_" +str(prob)
    nodes = randrange(100,100000,1)
    instance_id = instance_id +"_nodes_" +str(nodes)
    graph = nx.scale_free_graph(nodes)
    networkx_graph_to_ae_format(graph,instance_id,prob)
