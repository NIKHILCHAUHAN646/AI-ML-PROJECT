def find_quick_sub(graph, start, goal):
    """ BFS to find the closest possible substitute """
    queue = [[start]]
    visited = [] # Using a list to keep track of where we've been

    while queue:
        path = queue.pop(0)
        item = path[-1]

        if item == goal:
            return path
        
        if item not in visited:
            for next_item in graph.get(item, []):
                new_path = list(path)
                new_path.append(next_item)
                queue.append(new_path)
            visited.append(item)
    return None

def find_all_chains(graph, current, goal, path=[]):
    """ DFS to explore deeper substitution chains """
    path = path + [current]
    
    if current == goal:
        return path
        
    for next_item in graph.get(current, []):
        if next_item not in path: 
            result = find_all_chains(graph, next_item, goal, path)
            if result:
                return result
    return None