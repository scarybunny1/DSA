class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        
        for rowNo in range(9):
            for colNo in range(9):
                element = board[rowNo][colNo]
                
                if element.isdigit():
                
                    if element in rows[rowNo]:
                        return False
                    rows[rowNo].add(element)
                    
                    if element in cols[colNo]:
                        return False
                    cols[colNo].add(element)
                    
                    boxNo = ((rowNo // 3) * 3) + (colNo // 3)
                    if element in boxes[boxNo]:
                        return False
                    boxes[boxNo].add(element)
        return True