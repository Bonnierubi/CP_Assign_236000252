
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def sum_iterative(n):

    sum_num = 0
    
    for _val in range(n+1):
        # 下一项是前两项之和
        sum_num += _val 
    
    return sum_num