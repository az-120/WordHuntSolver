class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def build_trie(word_list):
    root = TrieNode()
    for word in word_list:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root


scores = {3: 100, 4: 400, 5: 800, 6: 140, 7: 1800, 8: 2200}


matrix = []
while 1:
    string = input("Enter board (16 letters): ")
    if len(string) != 16:
        print("Invalid length. Enter again.")
    else:
        break

for i in range(4):
    row = []
    for j in range(4):
        row.append(string[i * 4 + j].lower())
    matrix.append(row)


def solution(matrix):
    score = 0
    found_words = []

    def dfs(i, j, node, word, visited):
        nonlocal score

        if (
            i not in range(len(matrix))
            or j not in range(len(matrix[0]))
            or visited[i][j]
        ):
            return

        visited[i][j] = True
        char = matrix[i][j]

        if char in node.children:
            node = node.children[char]
            word = word + char

            if node.is_end_of_word and len(word) > 2 and word not in found_words:
                if len(word) in scores.keys():
                    score += scores[len(word)]
                else:
                    score += 3000
                found_words.append(word)

            dfs(i, j - 1, node, word, visited)
            dfs(i, j + 1, node, word, visited)
            dfs(i - 1, j, node, word, visited)
            dfs(i + 1, j, node, word, visited)
            dfs(i - 1, j - 1, node, word, visited)
            dfs(i + 1, j + 1, node, word, visited)
            dfs(i - 1, j + 1, node, word, visited)
            dfs(i + 1, j - 1, node, word, visited)

        visited[i][j] = False

    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    with open("word_list.txt", "r") as file:
        word_list = [word.strip().lower() for word in file]

    trie_root = build_trie(word_list)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(i, j, trie_root, "", visited)

    found_words.sort(key=len, reverse=True)

    print(found_words)

    print("Max score:", score)


solution(matrix)
