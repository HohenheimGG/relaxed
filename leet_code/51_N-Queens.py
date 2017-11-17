# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class N_Queue(object):
    def solution1(self, n):
        board = []
        # 初始化
        for i in range(0, n):
            for j in range(0, n):
                if not board[i]:
                    board.append([])
                board[i].append('.')
        result = []
        self.dfs(board, 0, result)
        return result

    def dfs(self, board, colIndex, res):
        if colIndex == len(board):
            res.append(board)
            return

        for x in range(0, len(board)):
            if(self.validate(board, x, colIndex)):
                board[x][colIndex] = 'Q'
                self.dfs(board, colIndex + 1, res)
                board[x][colIndex] = '.'

            pass

    def validate(self, board, x, y):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'Q' or x + j == i + y or x + y == i + j or x == i:
                    return False
        return True


if __name__ == '__main__':
    pass