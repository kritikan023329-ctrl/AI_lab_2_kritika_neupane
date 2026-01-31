import heapq

# Graph representation (City Map)
graph = {
    'Kathmandu': [('nepalgunj', 140), ('Butwal', 260)],
    'nepalgunj': [('Kathmandu', 140), ('Pokhara', 120)],
    'Butwal': [('Kathmandu', 260), ('Pokhara', 50)],
    'Pokhara': []
}

# Heuristic values (straight-line distance estimate to Pokhara)
heuristic = {
    'Kathmandu': 200,
    'nepalgunj': 100,
    'Butwal': 60,
    'Pokhara': 0
}

def a_star_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while priority_queue:
        current_cost, current_city = heapq.heappop(priority_queue)

        if current_city == goal:
            break

        for neighbor, road_cost in graph[current_city]:
            new_cost = cost_so_far[current_city] + road_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current_city

    # Reconstruct path
    path = []
    city = goal
    while city:
        path.append(city)
        city = came_from[city]

    path.reverse()
    return path, cost_so_far[goal]

# Run the algorithm
path, cost = a_star_search('Kathmandu', 'Pokhara')

print("Shortest Path:", path)
print("Total Cost:", cost)
