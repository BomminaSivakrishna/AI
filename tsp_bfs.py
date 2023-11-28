import itertools

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def total_distance(path, cities):
    distance = 0
    for i in range(len(path) - 1):
        distance += euclidean_distance(cities[path[i]], cities[path[i+1]])
    distance += euclidean_distance(cities[path[-1]], cities[path[0]])  # Return to the starting city
    return distance

def tsp_bfs(cities):
    num_cities = len(cities)
    starting_city = 0
    all_cities = set(range(num_cities))
    shortest_path = None
    min_distance = float('inf')

    queue = [(starting_city, [starting_city])]

    while queue:
        current_city, path = queue.pop(0)
        unvisited_cities = all_cities - set(path)

        if not unvisited_cities:
            path_distance = total_distance(path, cities)
            if path_distance < min_distance:
                min_distance = path_distance
                shortest_path = path
        else:
            for next_city in unvisited_cities:
                new_path = path + [next_city]
                queue.append((next_city, new_path))

    return shortest_path, min_distance

if __name__ == "__main__":
    # User input for cities and coordinates
    cities = []
    num_cities = int(input("Enter the number of cities: "))
   
    for i in range(num_cities):
        x, y = map(int, input(f"Enter coordinates for City {i+1} (x y): ").split())
        cities.append((x, y))

    shortest_path, min_distance = tsp_bfs(cities)
    print("Shortest Path:", shortest_path)
    print("Minimum Distance:", min_distance)

