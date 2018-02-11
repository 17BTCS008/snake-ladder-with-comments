import random                                           #extracting random function
c=0                                                     #assigning initial value as 0
while(c<100):                                           #limiting the count value to 100
    a=input("enter 'r' to roll the dice: ")             #asking user to roll the dice by entering r
    if (a=='r'):                                        #giving the value of r to 'a' parameter
        r=random.randint(1,6)                           #printing random number from 1 to 6
        c=c+r                                           #adding count value with random value
        print('Dice value=',r)                          #printing the dice value
        print('count value=',c)                         #printing the count value

        if(c==8):                                       #if count value is equal to 8 then count value =37
            c=37
            print('you have climbed the ladder')        #print command 

        elif(c==13):                                    #else if count value is equal to 13 then count value=34
            c=34
            print('you have climbed the ladder')        #print command 

        elif(c==40):                                    #else if count value is equal to 40 then count value=68
            c=68
            print('you have climbed the ladder')        #print command 
        

        elif(c==52):                                    #else if count value is equal to 52 then count value=81
            c=81
            print('you have climbed the ladder')        #print command 
        
        elif(c==76):                                    #else if count value is equal to 76 then count value=97
            c=97
            print('you have climbed the ladder')        #print command 
        
        elif(c==11):                                    #else if count value is equal to 11 then count value=2
            c=2
            print('you were bitten by the snake')       #print command 
        
        elif(c==25):                                    #else if count value is equal to 25 then count value=4
            c=4
            print('you were bitten by the snake')       #print command 
        
        elif(c==38):                                    #else if count value is equal to 38 then count value=9
            c=9
            print('you were bitten by the snake')       #print command 
        
        elif(c==65):                                    #else if count value is equal to 65 then count value=46
            c=46
            print('you were bitten by the snake')       #print command 
        
        elif(c==89):                                    #else if count value is equal to 89 then count value=70
            c=70
            print('you were bitten by the snake')       #print command 
        
        elif(c==93):                                    #else if count value is equal to 93 then count value=64
            c=64
            print('you were bitten by the snake')       #print command 

        elif (c>100):                                   #else if count value exceeds 100
            c=c-r                                       #count=count-dice value
        elif (c==100):                                  #else if count value is equal to 100
            print('you won')                            #print command 
        

        
