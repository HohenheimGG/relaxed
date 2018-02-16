# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.

class WordSearch(object):

    class TreeNode(object):
        def __init__(self):
            next =  None * 26
            word = None

    def solution1(self, words, board):
        result = []
        root = self.buildTrie(words)
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                self.find(i, j, board, root, result)


    def buildTrie(self, words):
        root = self.TreeNode()
        for word in words:
            p = root
            for index, char in enumerate(word):
                start = ord(char) - ord('a')
                if p.next[start] == None:
                    p.next[start] = self.TreeNode()
                p = p.next[start]
            p.word = word
        return root


    def find(self, i, j, board, p, result):
        char = board[i][j]
        if char == '#':
            return

        start = ord(char) - ord("a")
        if p.next[start] == None:
            return

        p = p.next[start]
        if p.word !=  None:
            result.append(p.word)
            p.word = None
            return

        board[i][j] = '#'
        if i > 0:
            self.find(i - 1, j, board, p, result)
        if j > 0:
            self.find(i, j - 1, board, p, result)
        if i < len(board):
            self.find(i + 1, j, board, p, result)
        if j < len(board[0]):
            self.find(i, j + 1, board, p, result)
        board[i][j] = char


if __name__ == '__main__':
    pass