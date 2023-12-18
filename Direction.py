from queue import Queue

class ShortestPathFinder:
    def find_shortest_path(self, matrix, start_x, start_y, flag_x, flag_y):
        rows, cols = len(matrix), len(matrix[0])

        queue = Queue()
        visited = [[False] * cols for _ in range(rows)]

        queue.put(Node(start_x, start_y, None))
        visited[start_x][start_y] = True

        while not queue.empty():
            current = queue.get()

            if current.x == flag_x and current.y == flag_y:
                return self.construct_path(current)

            directions = [(0, -1, "Gauche"), (0, 1, "Droite"), (-1, 0, "Haut"), (1, 0, "Bas")]

            for dx, dy, direction in directions:
                new_x, new_y = current.x + dx, current.y + dy

                if self.is_valid_move(new_x, new_y, rows, cols) and matrix[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    queue.put(Node(new_x, new_y, current))
                    visited[new_x][new_y] = True

        return []

    def construct_path(self, destination):
        path = []

        while destination.parent is not None:
            path.append(self.get_direction(destination.parent, destination))
            destination = destination.parent

        path.reverse()
        return path

    def get_direction(self, from_node, to_node):
        if from_node.x < to_node.x:
            return "Bas"
        elif from_node.x > to_node.x:
            return "Haut"
        elif from_node.y < to_node.y:
            return "Droite"
        elif from_node.y > to_node.y:
            return "Gauche"
        else:
            return ""

    def is_valid_move(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols   
        
class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent