n=int(input())
number=''

for i in range(1,n+1):
    number=number+ '*'
    print(number)
    
# another way 

n=int(input())

for i in range(1,n+1):
    print('*' * i)