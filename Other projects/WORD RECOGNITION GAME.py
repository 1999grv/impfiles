print("HELLO AND WELCOME TO RANDOM-WORD-RECOGNITION-GAME")
for i in range(0,40):
    print("*",end=" ")
list=['r','h','y','t','h','m']
k=len(list)
new_list=[0]
for i in range(1,k):
    new_list.append(0)
s=0
score=0
print("RULES:1)plus 2 for correct attempt and minus 1 for incorrect")
print("IT BEGINS....")
for i in range(0,40):
    print("*",end=" ")
while(s!=k):
    print("enter random value!")
    d=input()
    g=0
    for i in range(0,6):
        w=list[i]
        if(d==w):
            new_list[i]=d
            g+=1
    if(g==0):
        print("sorry you lost ....enter again!")
        score-=1
    else:
        s+=1
        score+=2
        print(new_list)
        print("godd job!...going correct")
for i in range(0,40):
    print("*",end=" ")
print("congrats! you got the word")
print(new_list)
print("and your SCORE is ",score)
            
