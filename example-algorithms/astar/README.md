# A* Search Algorithm

A* search algorithm is an algorithm used to find the shortest path between a starting point and a destination point on a graph or a map. It uses a heuristic function to find the solution (destination) and avoids exploring unnecessary paths, and has properties of optimality and completeness, which means it’s guaranteed to find the best possible solution and, if a solution exists, it is guaranteed to find it.

## Step-by-Step Process:

1. **Initialize the start node** (node from which the algorithm will start searching) and **goal node**.
2. Create an **open set** (set of nodes that have been discovered but not yet evaluated) and a **closed set** (set of nodes that have already been evaluated).
3. Add the start node to the open set.
4. While the open set is not empty (i.e., stop criteria is not met), do the following:
    1. Find the node in the open set (“yet to visit” set) with the lowest f-cost.
        - The equation for the f-cost is f(n) = g(n) + h(n), where g(n) is the cost of getting from the start node to node n, and h(n) is the estimated cost of getting from node n to the goal.
    2. Return the path if the current node is the goal node (the path has been found).
    3. Remove the current node from the open set and add it to the closed set.
    4. For each neighbor of the current node, do the following:
        1. If the neighbor is in the closed set, skip to the next neighbor.
        2. If the neighbor is not in the open set, add it to the open set.
        3. Calculate the tentative g-cost (cost of getting from the start node to the current node plus the cost of getting from the current node to the neighbor) of the neighbor.
        4. If the tentative g-cost is greater than or equal to the neighbor's current g-cost, skip to the next neighbor.
        5. Otherwise, update the neighbor's g-cost to the tentative g-cost and calculate its f-cost.
        6. Set the neighbor's parent node to the current node.
5. If the goal node is not found, then no path exists between the start and goal nodes.
6. Return the path by following the parent pointers from the goal node to the start node.
