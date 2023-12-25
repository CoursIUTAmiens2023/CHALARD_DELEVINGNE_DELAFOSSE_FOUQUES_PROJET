from collections import deque
from collections import namedtuple

Direction = namedtuple("Direction", ["dx", "dy", "name"])

class ShortestPathFinder:
    DIRECTIONS = [Direction(0, -1, "Gauche"), Direction(0, 1, "Droite"), Direction(-1, 0, "Haut"), Direction(1, 0, "Bas")]

    def find_shortest_path(self, matrix, start_x, start_y, flag_x, flag_y):
        rows, cols = len(matrix), len(matrix[0])

        queue = deque()
        visited = [[False] * cols for _ in range(rows)]

        queue.append(Node(start_x, start_y, None))
        visited[start_x][start_y] = True

        while queue:
            current = queue.popleft()

            if current.x == flag_x and current.y == flag_y:
                return self.construct_path(current)

            for direction in self.DIRECTIONS:
                new_x, new_y = current.x + direction.dx, current.y + direction.dy

                if self.is_valid_move(new_x, new_y, rows, cols) and matrix[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    queue.append(Node(new_x, new_y, current))
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
        for direction in self.DIRECTIONS:
            if from_node.x + direction.dx == to_node.x and from_node.y + direction.dy == to_node.y:
                return direction.name

        return ""

    def is_valid_move(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

Node = namedtuple("Node", ["x", "y", "parent"])
