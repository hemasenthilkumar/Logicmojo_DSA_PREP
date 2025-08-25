class Solution:
    def generateParenthesis(self, n: int):
        
        results = []
        open_count = 0
        close_count = 0
        string = []
        self.generate(n, open_count, close_count, string, results)
        return results
    
    def generate(self, n, open_count, close_count, string, results):

        # Terminating condition
        if len(string) == n * 2 or (close_count== n and open_count==n):
            results.append(''.join(string))
            return 
        
        # pruning condition
        # pick (
        if open_count < n:
            string.append('(')
            self.generate(n, open_count+1, close_count, string, results)
            string.pop()
        # pick )
        if close_count < n and close_count < open_count:
            string.append(')')
            self.generate(n, open_count, close_count+1, string, results)    
            string.pop()
