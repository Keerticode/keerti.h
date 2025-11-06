import random
computer=random.choice([-1,0,1])
youStr=input("Enter your choice : ")
youDict={"s":1, "w":-1, "g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youStr]
print(f"Computer chooses {reverseDict[computer]}\nYou chooses{reverseDict[you]}")
if(computer==you):
     print("It is a Drawn")
     #if(computer==-1 and you==1): #diff(-1-1=-2)
       # print("You Wins")
    # elif(computer==-1 and you==0): #diff(-1-0=-1)
        #print("Computer Wins")
    # elif(computer==0 and you==-1):  #diff(0-(-1)=1)                  # Diffrence is done to check the pattern,so whenever there is 1 and -2 you wins and whwnever there is                                         
        #print("You Wins")                                                   -1,1,2 computer wins and you looses
    # elif(computer==0 and you==1): #diff(0-1=-1)
       # print("Computer Wins")
    # elif(computer==1 and you==-1): #diff(1+1=2)
       # print("Computer Wins")
    # elif(computer==1 and you==0): #diff(1-0=1)
        #print("You Wins")
    # else:
       # print("Something is Wrong")
if((computer-you)==1 and (computer-you)==-2):
     print("You Wins")
else:
     print("Computer Wins")


      


      