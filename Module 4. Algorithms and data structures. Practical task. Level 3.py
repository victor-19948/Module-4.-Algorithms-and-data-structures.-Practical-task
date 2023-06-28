# Написать функцию, реализующую поиск в ширину на графе

graph = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}

graph2 = {'1': {'2', '7', '8'},
          '2': {'1', '3', '6'},
          '3': {'2', '4', '5'},
          '4': {'3'},
          '5': {'3'},
          '6': {'2'},
          '7': {'1'},
          '8': {'1', '9', '12'},
          '9': {'8', '10', '11'},
          '10': {'9', '11'},
          '11': {'9'},
          '12': {'8'}}


# поиск в ширину
def dfs4(graph, start, visited, res):
    if res == []:
        visited.append(start)
        for v in graph[start]:
            if v not in visited:
                visited.append(v)
                res.append(v)
        dfs4(graph, start, visited, res)
    else:
        for j in res:
            for v in graph[j]:
                if v not in visited:
                    visited.append(v)
                    res.append(v)
    return visited


print(dfs4(graph2, '2', [], []))
print()
print(dfs4(graph, '2', [], []))
