class Solution:
    def compress(self, c: list[str]) -> int:
        n = len(c)
        if n == 0: return 0
        w = 0
        r = 0
        while r < n:
            x = c[r]
            cnt = 0
            while r < n and c[r] == x:
                r += 1
                cnt += 1
            c[w] = x
            w += 1
            if cnt > 1:
                for d in str(cnt):
                    c[w] = d
                    w += 1
        return w