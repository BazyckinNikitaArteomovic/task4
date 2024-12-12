class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word, max_penalties=3):
        def dfs(node, word, index, current_word, penalties):
            if penalties > max_penalties:
                return
            if index == len(word):
                if node.is_end_of_word:
                    similar_words.append((penalties, current_word))
                return
            current_char = word[index]
            if current_char in node.children:
                dfs(node.children[current_char], word, index + 1, current_word + current_char, penalties)
            for char, child_node in node.children.items():
                if char != current_char:
                    dfs(child_node, word, index + 1, current_word + char, penalties + 1)

            dfs(node, word, index + 1, current_word, penalties + 1)
            for char, child_node in node.children.items():
                dfs(child_node, word, index, current_word + char, penalties + 1)

        similar_words = []
        dfs(self.root, word, 0, "", 0)
        similar_words.sort(key=lambda x: x[0])
        return [word for _, word in similar_words]


trie = Trie()
words = ["cat", "bat", "rat", "mat", "hat", "cap", "map"]
for word in words:
    trie.insert(word)
input_word = input("Введите слово: ")
closest_words = trie.search(input_word)
if closest_words:
    print("Похожие слова:", closest_words)
else:
    print("Похожих слов не найдено.")
