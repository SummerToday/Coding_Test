N, M = map(int, input().split()) 

max_value = 0

for i in range(N):
    data = list(map(int, input().split()))   
    max_value = max(max_value, min(data))

print(max_value)        
        
    
    
    
        
        