from Q2 import ShortestPath
import unittest


class TestShortestPath(unittest.TestCase):

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
    def test_dijkstra(self):
        print("send the array and node number 0 and get all his path")
        self.assertEqual(self.sp.find_shortest_path(0), [0, 7, 5, 10])

    def test_fw(self):
        print("send the array and get the path matrix of all the nodes")
        self.assertEqual(self.sp.find_shortest_path(), [[0, 7, 5, 10],
                                                        [7, 0, 2, 3],
                                                        [5, 2, 0, 5],
                                                        [10, 3, 5, 0]])
