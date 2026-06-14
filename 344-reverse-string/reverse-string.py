class Solution:
    def reverseString(self, s: list[str]) -> None:
        stack =[]

        for ch in s:
            stack.append(ch)

        i=0
        while stack:
            s[i] =stack.pop()
            i +=1