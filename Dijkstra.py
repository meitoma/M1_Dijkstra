import heapq

def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    mins = {start: 0}
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return cost, path

            for next_node, next_cost in graph[node].items():
                prev_cost = mins.get(next_node, None)
                next_cost += cost
                if prev_cost is None or next_cost < prev_cost:
                    heapq.heappush(queue, (next_cost, next_node, path))
                    mins[next_node] = next_cost

    return float("inf"), []
