'''

'''

def dfs(nodes:list,graph,currentNode):
    if currentNode not in nodes:
        print(currentNode,end=', ')
        nodes.append(currentNode)
        for n in graph[currentNode]:
            dfs(nodes,graph,n)

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

dfs([],graph,'A')