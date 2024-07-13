import igraph as ig
import matplotlib.pyplot as plt

def shortest_path(graph, start, end):
  return graph.get_shortest_paths(start, to=end, output = "vpath")[0]

def construct_graph(prompt, num_of_vertices: int, policy_names: list[str], policy_descriptions: list[str], edges: list[list[int]]):
  graph = ig.Graph(num_of_vertices, edges)
  graph['title'] = prompt
  graph.vs['name'] = [i for i in policy_names]
  fig, ax = plt.subplots(figsize = (5, 5))
  optimal_path = shortest_path(graph, 0, num_of_vertices-1)
  print(optimal_path)
  optimal_edges = []
  for i in range(len(optimal_path)-1):
    if [optimal_path[i], optimal_path[i+1]] in edges:
      optimal_edges.append(edges.index([optimal_path[i], optimal_path[i+1]]))
  print(optimal_edges)
  graph.es[optimal_edges]['color'] = "salmon"
  ig.plot(
    graph,
    target = ax,
    layout = "circle",
    vertex_size = 50,
    vertex_color = "salmon",
    vertex_frame_width = 1.0,
    vertex_frame_color = "black",
    vertex_label = graph.vs["name"],
    vertex_label_size = 7.0,
    edge_width = 2
  )
  fig.savefig('plan.png')


#policynames = ["bicycle lanes", "car-free boulevards", "driverless cars", "$1000/month SUV tax", "electric buses", "vertical farms"]
#edges = [[0, 1], [1, 2], [0, 3], [2, 4], [3, 5], [1, 3]]
#construct_graph("sf reimagined", 5, policynames, ["", "", "", "", "", "", "", ""], edges)