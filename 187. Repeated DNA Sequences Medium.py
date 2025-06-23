class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lengthofs=len(s)
        j=10
        hashset=set()
        repetedsequence=set()
        for i in range(lengthofs):
         if s[i:j] not in hashset:
          hashset.add(s[i:j])
         else:
          repetedsequence.add(s[i:j])
         if j==lengthofs:
          break
         j+=1
        return list(repetedsequence)


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10 or len(s) >= 10**5:
            return []

        WINDOWSIZE = 10
        WINDOWSIZE0 = 9
        BASE = 31
        BASE10 = pow(31, WINDOWSIZE0)
        MOD = (10**9) + 7
        T = lambda x: ord(x) - 40

        h = 0

        # encode
        for i, char in enumerate(s[:WINDOWSIZE]):
            h += (T(char) * pow(BASE, WINDOWSIZE0-i))

        h = h % MOD
        seen = set({h})
        res = set()

        for i in range(1, len(s) - (WINDOWSIZE0)):
            # remove first char/bit
            h -= (T(s[i-1]) * BASE10) % MOD

            # 1 power to each char -> (c1*BASE^9 + ... c10*BASE^0) * BASE -> (c1*BASE^10 + ... c10*BASE^1)
            # (c1*BASE^10 + ... c10*BASE^1) + c11*BASE^0
            char = s[i+WINDOWSIZE0]
            h = (h * BASE + T(char)) % MOD

            # print(f"removing {s[i-1]} [{T(s[i-1])}] | adding {char} [{T(char)}] | s={s[i:i+WINDOWSIZE]} | {h=}, {(T(s[i-1]) * BASE10)}")

            if h in seen:
                res.add(s[i:i+WINDOWSIZE])

            seen.add(h)

        # print(seen)
        return list(res)

        