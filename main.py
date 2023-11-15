def remove_unnecessary_vertices(graph):
    degree_two_vertices = [v for (v, neighbors) in graph.items()
                           if len(neighbors) == 2]
    for vertex in degree_two_vertices:
        if vertex in graph:
            neighbors = graph[vertex]
            graph.pop(vertex)
            if neighbors[0] != neighbors[1]:
                graph[neighbors[0]].remove(vertex)
                graph[neighbors[1]].remove(vertex)
                graph[neighbors[0]].append(neighbors[1])
                graph[neighbors[1]].append(neighbors[0])

    return graph


graph = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5, 6],
    5: [4],
    6: [4, 7, 8],
    7: [6],
    8: [6, 9],
    9: [8, 10, 11],
    10: [9],
    11: [9, 12, 13],
    12: [11],
    13: [11, 14, 15],
    14: [13],
    15: [13, 16],
    16: [15, 17],
    17: [16, 18],
    18: [17, 19, 20, 27],
    19: [18],
    20: [18, 21, 22],
    21: [20],
    22: [20, 23, 24],
    23: [22],
    24: [22, 25, 26],
    25: [24],
    26: [24],
    27: [18, 28, 32],
    28: [27, 29, 30, 31],
    29: [28],
    30: [28],
    31: [28],
    32: [27, 33],
    33: [32, 34],
    34: [33, 35],
    35: [34, 36],
    36: [35, 37],
    37: [36, 38, 47, 60],
    38: [39, 44, 45],
    39: [38, 40],
    40: [39, 41, 42, 43],
    41: [40],
    42: [40],
    43: [40],
    44: [38],
    45: [38, 46],
    46: [45],
    47: [37, 48, 49, 53],
    48: [47],
    49: [47, 50],
    50: [49, 51, 52],
    51: [50],
    52: [50],
    53: [47, 54],
    54: [53, 55, 56],
    55: [54],
    56: [54, 57, 58, 59],
    57: [56],
    58: [56],
    59: [56],
    60: [37, 61],
    61: [60, 62],
    62: [61, 63],
    63: [62, 64],
    64: [63, 65],
    65: [64, 66, 74],
    66: [65, 67, 68, 69],
    67: [66],
    68: [66],
    69: [66, 70, 71],
    70: [69],
    71: [69, 72, 73],
    72: [71],
    73: [71],
    74: [65, 75, 76, 82],
    75: [74],
    76: [74, 77, 78, 79],
    77: [76],
    78: [76],
    79: [76, 80, 81],
    80: [79],
    81: [79],
    82: [74, 83, 84],
    83: [82],
    84: [82, 85, 86],
    85: [84],
    86: [84, 87, 90],
    87: [86, 88, 89],
    88: [87],
    89: [87],
    90: [86, 91, 92],
    91: [90],
    92: [90, 93, 95],
    93: [92, 94],
    94: [93],
    95: [92],
    }

result = remove_unnecessary_vertices(graph)
print(result)