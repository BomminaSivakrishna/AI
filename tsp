

def tsp_dfs(graph, current_node, visited, num_visited, path_length, min_path):
    if num_visited == len(graph):
        min_path[0] = min(min_path[0], path_length + graph[current_node][0])  # Return to starting node
        return
   
    visited[current_node] = True
   
    for next_node in range(len(graph)):
        if not visited[next_node]:
            tsp_dfs(graph, next_node, visited, num_visited + 1, path_length + graph[current_node][next_node], min_path)
           
    visited[current_node] = False

def tsp():
    num_cities = int(input("Enter the number of cities: "))
   
    graph = []
    print("Enter the distance matrix:")
    for _ in range(num_cities):
        row = list(map(int, input().split()))
        graph.append(row)
   
    visited = [False] * num_cities
    min_path = [float('inf')]
   
    tsp_dfs(graph, 0, visited, 1, 0, min_path)  # Start from node 0
   
    return min_path[0]

min_distance = tsp()
print("Minimum distance:", min_distance)