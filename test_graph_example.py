from implementations import Graph
graph = Graph()


def check_word(source, target):
    counter, i = 0, 0
    while i < len(source) and i < len(target):
        if source[i] is not target[i]:
            counter += 1
        i += 1
    return counter


def build_vertice_in_graph(source, words):
    arr = []
    for word in words:
        diff = check_word(source, word)
        if diff is 1:
            arr.append(word)

    graph.add_vertice(source, arr)


words = ["bit", "but", "put", "big", "pot", "pog", "dog", "lot"]

if __name__ == "__main__":
    for word in words:
        build_vertice_in_graph(word, words)

    print(graph.linkedListDict)
