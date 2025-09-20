class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        temp = ""
        for c in s:
            if c != ' ':
                temp += c
            elif temp !="":
                if ans == "":
                    ans = temp
                else:
                    ans = temp + " " + ans
                temp = ""
        
        if temp !="":
            if ans == "":
                ans = temp
            else:
                ans = temp + " " + ans
            temp = ""
        return ans