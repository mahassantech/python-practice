even=0
odd=0
for i in  range(1,51):
    if i % 2==0:
        even=even+1
    else:
        odd=odd+1
print('even:', even)
print('odd:', odd)