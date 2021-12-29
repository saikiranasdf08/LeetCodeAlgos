'''

'''

def bfs(nodes:list,graph,currentNode):
    queue=[]
    nodes.append(currentNode)
    queue.append(currentNode)
    while queue:
        x= queue.pop(0)
        print(x,end=', ')
        for n in graph[x]:
            if n not in nodes:
                queue.append(n)
                nodes.append(n)


graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I":[]
}

bfs([],graph,'A')