# I got help from my fried Liad Nagi
# The main idea is to use the strategy design pattern to decide which algorithm our program
# should use. I used Dijkstra and Floyd Warshall algorithms to solve the min distance problem in a graph.
import queue

class ShortestPath:

    def __init__(self, adj_mat: list):
        self.adj_mat = adj_mat

    @staticmethod
    def __min_distance(dist, queue):
        """min distance for dijkstra"""
        minimum = float('inf')
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    # dijkstra algo
    def __dijkstra(self, src):
        row = len(self.adj_mat)
        col = len(self.adj_mat[0])
        dist = [float('inf')] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)

        # Find shortest path from src to all
        while queue:
            u = self.__min_distance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if self.adj_mat[u][i] and i in queue:
                    if dist[u] + self.adj_mat[u][i] < dist[i]:
                        dist[i] = dist[u] + self.adj_mat[u][i]
        return dist


    def __floyd_warshall(self):
        n = len(self.adj_mat)
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.adj_mat))

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if(dist[i][j] > dist[k][j]+dist[i][k]):
                        dist[i][j] = dist[k][j]+dist[i][k]

        return dist

    def find_shortest_path(self, start: int = float('inf')):
        if start == float('inf'):
            return self.__floyd_warshall()
        return self.__dijkstra(start)


if __name__ == "__main__":

    arr = [[0, 18, 5, float('inf')],
           [18, 0, 2, 3],
           [5, 2, 0, float('inf')],
           [float('inf'), 3, float('inf'), 0]]
    
    print("  Our Graph Is: ")
    print("       18               ")
    print("   [0]----[1]                ")
    print("   |   /   \ 3                ")
    print("  5|  /2    \             ")
    print("   | /      [3]           ")
    print("   [2]                   ")
    
    sp = ShortestPath(arr)
    print("send the array and node number 0 and get all his path")
    print(sp.find_shortest_path(0))
    print()

    print("send the array and get the path matrix of all the nodes")
    a = sp.find_shortest_path()
    for i in a:
        print(i)
