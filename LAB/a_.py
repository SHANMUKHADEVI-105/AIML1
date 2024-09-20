# -*- coding: utf-8 -*-
"""A*.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SZ67IOrp0e0Aq3TwDCF_jM8-4Jzo48aa
"""

import heapq

def a_star(maze, start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_scores = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == end:
            path = []
            while current:
                path.append(current)
                current = g_scores.get(current, None)
            return path[::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_scores[current] + 1
                if tentative_g < g_scores.get(neighbor, float('inf')):
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                    heapq.heappush(open_list, (f_score, neighbor))
    return None

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start, end = (0, 0), (4, 4)
path = a_star(maze, start, end)
print("Path found:", path)