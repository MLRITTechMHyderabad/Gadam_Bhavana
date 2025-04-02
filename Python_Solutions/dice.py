import random
d1= [1,2,3,4,5,6]
d2= [1,2,3,4,5,6]
li=[]
for i in d1:
    for j in d2:
        li.append((i,j))
print(li)

di = {}
for i in range(2, 13):
    c=0
    for j in li:
        if i==j[0]+j[1]:
            c+=1
    di[str(i)]=c/len(li)
print(di)

ply=int (input("enter no of rounds"))

for d in range(1,ply+1):
    ply1=random.randint(1, 6), random.randint(1,6)
    print (ply1)
    ply2=random.randint(1, 6), random.randint(1,6)
    print (ply2)
    score1=sum(ply1)
    score2=sum (ply2)
    
    if di[str(score1)]<di[str(score2)]:
        print("playerl wins")
    else:
        print ("player2 wins")