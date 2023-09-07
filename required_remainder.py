t = int(input())

for i in range(t):
    x, y, n = map(int, input().split())
    
    
    k = (n - y) // x * x + y
    
    
    if k < 0:
        k -= x
        
    print(k)
