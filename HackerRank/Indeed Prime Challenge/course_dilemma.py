import Queue
import sys

num_testcases = int(input())
class Vertex:
	marked = False

	def __init__(self, course_number, children=[]):
		self.course_number = course_number
		self.children = children
		self.has_parent = False
		self.height = sys.maxint

	def add_edge(self, child):
		self.children = self.children + [child]
		child.has_parent = True

def determine_semesters(v, height, max_height):
	v.height = min(v.height, height)
	max_height[0] = max(v.height, max_height[0])
	for child in v.children:
		determine_semesters(child, height + 1, max_height)
	return max_height[0]

def has_cycle(v, visited):
	if v in visited:
		return True
	visited.append(v)
	for child in v.children:
		if has_cycle(child, visited):
			return True
	return False

for i in range(1, num_testcases + 1):
	N, R = [int(x) for x in raw_input().split()]
	ends = True

	vertices = []
	for course_number in range(N):
		vertices.append(Vertex(course_number))

	for _ in range(R):
		i, j = [int(x) for x in raw_input().split()]
		vertices[j].add_edge(vertices[i])

	top_vertex = Vertex(-1)
	for v in vertices:
		if has_cycle(v,[]):
			ends = False
			break
		if not v.has_parent:
			top_vertex.add_edge(v)
				
	if ends:
		print("Case " + str(i) + ": " + str(determine_semesters(top_vertex, 0, [0])) + " semester(s)")
	else:
		print("Case " + str(i) + ": Never Ends")		

