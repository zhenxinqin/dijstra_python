infinity = float ('inf')

graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] =5

graph['fin'] = {}

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []



def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node  = None 
	for node in costs:
		#print node 
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
			#print lowest_cost_node
	return lowest_cost_node

# i = 1	
# while i:
# 	find_lowest_cost_node(costs)
# 	i = i - 1

node = find_lowest_cost_node(costs)
while node is not None:
	#print node 
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
			#print 'new_parent:',node 
	processed.append(node)
	#print 'processed:',processed[-1]
	node = find_lowest_cost_node(costs)

print 'shortest:'
for node in costs:
	print str(node) +':'+ str(costs[node])
for n in parents:
	print n +'	'+ parents[n]
