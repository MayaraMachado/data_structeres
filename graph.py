class Graph:

  def __init__(self, nodes, edges):
      self.grafo = {}
      for node in nodes:
          self.grafo[node] = []
      for edge in edges:
          self.grafo[edge[0]].append(edge[1])
  

  def dfs_caminhos(self, inicio, fim):
      pilha = [(inicio, [inicio])]
      while pilha:
          vertice, caminho = pilha.pop()
          for proximo in set(self.grafo[vertice]) - set(caminho):
              if proximo == fim:
                  yield caminho + [proximo]
              else:
                  pilha.append((proximo, caminho + [proximo]))



if __name__ == '__main__':
  nodes = ['GRU', 'BRC', 'SCL', 'ORL', 'CDG']
  edges = [('GRU', 'CDG', 75), ('GRU', 'BRC', 10),('GRU', 'SCL', 20), ('GRU', 'ORL', 56), ('BRC', 'SCL', 5), ('SCL', 'ORL', 20), ('ORL', 'CDG', 5)]  
  grafo = Graph(nodes, edges)

  caminhos = list(grafo.dfs_caminhos('GRU', 'CDG'))
  print(caminhos)
