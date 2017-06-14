

def collect_components(graph, threshold):
	components = []
	processed = set()

	def dfs(v, current_component):
		current_component.add(v)
		processed.add(v)
		neighbours = np.where(graph[v,:] >= threshold)[0]
		for w in neighbours:
			if w not in processed:
				dfs(w, current_component)

	for v in range(graph.shape[0]):
		if v not in processed:
			current_component = set()
			dfs(v, current_component)
			components.append(current_component)

	return components



if __name__ == '__main__':
	import numpy as np

	graph = np.array([
		[ 0, 12,  2,  3,  4],
		[12,  0,  9,  5,  3],
		[ 2,  9,  0, 15, 10],
		[ 3,  5, 15,  0, 10],
		[ 4,  3, 10, 10,  0],
		])

	components = collect_components(graph, threshold = 5)
	for component in components:
		print(component)
	print("-" * 50)

	components = collect_components(graph, threshold = 10)
	for component in components:
		print(component)
	print("-" * 50)

	components = collect_components(graph, threshold = 15)
	for component in components:
		print(component)
	print("-" * 50)
