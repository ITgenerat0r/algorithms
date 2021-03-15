from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "michael"]
graph["alice"] = ["meggi"]
graph["michael"] = ["thom", "jonny"]
graph["bob"] = []
graph["meggi"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
	if person[0] == "m":
		return True
	return False

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person_is_seller(person):
				print(person + " is a mango seller!")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

search("you")