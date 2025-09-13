
# TC: O(n^2)
# SC: O(1)
def stock_span_a1(arr):
    result =  [0] * len(arr)
    for i in range(len(arr)):
        j=i-1
        while j >= 0 and arr[j] <= arr[i]:
            j -= 1 
        result[i] = i - j 
    return result

def stock_span_a2(arr):
    min_stack = []
    result =  [0] * len(arr)
    for i in range(len(arr)):
        # top is less
        while min_stack and arr[min_stack[-1]] <= arr[i]:
            min_stack.pop()
        result[i]  = i-min_stack[-1] if min_stack else i+1
        min_stack.append(i)
                    
    return result
        

if __name__ == "__main__":
    x = stock_span_a1([100,80,60,70,60,75,86])
    print(x)