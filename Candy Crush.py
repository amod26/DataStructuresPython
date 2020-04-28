class Solution:
    def candyCrush(self, M):
        while True:
            # 1, Check
            crush = set()
            for i in range(len(M)):
                for j in range(len(M[0])):
                    if j > 1 and M[i][j] and M[i][j] == M[i][j - 1] == M[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
                    if i > 1 and M[i][j] and M[i][j] == M[i - 1][j] == M[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}

            # 2, Crush
            if not crush: break
            for i, j in crush: M[i][j] = 0

            # 3, Drop
            for j in range(len(M[0])):
                idx = len(M) - 1
                for i in reversed(range(len(M))):
                    if M[i][j]: M[idx][j] = M[i][j]; idx -= 1
                for i in range(idx + 1): M[i][j] = 0
        return M
