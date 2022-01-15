"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List


class Solution:
    # time: o(9x9)
    # Space: o(9x9x3)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            My first dumb solution:
                - I make 3 passes, and on each one I use a hashmap
                  to keep track of the numbers I have already visited

                - The first pass checks each line if it is valid
                - The second pass checks each column if it is valid
                - The third pass checks each sub box of (3x3) if it is valid

                - The time complexity of this is o(9x9x3x3)
                - Space complexity though is o(9)

            Code
            ~~~~~~~~~~
                # First pass
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                for line in board:
                    visited = set()
                    for char in line:
                        if char not in visited:
                            if char != ".":
                                visited.add(char)
                        else:
                            return False

                # Second pass
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                columns = len(board[0])
                for column in range(columns):
                    visited = set()
                    for line in board:
                        char = line[column]
                        if char not in visited:
                            if char != ".":
                                visited.add(char)
                        else:
                            return False

                # Third pass
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                indices_x = [(0, 2), (3, 5), (6, 8)]
                indices_y = [(0, 2), (3, 5), (6, 8)]
                for x in indices_x:
                    for y in indices_y:
                        visited = set()
                        for i in range(x[0], x[1]+1):
                            for j in range(y[0], y[1]+1):
                                char = board[j][i]
                                if char not in visited:
                                    if char != ".":
                                        visited.add(char)
                                else:
                                    return False

                return True

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        After making one little observation, I have noticed I could hugely improve this
        and make it converge in one pass over the board.

        The idea is to use one single hashmap, in which we store tuples,
        those tuples contains each number we visit and its position:

        for each number, we store 3 tuples in the hashmap:
            - (line_position, number)
            - (number, column_position)
            - (line_position / 3, column_position / 3, number)

        - the first tuple stores the number and its position alongside the lines,
        - the second stores the number alongside the columns (we flip the ordering to avoid 
        duplicates between lines and columns)
        - the third one stores the number and the coordinates of the sub-box.

        as soon as we find a tuple that already exists on the hashmap we return False
        otherwise the board is valid.

        Time: o(9x9)
        Space: o(9x9x3)

        """
        visited = set()
        for i in range(0, 9):
            for j in range(0, 9):
                current = board[i][j]

                if current != ".":
                    if (i, current) in visited or (current, j) in visited or (i // 3, j // 3, current) in visited:
                        return False

                    visited.add((i, current))
                    visited.add((current, j))
                    visited.add((i // 3, j // 3, current))

        return True


s = Solution()
test1 = s.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])

test2 = s.isValidSudoku([
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
])

assert test1 == True
assert test2 == False
