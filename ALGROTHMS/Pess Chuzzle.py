from typing import List, Tuple

class RookMover:
    def __init__(self, n: int, perm: List[int]):
        self.n = n
        self.target = [p-1 for p in perm]  # Convert to 0-based indexing
        self.moves = []
        self.board = [[False] * 8 for _ in range(n)]
        # Place initial rooks on bottom row
        for i in range(n):
            self.board[i][0] = True
            
    def is_path_clear(self, start_col: int, start_row: int, end_col: int, end_row: int) -> bool:
        """Check if path is clear for horizontal then vertical movement"""
        # Check horizontal path
        if start_row == end_row:
            min_col = min(start_col, end_col)
            max_col = max(start_col, end_col)
            return not any(self.board[col][start_row] for col in range(min_col+1, max_col))
            
        # Check vertical path
        min_row = min(start_row, end_row)
        max_row = max(start_row, end_row)
        return not any(self.board[start_col][row] for row in range(min_row+1, max_row))
        
    def move_rook(self, start_col: int, start_row: int, end_col: int, end_row: int):
        """Move rook and record the move"""
        # Update board
        self.board[start_col][start_row] = False
        self.board[end_col][end_row] = True
        # Record move (convert to 1-based indexing for output)
        self.moves.append((start_col+1, start_row+1, end_col+1, end_row+1))
        
    def solve(self) -> List[Tuple[int, int, int, int]]:
        """Find optimal sequence of moves to arrange rooks according to permutation"""
        rook_positions = list(range(self.n))  # Current column positions of rooks
        
        def move_to_target(rook_idx: int, intermediate_row: int = 7):
            """Move rook to its target position using an intermediate row if needed"""
            curr_col = rook_positions[rook_idx]
            target_col = self.target[rook_idx]
            
            if curr_col == target_col:
                return
                
            # If direct path is clear, move directly
            if self.is_path_clear(curr_col, 0, target_col, 0):
                self.move_rook(curr_col, 0, target_col, 0)
                rook_positions[rook_idx] = target_col
                return
                
            # Move up to intermediate row if path is clear
            if self.is_path_clear(curr_col, 0, curr_col, intermediate_row):
                self.move_rook(curr_col, 0, curr_col, intermediate_row)
                # Move horizontally
                self.move_rook(curr_col, intermediate_row, target_col, intermediate_row)
                # Move down
                self.move_rook(target_col, intermediate_row, target_col, 0)
                rook_positions[rook_idx] = target_col
                return
                
            # Try different intermediate rows if needed
            for row in range(6, 0, -1):
                if (self.is_path_clear(curr_col, 0, curr_col, row) and 
                    self.is_path_clear(curr_col, row, target_col, row) and 
                    self.is_path_clear(target_col, row, target_col, 0)):
                    self.move_rook(curr_col, 0, curr_col, row)
                    self.move_rook(curr_col, row, target_col, row)
                    self.move_rook(target_col, row, target_col, 0)
                    rook_positions[rook_idx] = target_col
                    return
        
        # Try to move each rook to its target position
        for i in range(self.n):
            move_to_target(i)
            
        return self.moves

def solve_test_case():
    n = int(input())
    perm = list(map(int, input().split()))
    
    solver = RookMover(n, perm)
    moves = solver.solve()
    
    print(len(moves))
    for move in moves:
        print(*move)

def main():
    T = int(input())
    for _ in range(T):
        solve_test_case()

if __name__ == "__main__":
    main()