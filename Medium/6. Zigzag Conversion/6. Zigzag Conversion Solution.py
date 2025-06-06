class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ["" for _ in range(0, numRows)]
        for i in range(0, len(s)):
            r = i % (2*numRows-2)
            if r < numRows:
                # r from 0 to numRows-1
                ans[r] += s[i]
            else:
                ans[2*numRows-2-r] += s[i]
        return "".join(ans)
        
