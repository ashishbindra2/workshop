str1 = input("Enter the Some String: ") 

d = {} 
for x in str1: 
    if x in d.keys(): 
        d[x] = d[x] + 1  
    else: 
        d[x] = 1

for k, v in d.items(): 
        print(f"{k} = {v} Times")