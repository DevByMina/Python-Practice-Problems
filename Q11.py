prev=1
prevprev=0
print(prevprev," ", end="")
print(prev," ", end="")
for i in range(2,9):
    current=prev+prevprev
    print(current," ", end="")
    prevprev=prev
    prev=current