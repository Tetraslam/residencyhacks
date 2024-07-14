import igraph as ig
import matplotlib.pyplot as plt

def shortest_path(graph, start, end):
    """
    Find the shortest path in the graph from the start vertex to the end vertex.
    
    Args:
        graph (igraph.Graph): The graph object.
        start (int): The starting vertex index.
        end (int): The ending vertex index.
    
    Returns:
        list: The list of vertex indices representing the shortest path.
    """
    return graph.get_shortest_paths(start, to=end, output="vpath")[0]

def construct_graph(prompt, num_of_vertices, policy_names, policy_descriptions, edges, city_name):
    """
    Construct a graph based on the given parameters, find the shortest path, and visualize it.
    
    Args:
        prompt (str): The title of the graph.
        num_of_vertices (int): The number of vertices in the graph.
        policy_names (list[str]): The list of names for each vertex.
        policy_descriptions (list[str]): The list of descriptions for each policy (not used in visualization).
        edges (list[list[int]]): The list of edges connecting the vertices.
        city_name (str): The name of the city (used for saving the graph image).
    
    Returns:
        None
    """
    # Create the graph with the specified number of vertices and edges
    graph = ig.Graph(num_of_vertices, edges)
    graph['title'] = prompt
    graph.vs['name'] = policy_names
    
    # Initialize a figure for plotting
    fig, ax = plt.subplots(figsize=(5, 5))
    
    # Find the shortest path from the first to the last vertex
    optimal_path = shortest_path(graph, 0, num_of_vertices - 1)
    print(optimal_path)
    
    # Identify the edges that are part of the shortest path
    optimal_edges = []
    for i in range(len(optimal_path) - 1):
        if [optimal_path[i], optimal_path[i + 1]] in edges:
            optimal_edges.append(edges.index([optimal_path[i], optimal_path[i + 1]]))
    print(optimal_edges)
    
    # Highlight the edges in the shortest path
    graph.es[optimal_edges]['color'] = "salmon"
    
    # Plot the graph
    ig.plot(
        graph,
        target=ax,
        layout="circle",
        vertex_size=50,
        vertex_color="salmon",
        vertex_frame_width=1.0,
        vertex_frame_color="black",
        vertex_label=graph.vs["name"],
        vertex_label_size=7.0,
        edge_width=2
    )
    
    # Save the figure as a PNG file
    fig.savefig(f'{city_name}.png')

# Example usage:
# policy_names = ["bicycle lanes", "car-free boulevards", "driverless cars", "$1000/month SUV tax", "electric buses", "vertical farms"]
# edges = [[0, 1], [1, 2], [0, 3], [2, 4], [3, 5], [1, 3]]
# construct_graph("sf reimagined", 5, policy_names, ["", "", "", "", "", ""], edges, "sf_reimagined")
