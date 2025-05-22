class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # кількість слів, які проходять через вузол
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
            node.count += 1
        node.is_end_of_word = True


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(word, str) for word in strings):
            return ""

        # Вставляємо всі слова в префіксне дерево (Trie)
        for word in strings:
            self.insert(word)

        # Проходимо префіксне дерево, поки всі слова мають однаковий префікс
        prefix = ""
        node = self.root
        min_length = min(len(word) for word in strings)

        while node and len(node.children) == 1 and node.count == 0:
            # ця умова не дає пройти вглиб дерева, виправимо її нижче
            break

        while len(node.children) == 1 and len(prefix) < min_length:
            char, next_node = next(iter(node.children.items()))
            if next_node.count < len(strings):
                break
            prefix += char
            node = next_node

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["alone"]
    assert trie.find_longest_common_word(strings) == "alone"

    print("Усі тести пройдено успішно.")
