class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        n = len(s)
        f_count = Counter(words)
        word_l = len(words[0])
        target = len(words)
        ans = []

        for i in range(word_l):
            left, right = i, i
            tem = deque([])
            cur_count = Counter()

            while right + word_l <= n:
                clip = s[right: right + word_l]
                right += word_l

                if clip in f_count:
                    tem.append(clip)
                    cur_count[clip] += 1

                    while cur_count[clip] > f_count[clip]:
                        cur_count[tem.popleft()] -= 1
                        left += word_l

                    if len(tem) == target:
                        ans.append(left)
                else:
                    tem.clear()
                    cur_count.clear()
                    left = right

        return ans

