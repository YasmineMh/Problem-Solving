class Solution:
    
    #Runtime: 158 ms, faster than 45.57% of Python3 online submissions for Valid Sudoku.
    #Memory Usage: 13.9 MB, less than 35.29% of Python3 online submissions for Valid Sudoku.
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
                
        return True