from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Construct Trie
        END_WORD = '-'

        trie = {}
        for word in words:
            node = trie
            for l in word:
                node = node.setdefault(l, {})
            node[END_WORD] = word

        mrows = len(board)
        ncols = len(board[0])
        result = []

        # Backtracking
        def backtracking(row, col, parent):
            l = board[row][col]
            curr_node = parent[l]

            # Check if we find a match of word
            word_match = currNode.pop(END_WORD, False)
            if word_match:
                result.append(word_match)
            
            board[row][col] = '#'

            for roff, coff in [(-1,0), (0,-1), (1,0), (0,1)]:
                nrow, ncol = row + roff, col + coff

                if 0 <= nrow < mrows and 0 <= ncol < ncols:
                    if not board[nrow][ncol] in curr_node:
                        continue
                        
                    backtracking(nrow, ncol, curr_node)
            
            # Cleanup
            board[row][col] = l

            if not currNode:
                parent.pop(l)
        

        # Then iterate through array checking in trie
        for r in range(mrows):
            for c in range(ncols):
                if board[r][c] in trie:
                    backtracking(r, c, trie)
        
        return result