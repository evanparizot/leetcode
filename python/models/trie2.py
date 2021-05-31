!#/usr/bin/python3
class Trie():

    def __init__(self):
        self.trie = {}

    def insert(self, word:str):
        # Copy trie
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['-'] = True

    def search(self, word:str):
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return '-' in t

    def startswith(self, prefix: str):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True