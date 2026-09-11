class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}      # rows[r]  → set of digits seen in row r
        cols = {}      # cols[c]  → set of digits seen in column c
        boxes = {}     # boxes[(r//3, c//3)] → set of digits seen i

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_key = (r // 3, c // 3)

                # create the set for this group if we haven't seen it yet
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box_key not in boxes:
                    boxes[box_key] = set()

                # check before adding
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)

        return True
        