# map
m=list(map(int, input("Enter range of numbers ").split(" ")))
square_list=[]
for i in m:
    sq=lambda i:i*i
    square_list.append(sq(i))

print(square_list)



    
