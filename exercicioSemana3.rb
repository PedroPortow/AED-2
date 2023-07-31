class Graph
  def initialize
    @graph = {}
  end

  def add_node(node)
    @graph[node] = []
  end

  def add_path(source, destination, weight = 0, directed = true)
    @graph[source] << { node: destination, weight: weight }

    if not directed
      @graph[destination] << { node: source, weight: weight }
    end
  end


  def remove_node(node)
    @graph.delete(node)
    @graph.each do |_, adjacentNodes|
      adjacentNodes.reject! { |hash| hash[:node] == "#{node}" }
    end

  end

  def remove_path(source, destination, directed = true)
    @graph[source].reject!{ |hash| hash[:node] == "#{destination}" }

    if not directed
      @graph[destination].reject!{ |hash| hash[:node] == "#{source}" }
    end
  end

  def adjacent_nodes(node)
    @graph[node]
  end

  def has_node(node)
    @graph.key?(node)
  end

  # def dijkstra(source, dest)
  #   distances = {}     # dist min nós ao nó de origem
  #   previous_nodes = {}  # predecessores que foram o caminho minimo

  #   # Inicialização das distâncias para todos os nós (exceto o nó de origem) como infinito
  #   @graph.keys.each do |node|
  #     distances[node] = 999999
  #   end

  #   distances[source] = 0

  #   unvisited_nodes = @graph.keys
  #   puts distances
  # end

  # def kruskal
  #   mst = []
  #   visited = []
  #   sorted_paths = []

  #   @graph.each do |node_key, adjacent_nodes|
  #     adjacent_nodes.each do |path|
  #       sorted_paths << {source: node_key, dest: path[:node], weight: path[:weight]}
  #     end
  #   end

  #   sorted_paths.sort_by! { |path| path[:weight] }

  #   sorted_paths.each do |path|
  #     next if visited.include? (path[:source])

  #     mst.each do |mst_path|
  #       mst << path unless mst_path[:source] == path[:source]
  #     end

  #     visited.push(path[:source])
  #   end

  #   puts mst
  # end

  def prim(start = "A")
    mst = []  # array com os nós mst
    visited = []   # nós já visitados
    queue = []      # fila

    queue.push({ node: start, weight: 0 })  # nó de partida

    while !queue.empty?
      queue.sort_by! { |path| path[:weight] }  # ordena pelo peso, aqui sempre vai pegar a aresta de menor peso

      min_path = queue.shift                   # pegando a aresta de menor peso
      current_node_key = min_path[:node]
      current_node_weight = min_path[:weight]

      next if visited.include?(current_node_key)  # nó já foi visitado? vai embora
      visited.push(current_node_key)

      mst.push(current_node_key)          # já pode dar o push pro mst, pq se chegou nesse nó ele já faz parte

      @graph[current_node_key].each do |path|               # pegando as menores arestas
        queue.push(path) unless visited.include?(path[:node])
      end
    end

    mst
  end


  def print_graph
    @graph.each do |node, adjacent_nodes|
      puts "#{node} -> #{adjacent_nodes.map { |adjacent| "#{adjacent[:node]} (#{adjacent[:weight]})" }.join(', ')}"
    end
  end
end

graph = Graph.new

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("F")
graph.add_node("E")
graph.add_node("G")

# graph.add_path("A", "B", 2, false)
# graph.add_path("A", "D", 3, false)
# graph.add_path("A", "C", 3, false)
# graph.add_path("B", "C", 4, false)
# graph.add_path("B", "E", 3, false)
# graph.add_path("C", "D", 5, false)
# graph.add_path("C", "E", 1, false)
# graph.add_path("C", "F", 6, false)
# graph.add_path("D", "F", 7, false)
# graph.add_path("E", "F", 8, false)
# graph.add_path("F", "G", 9, false)


mst = graph.prim("A")
# mst = graph.kruskal

