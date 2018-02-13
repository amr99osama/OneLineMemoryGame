import random
list=['a','b','c','d','e','f','g','h','i','j']
z=2*list
random.shuffle (z)
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,5,16,17,18,19,20]
print("WELCOME to the memory game!",y)
p1=0
p2=0
while(y!=['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']):
        print("player1 turn")
        n1=int(input("choose a number from the list above"))
        n2=int(input("choose another number from the list above"))
        y[n1-1]=z[n1-1]
        y[n2-1]=z[n2-1]
        print(y)
        if(y[n1-1]==y[n2-1]):
            y[n1-1]=y[n2-1]=z[n1-1]=z[n2-1]="*"
            p1=p1+1
            print ("p1=",p1,y)
        else:
            y[n1-1]=n1
            y[n2-1]=n2
            print("p1=",p1,y)
            print("player2 turn")
            n3=int(input("choose a number from the list above"))
            n4=int(input("choose another number from the list above"))
            y[n3-1]=z[n3-1]
            y[n4-1]=z[n4-1]
            print(y)
        if(y[n3-1]==y[n4-1]):
            y[n4-1]=y[n3-1]=z[n4-1]=z[n3-1]='*'
            p2=p2+1
            print ("p2=",p2,y)
        else:
            y[n3-1]=n3
            y[n4-1]=n4
            print("p2=",p2,y)
if(p1>p2):
    print("player one wins!!!")
else:
    print("player 2 wins!!!")
1