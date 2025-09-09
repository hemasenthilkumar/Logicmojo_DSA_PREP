class Solution:
    def nextLargerNodes(self, head):
        curr= head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        answer = [0] * len(vals)
        stack = []
        for i in range(len(vals)):
            while stack and vals[i] > vals[stack[-1]]:
                    answer[stack.pop()] = vals[i]
            stack.append(i)
        return answer