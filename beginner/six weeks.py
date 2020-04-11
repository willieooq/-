import random


chioce = 1
win,lose= 0,0
counter = 0
suit = {3:'黑桃',2:'紅心',1:'方塊',0:'梅花'}
        
poker = []
        
while( len(poker) != 53):
    poker.append(0)

while(True):
    print("比大小遊戲")
    
    chioce = input("請選擇 1:比大 2:比小 3:離開 \n")
    
    while(chioce != '1' and chioce != '2' and chioce != '3'):
        print("請輸入正確的數字喔！")
        chioce = input("請選擇 1:比大 2:比小 3:離開 \n")

        
    while(True):
        pl = random.randint(1,52)
        if(poker[pl] != 1):
            poker[pl] = 1
            break
    while(True):
        com = random.randint(1,52)
        if(poker[com] != 1):
            poker[com] = 1
            break
    pl_no = pl//4
    pl_su = suit[pl%4]
    com_no = com//4
    com_su = suit[com%4]
    if(pl_no == 0):
        pl_no= pl
    if(com_no == 0):
        com_no == com
        
    if(chioce == '1'):
        print("你抽到的牌為  :",pl_su,pl_no)
        print("電腦抽到的牌為:",com_su,com_no)
        if(pl > com ):
            print("你贏了\n")
            win+=1
        elif(pl < com ):
            print("你輸了\n")
            lose+=1
        else:
            if(pl_su > com_su):
                print("你贏了\n")
                win+=1
            else:
                print("你輸了\n")
                lose+=1

    elif(chioce == '2'):
        print("你抽到的牌為 :",pl_su,pl_no)
        print("電腦抽到的牌為:",com_su,com_no)
        if(pl < com ):
            print("你贏了\n")
            win+=1
        elif(pl > com ):
            print("你輸了\n")
            lose+=1
        else:
            if(pl_su < com_su):
                print("你贏了\n")
                win+=1
            else:
                print("你輸了\n")
                lose+=1
    elif(chioce == '3'):
        break


    counter+=1
    
    if(counter == 26):
        print("沒牌了喔！")
        break

    
print("你共贏了"+str(win)+"次")
print("你共輸了"+str(lose)+"次")

      
