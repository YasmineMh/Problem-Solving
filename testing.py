import collections
from typing import List

squares = collections.defaultdict(set)
# print(squares)
# print(1 // 3)
# print(4 // 3)
# print(7 // 3)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #define empty dicts of sets
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_grid = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if "." == board[r][c]:
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sub_grid[(r//3,c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_grid[(r//3,c//3)].add(board[r][c])
                
                print("******** r={} and c={}".format(r,c))
                print(rows)
                print(cols)
                print(sub_grid)

        return True

s = Solution()
sod = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
b = s.isValidSudoku(sod)
print(b)