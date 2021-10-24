#My Big Tkinter Project: Catch The Gift
from tkinter import *
import winsound
import time
import random

#Background Music
winsound.PlaySound("BGM", winsound.SND_ASYNC | winsound.SND_ALIAS )

#Variables
user = ""
realchar = 0
lives_num = 1
win_score = 5
score_num = 0
char_x = 200
'''gift_x'''
gift_y = 80
gift_y2 = 80
catched1 = False
catched2 = False
win = False
diff = 0.1

giftList = list()

#this function is used to get the name of the user from the entry box
def getName():
    global user
    user = name.get() #input
    if user == "":
        startmenu.itemconfig(title5, state = NORMAL)
    else:
        root.destroy() #destroy the canvas
    
#this function shows different character based on the user's choice in the optionmenu
def characterChoice():
    global realchar
    #get the information from optionmenu
    finalc = variable1.get()
    finalt = variable2.get()
    
    #show different characters based on different choices
    if finalc == "Girl" and finalt == "Plate":
        decmenu.itemconfigure(showgirl, state = NORMAL)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = NORMAL)
        decmenu.itemconfigure(showpot, state = HIDDEN)
        
        realchar = 1
        GoPlay()
        
    elif finalc == "Boy" and finalt == "Plate":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = NORMAL)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = NORMAL)
        decmenu.itemconfigure(showpot, state = HIDDEN)  
        
        realchar = 2
        GoPlay()
                
    elif finalc == "Kangaroo" and finalt == "Plate":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = NORMAL)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = NORMAL)
        decmenu.itemconfigure(showpot, state = HIDDEN)       
        
        realchar = 3
        GoPlay()
                
    elif finalc == "Sloth" and finalt == "Plate":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = NORMAL)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = NORMAL)
        decmenu.itemconfigure(showpot, state = HIDDEN)    
        
        realchar = 5
        GoPlay()
                
    elif finalc == "Koala" and finalt == "Plate":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = NORMAL)
        decmenu.itemconfigure(showplate, state = NORMAL)
        decmenu.itemconfigure(showpot, state = HIDDEN) 
        
        realchar = 4
        GoPlay()
                
    elif finalc == "Girl" and finalt == "Pot":
        decmenu.itemconfigure(showgirl, state = NORMAL)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = HIDDEN)
        decmenu.itemconfigure(showpot, state = NORMAL)     
        
        realchar = 6
        GoPlay()
                
    elif finalc == "Boy" and finalt == "Pot":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = NORMAL)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = HIDDEN)
        decmenu.itemconfigure(showpot, state = NORMAL)  
        
        realchar = 7
        GoPlay()
                
    elif finalc == "Kangaroo" and finalt == "Pot":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = NORMAL)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = HIDDEN)
        decmenu.itemconfigure(showpot, state = NORMAL)   
        
        realchar = 8
        GoPlay()
                
    elif finalc == "Sloth" and finalt == "Pot":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = NORMAL)
        decmenu.itemconfigure(showkoala, state = HIDDEN)
        decmenu.itemconfigure(showplate, state = HIDDEN)
        decmenu.itemconfigure(showpot, state = NORMAL)    
        
        realchar = 10
        GoPlay()
                
    elif finalc == "Koala" and finalt == "Pot":
        decmenu.itemconfigure(showgirl, state = HIDDEN)
        decmenu.itemconfigure(showboy, state = HIDDEN)
        decmenu.itemconfigure(showkan, state = HIDDEN)
        decmenu.itemconfigure(showsloth, state = HIDDEN)
        decmenu.itemconfigure(showkoala, state = NORMAL)
        decmenu.itemconfigure(showplate, state = HIDDEN)
        decmenu.itemconfigure(showpot, state = NORMAL)  

        realchar = 9
        GoPlay()        
    
    decmenu.update()

#this function makes a button that continues the game after the user finished choosing the character
def GoPlay():
    #show the go play button
    GoPlay = decmenu.create_window(350,530, window = (Button(root, text = "Next ==>", font = ("helvetica, 8"), bg = "light yellow", command = destroysecond)))
    
def destroysecond():
    root.destroy()   #destroy the canvas
 
#set the difficulty of the game to easy
def easydif():
    global diff
    #reset the speed of gift falling
    diff = 0.2
    root.destroy()
    
#set the difficulty of the game to medium
def meddif():
    global diff
    #reset the speed of gift falling
    diff = 0.1
    root.destroy()

#set the difficulty of the game to hard
def harddif():
    global diff
    #reset the speed of gift falling
    diff = 0.05
    root.destroy()

#this function displays the character image on the gamearea canvas based on the user's choice
def realcharacter():
    global realchar, showc
    #based on user's choice show different characters
    if realchar == 1:
        showc = gamearea.create_image(char_x,520,image = girlplate)
    elif realchar == 2:
        showc = gamearea.create_image(char_x,520,image = boyplate)
    elif realchar == 3:
        showc = gamearea.create_image(char_x,520,image = kanplate)
    elif realchar == 4:
        showc = gamearea.create_image(char_x,520,image = koalaplate)
    elif realchar == 5:
        showc = gamearea.create_image(char_x,520,image = slothplate)
    elif realchar == 6:
        showc = gamearea.create_image(char_x,520,image = girlpot)
    elif realchar == 7:
        showc = gamearea.create_image(char_x,520,image = boypot)
    elif realchar == 8:
        showc = gamearea.create_image(char_x,520,image = kanpot)
    elif realchar == 9:
        showc = gamearea.create_image(char_x,520,image = koalapot)
    else:
        showc = gamearea.create_image(char_x,520,image = slothpot)
    
    gamearea.update()


def destroyIns():
    #delete all the previous information on the canvas
    gamearea.delete(showtemp)
    gamearea.delete(ins1)
    gamearea.delete(ins2)
    gamearea.delete(showkey)
    gamearea.delete(showarrow1)
    gamearea.delete(showarrow2)
    gamearea.delete(GotItButton)
    
    #stop the music
    winsound.PlaySound(None, winsound.SND_ASYNC)
    
    gamearea.update()

    '''
    #test
    global score_num,lives_num
    score_num = 5
    lives_num = 1
    fallList[0].gift_x = 200
    fallList[0].gift_y = 440
    fallList[0].catched = False
    fallList[0].gift = gift
    
    fallList[1].gift_x = 220
    fallList[1].gift_y = 440
    fallList[1].catched = False
    fallList[1].gift = bomb
    
    #test case 1
    goIng = catchCheck(200)
    for i in range(2):
        if fallList[i].catched:
            print(f"Gift {i} is catched")
        else:
            print(f"Gift {i} is not catched")
    
    # test case 2
    score_num = 5
    lives_num = 1
    fallList[0].gift_x = 200
    fallList[0].gift_y = 440
    fallList[0].catched = False
    fallList[0].gift = gift
    
    fallList[1].gift_x = 220
    fallList[1].gift_y = 440
    fallList[1].catched = False
    fallList[1].gift = bomb
    
    goIng = catchCheck(120)
    for i in range(2):
        if fallList[i].catched:
            print(f"Gift {i} is catched")
        else:
            print(f"Gift {i} is not catched")
    '''
    
    startcountdown()

#this functions starts a countdown before the game actually starts

def startcountdown():
    #countdown 3-2-1 animation
    #sound effects
    winsound.PlaySound("Tick", winsound.SND_ASYNC | winsound.SND_ALIAS ) 
    #show each number only about a second
    for a in range(60):
        gamearea.itemconfigure(count3, state = NORMAL) 
        root.update()
        time.sleep(0.01)  
    winsound.PlaySound("Tick", winsound.SND_ASYNC | winsound.SND_ALIAS )
    for b in range(60):
        gamearea.itemconfigure(count3, state = HIDDEN)
        gamearea.itemconfigure(count2, state = NORMAL) 
        root.update()
        time.sleep(0.01)  
    winsound.PlaySound("Tick", winsound.SND_ASYNC | winsound.SND_ALIAS )
    for c in range(60):
        gamearea.itemconfigure(count2, state = HIDDEN)
        gamearea.itemconfigure(count1, state = NORMAL)   
        root.update()
        time.sleep(0.01) 
    
    #delete them after
    gamearea.delete(count3)
    gamearea.delete(count2)
    gamearea.delete(count1)                      
    
    gamearea.update()
    
    #start the real game functionalities
    realcharacter()   #choose the character
    livescount()   #count the lives
    scorecount()   #count the score
    
    #always display the user's name on the screen
    showplayer = gamearea.create_text(58,45, text = "Player: ", font = ("rockwell", 16), fill = "white")
    showuser = gamearea.create_text(98,45, text = user, font = ("rockwell", 16), fill = "white", anchor = W)
    showsc = gamearea.create_text(52,72, text = "Score:", font = ("rockwell", 16), fill = "white")

    goIng = True
    while goIng:
        goIng = fallingGift() #control how the gifts fall from the sky
    
#this function counts the number of lives
def livescount():
    global lives_num, win
    goIng = True
    #based on the number of lives left, display the number of lives to the user
    if lives_num == 3:
        gamearea.itemconfigure(lives1, state = NORMAL)
        gamearea.itemconfigure(lives2, state = NORMAL)
        gamearea.itemconfigure(lives3, state = NORMAL)
    elif lives_num == 2:
        gamearea.itemconfigure(lives1, state = HIDDEN)
        gamearea.itemconfigure(lives2, state = NORMAL)
        gamearea.itemconfigure(lives3, state = NORMAL) 
    elif lives_num == 1:
        gamearea.itemconfigure(lives1, state = HIDDEN)
        gamearea.itemconfigure(lives2, state = HIDDEN)
        gamearea.itemconfigure(lives3, state = NORMAL) 
    else:
        gamearea.itemconfigure(lives1, state = HIDDEN)
        gamearea.itemconfigure(lives2, state = HIDDEN)
        gamearea.itemconfigure(lives3, state = HIDDEN)   
        
        #if there's no lives left, the player loses
        win = False
        root.destroy()
        goIng = False
        return goIng
    
    gamearea.update()
    return goIng

#this function counts the score number
def scorecount():
    global score_num, showscore, win, win_score
    goIng = True
    #the score stays the same in the beginning
    if score_num == 0:
        showscore = gamearea.create_text(91,72, text = str(score_num), font = ("rockwell", 16), fill = "white", anchor = W)
    #if the player catches a gift, the score increases
    else:
        gamearea.delete(showscore)
        showscore = gamearea.create_text(91,72, text = str(score_num), font = ("rockwell", 16), fill = "white", anchor = W)
    
    #if the score reaches 26, the player wins
    if score_num >= win_score:
        win = True
        root.destroy()
        goIng = False
        return goIng
            
    gamearea.update()
    return goIng

#this function moves the character left or right based on the key that the player presses, thus changing the location of the character
def changeLocation():
    global showc, char_x
    
    #delete the original character
    gamearea.delete(showc)
    
    #recreates the character at the new location
    if realchar == 1:
        showc = gamearea.create_image(char_x,520,image = girlplate)
    elif realchar == 2:
        showc = gamearea.create_image(char_x,520,image = boyplate)
    elif realchar == 3:
        showc = gamearea.create_image(char_x,520,image = kanplate)
    elif realchar == 4:
        showc = gamearea.create_image(char_x,520,image = koalaplate)
    elif realchar == 5:
        showc = gamearea.create_image(char_x,520,image = slothplate)
    elif realchar == 6:
        showc = gamearea.create_image(char_x,520,image = girlpot)
    elif realchar == 7:
        showc = gamearea.create_image(char_x,520,image = boypot)
    elif realchar == 8:
        showc = gamearea.create_image(char_x,520,image = kanpot)
    elif realchar == 9:
        showc = gamearea.create_image(char_x,520,image = koalapot)    
    else:
        showc = gamearea.create_image(char_x,520,image = slothpot)    

    gamearea.update()

#move the character left
def moveLeft(event):
    global char_x, showc
    
    #make a boundary for the character
    if char_x < 60:
        char_x = 60
    #otherwise move the character left
    else:
        char_x = char_x - 20
        changeLocation()
        
    gamearea.update()

#move the character right
def moveRight(event):
    global char_x, showc
    
    #make a boundary for the character
    if char_x > 340:
        char_x = 340
    #otherwise move the character right
    else:
        char_x = char_x + 20
        changeLocation()
        
    gamearea.update()    

#this function randomizes the gifts that are falling
def chooseGift():
    n = len(giftList)
    #randomize the objects of the gifts
    giftIndex = random.randint(0,n-1)
    gamearea.update() #then show the gifts based on the randomized gifts
    return giftList[giftIndex]

    # global gift
    # #then show the gifts based on the randomized gifts
    # if giftnum == 1:
    #     gift = apple
    # elif giftnum == 2:
    #     gift = banana
    # elif giftnum == 3:
    #     gift = strawberry
    # elif giftnum == 4:
    #     gift = kiwi
    # elif giftnum == 5:
    #     gift = emoji1
    # elif giftnum == 6:
    #     gift = gift2
    # elif giftnum == 7:
    #     gift = candy
    # elif giftnum == 8:
    #     gift = candycane
    # elif giftnum == 9:
    #     gift = chocolate
    # elif giftnum == 10:
    #     gift = emoji2
    # else:
    #     gift = bomb
    #
    # gamearea.update()
    # return gift


class fallGift: #20210425
    def __init__(self, type, pos_x, pos_y):
        self.gift = type # fall gift type
        self.gift_x = pos_x #fall gift x position
        self.gift_y = pos_y #fall gift y position
        self.fallgift = 0 #image object
        self.catched = True

#this function makes the gift fall from top to bottom at a constant speed
def fallingGift():
    global char_x, test
    #randomize the location (y-coordinate) where the gift falls
    # for i in range(0,26):
    for j in range(len(fallList)):
        if  fallList[j].gift_y==80:
            fallList[j].gift_x = random.randint(3, 17) * 20
            # randomize the gifts when falling
            fallList[j].gift = chooseGift()
            fallList[j].catched = False
            # create the gift at the top
            fallList[j].fallgift = gamearea.create_image(fallList[j].gift_x, fallList[j].gift_y, image = fallList[j].gift)

        elif fallList[j].gift_y>80 and fallList[j].gift_y<560 and fallList[j].catched == False:# i < 24 and
            #delete the original gift
            gamearea.delete(fallList[j].fallgift)
            #recreates the gift at the new location as it fallsf
            fallList[j].fallgift = gamearea.create_image(fallList[j].gift_x, fallList[j].gift_y, image = fallList[j].gift)

        fallList[j].gift_y = fallList[j].gift_y + 20
    root.update()
    #the gifts fall at the speed that the user determines the difficulty
    time.sleep(diff)

    goIng = True
    #check if the gift is catched or not
    goIng = catchCheck(char_x)
    if not goIng:
        return goIng

    #if the gift reached the bottom, delete it
    for j in range(len(fallList)):
        if fallList[j].gift_y >= 560:
            if not fallList[j].catched:
                gamearea.delete(fallList[j].fallgift)
            fallList[j].gift_y = 80
    gamearea.update()
    return goIng

#this function checks if the character catches the first gift
def catchCheck(char_x):
    global score_num, lives_num  #gift gift_x, gift_y,

    goIng = True
    n = len(fallList)
    for i in range(n):
        gift_x = fallList[i].gift_x
        gift_y = fallList[i].gift_y
        gift = fallList[i].gift
        fallgift = fallList[i].fallgift
        catched = fallList[i].catched

        if not catched:
        #if the player catches a bomb
            if gift_y >= 440 and gift_y <= 460 and char_x >= gift_x-20 and char_x <= gift_x + 20 and gift == bomb:
                gamearea.delete(fallgift)
                showblast = gamearea.create_image(gift_x, gift_y, image = blast) #blast animation
                winsound.PlaySound("BombSound", winsound.SND_ASYNC | winsound.SND_ALIAS ) #sound effect
                root.update()
                time.sleep(0.25)
                lives_num = lives_num - 1   #loses one life
                goIng = livescount()
                if not goIng:
                    return goIng
                gamearea.delete(showblast)   #delete the blast
                catched = True   #the gift is catched

            #if the player catches an emoji
            elif gift_y >= 440 and gift_y <= 460 and char_x >= gift_x-20 and char_x <= gift_x + 20 and (gift == emoji1 or gift == emoji2):
                winsound.PlaySound("Laugh", winsound.SND_ASYNC | winsound.SND_ALIAS ) #sound effect
                score_num = score_num + 1  #score adds 1
                goIng = scorecount()
                if not goIng:
                    return goIng
                gamearea.delete(fallgift)   #delete the emoji
                catched = True   #the gift is catched

            #if the player catches other gifts
            elif gift_y >= 440 and gift_y <= 460 and char_x >= gift_x-20 and char_x <= gift_x + 20:
                winsound.PlaySound("Pop", winsound.SND_ASYNC | winsound.SND_ALIAS ) #sound effect
                score_num = score_num + 1   #score adds 1
                goIng = scorecount()
                if not goIng:
                    return goIng
                gamearea.delete(fallgift)   #delete the gift
                catched = True   #the gift is catched
        fallList[i].catched = catched
    gamearea.update()
    return goIng


#this function displays the easter egg
def showEasterEgg():
    
    winsound.PlaySound("Typing", winsound.SND_ASYNC | winsound.SND_ALIAS ) #sound effect
    end.delete(easterEgg)
    showendBack = end.create_image(200,310,image = endBack)
    showtrans2 = end.create_image(202,312, image = trans2)    
    
    texts = "Dear Player,Hope you enjoyed my game~This is the first game I ever made :)Again, thanks for playing~From Wendy"  #length 110
    
    #display the characters (words) one by one
    for a in range(1,13):   #first line
        showtext1 = end.create_text(50,100, text = texts[0:a], font = ("forte", 18), fill = "white", anchor = NW)
        root.update()
        time.sleep(0.1)
        if a < 12:
            end.delete(showtext1)
     
    for b in range(13,38):   #second line
        showtext2 = end.create_text(50,170, text = texts[12:b], font = ("forte", 18), fill = "white", anchor = NW)
        root.update()
        time.sleep(0.1)
        if b < 37:
            end.delete(showtext2)    
    
    for c in range(38,68):   #third line
        showtext3 = end.create_text(50,210, text = texts[37:c], font = ("forte", 18), fill = "white", anchor = NW)
        root.update()
        time.sleep(0.1)
        if c < 67:
            end.delete(showtext3)     
        
    for d in range(68,75):   #fourth line
        showtext4 = end.create_text(50,250, text = texts[67:d], font = ("forte", 18), fill = "white", anchor = NW)
        root.update()
        time.sleep(0.1)
        if d < 74:
            end.delete(showtext4)   
            
    for e in range(75,101):   #fifth line
        showtext5 = end.create_text(50,290, text = texts[74:e], font = ("forte", 18), fill = "white", anchor = NW)
        root.update()
        time.sleep(0.1)
        if e < 100:
            end.delete(showtext5)        
    
    for f in range(101,111):   #last line
        showtext6 = end.create_text(240,400, text = texts[100:f], font = ("forte", 18), fill = "white", anchor = NW)
        root.update()
        time.sleep(0.1)
        if f < 110:
            end.delete(showtext6)         
            
    winsound.PlaySound(None, winsound.SND_ASYNC)  #stop the sound effect
    #Exit Button
    exit = end.create_window(355,565, window = (Button(root, text = "Exit", font = ("helvetica, 7"), bg = "light yellow", command = exiting)))    
    
    end.update()
    
def exiting():
    root.destroy()  #destroy the canvas


#The Start Menu
root = Tk()
startmenu = Canvas (root, width = 400, height = 620, bg = "light yellow")
startmenu.pack() 

#Cursor shape
root.configure(cursor = "heart")

#background
introBack = PhotoImage(file = "Background.gif")
introBack = introBack.subsample(3)
showintroBack = startmenu.create_image(200,310,image = introBack)

#titles (texts)
title11 = startmenu.create_text(205,175, text = "Welcome To", font = ("showcard gothic", 30), fill = "black")
title1 = startmenu.create_text(200,170, text = "Welcome To", font = ("showcard gothic", 30), fill = "white")
title22 = startmenu.create_text(205,235, text = "Catch The Gift", font = ("showcard gothic", 35), fill = "black")
title2 = startmenu.create_text(200,230, text = "Catch The Gift", font = ("showcard gothic", 35), fill = "white")

#import images
sgift = PhotoImage(file = "StartGift.png")
sgift = sgift.subsample(21)
showsgift = startmenu.create_image(200,495, image = sgift, state = NORMAL)

ogift = PhotoImage(file = "GiftOpen.png")
ogift = ogift.subsample(5)
showogift = startmenu.create_image(208,475, image = ogift, state = HIDDEN)

#animation of a gift opening
for i in range(4): #repeat the action 4 times
    for a in range(30): #show the first image, then hide it
        startmenu.itemconfigure(showsgift, state = HIDDEN) 
        startmenu.itemconfigure(showogift, state = NORMAL) 
        root.update()
        time.sleep(0.01)
        
    for b in range(30):#show the second image, then hide it
        startmenu.itemconfigure(showogift, state = HIDDEN) 
        startmenu.itemconfigure(showsgift, state = NORMAL) 
        root.update()
        time.sleep(0.01)        

title3 = startmenu.create_text(200,310, text = "Please enter your name", font = ("forte", 15), fill = "white")
title4 = startmenu.create_text(200,70, text = "Please turn on your volume to listen to the BGM", font = ("forte", 10), fill = "white")

name = StringVar()  #control
nameEntry = startmenu.create_window(200,350, window = Entry(startmenu, font = ("helvetica, 16"), textvariable = name))  #entry box to enter the name
startGame = startmenu.create_window(285,390,window = Button(startmenu, text = "Start Game!", font = ("helvetica, 9"), bg = "light yellow", command = getName))
title5 = startmenu.create_text(200,285, text = "Your name cannot be BLANK!", font = ("forte", 10), fill = "white", state = HIDDEN)

mainloop()


#Second canvas: the decoration menu 第2个阶段 选角色和容器
root = Tk()
decmenu = Canvas (root, width = 400, height = 620, bg = "light yellow")
decmenu.pack() 

#Cursor shape
root.configure(cursor = "heart")

#background
decBack = PhotoImage(file = "Background.gif")
decBack = decBack.subsample(3)
showdecBack = decmenu.create_image(200,310,image = decBack)

#Imported images
girl = PhotoImage(file = "Girl.png")
girl1 = girl.subsample(5)
showgirl = decmenu.create_image(200,490, image = girl1, state = HIDDEN)

boy = PhotoImage(file = "Boy.png")
boy1 = boy.subsample(4)
showboy = decmenu.create_image(205,495, image = boy1, state = HIDDEN)

kangaroo = PhotoImage(file = "Kan.png")
kangaroo1 = kangaroo.subsample(2)
showkan = decmenu.create_image(190,505, image = kangaroo1, state = HIDDEN)

sloth = PhotoImage(file = "Sloth1.png")
sloth1 = sloth.subsample(3)
showsloth = decmenu.create_image(200,490, image = sloth1, state = HIDDEN)

koala = PhotoImage(file = "Koala.png")
koala1 = koala.subsample(8)
showkoala = decmenu.create_image(200,495, image = koala1, state = HIDDEN)

plate = PhotoImage(file = "Plate.png")
plate1 = plate.subsample(19)
showplate = decmenu.create_image(200,430, image = plate1, state = HIDDEN)

pot = PhotoImage(file = "Pot.png")
pot1 = pot.subsample(12)
showpot = decmenu.create_image(200,425, image = pot1, state = HIDDEN)

#titles (texts)
dectitle11 = decmenu.create_text(210,75, text = "Make Your", font = ("showcard gothic", 30), fill = "black")
dectitle1 = decmenu.create_text(200,70, text = "Make Your", font = ("showcard gothic", 30), fill = "white")

dectitle22 = decmenu.create_text(210,125, text = "Character", font = ("showcard gothic", 30), fill = "black")
dectitle2 = decmenu.create_text(200,120, text = "Character", font = ("showcard gothic", 30), fill = "white")

#The optionmenu
variable1 = StringVar(root)
variable1.set("Characters")  #set the variable

menu1 = OptionMenu(root, variable1, "Girl", "Boy", "Kangaroo", "Koala", "Sloth")
menu1.config(bg = "misty rose")
menu11 = decmenu.create_window(120,190, window = menu1)

variable2 = StringVar(root)
variable2.set("Catching Tool")  #set the variable

menu2 = OptionMenu(root, variable2, "Plate", "Pot")
menu2.config(bg = "misty rose")
menu22 = decmenu.create_window(280,190, window = menu2)

#Button to confirm and get the information from the optionmenu
ConfirmButton = decmenu.create_window(350,240, window = (Button(root, text = "Confirm", font = ("helvetica, 7"), bg = "light yellow", command = characterChoice)))

mainloop()


#Third Canvas: Choosing Difficulty Tab
root = Tk()
difficulty = Canvas (root, width = 400, height = 620, bg = "light yellow")
difficulty.pack() 

#Cursor shape
root.configure(cursor = "heart")

#background
difBack = PhotoImage(file = "Background2.gif")
difBack = difBack.subsample(3)
showdifBack = difficulty.create_image(200,310,image = difBack)

#titles (texts)
diftitle11 = difficulty.create_text(210,75, text = "Choose The", font = ("showcard gothic", 30), fill = "black")
diftitle1 = difficulty.create_text(200,70, text = "Choose The", font = ("showcard gothic", 30), fill = "white")

diftitle22 = difficulty.create_text(210,125, text = "Difficulty", font = ("showcard gothic", 30), fill = "black")
diftitle2 = difficulty.create_text(200,120, text = "Difficulty", font = ("showcard gothic", 30), fill = "white")

#difficulty buttons
easyButton = difficulty.create_window(200,210, window = (Button(root, text = "Easy", font = ("rockwell", 25), bg = "light yellow", command = easydif)))
medButton = difficulty.create_window(200,310, window = (Button(root, text = "Medium", font = ("rockwell", 25), bg = "light yellow", command = meddif)))
hardButton = difficulty.create_window(200,410, window = (Button(root, text = "Hard", font = ("rockwell", 25), bg = "light yellow", command = harddif)))

#side notes
difarrow = PhotoImage(file = "DifArrow.png")
difarrow = difarrow.subsample(5)
showdifarrow = difficulty.create_image(300,312,image = difarrow)
recommend = difficulty.create_text(358,310, text = "Recommended", font = ("rockwell", 8), fill = "black")

mainloop()


#Gamearea Canvas
root = Tk()
gamearea = Canvas (root, width = 400, height = 620, bg = "light yellow")
gamearea.pack() 

#Cursor shape
root.configure(cursor = "heart")

#background
gameBack = PhotoImage(file = "Background2.gif")
gameBack = gameBack.subsample(3)
showgameBack = gamearea.create_image(200,310,image = gameBack)

#Instructions
tempback = PhotoImage(file = "Translucent1.png")
showtemp = gamearea.create_image(203,310,image = tempback)

ins1 = gamearea.create_text(140,175, text = "Instructions:", font = ("rockwell", 20), fill = "black")

ins2 = gamearea.create_text(202,305, text = '- There will be gifts falling from the sky\n  Move your character left and right to catch the gifts\n\n- Press key "a" to move left, key "d" to move right\n\n\n\n\n- You have 1 live\n\n- If you catch a bomb, you lose one life\n\n- You will win if your score reaches 5 and you live until\n   the end :)', font = ("rockwell", 10), fill = "black")

key = PhotoImage(file = "Key.png")
key = key.subsample(2)
showkey = gamearea.create_image(200,295,image = key)

arrow1 = PhotoImage(file = "Arrow1.png")
arrow1 = arrow1.subsample(18)
showarrow1 = gamearea.create_image(152,300,image = arrow1)

arrow2 = PhotoImage(file = "Arrow2.png")
arrow2 = arrow2.subsample(18)
showarrow2 = gamearea.create_image(250,300,image = arrow2)

#Button to actually start the game
#Initiate fall gift list 20210425
fallList = list() #20210425 Put two object
fallList.append(fallGift(0,0,80))
fallList.append(fallGift(0,0,-12 * 20))
GotItButton = gamearea.create_window(200,445, window = (Button(root, text = "Got It!", font = ("helvetica, 9"), bg = "light yellow", command = destroyIns)))

#Characters image Import
girlplate = PhotoImage(file = "GirlPlate.png")
girlplate = girlplate.subsample(2)

boyplate = PhotoImage(file = "BoyPlate.png")
boyplate = boyplate.subsample(2)

kanplate = PhotoImage(file = "KanPlate.png")
kanplate = kanplate.subsample(2)

koalaplate = PhotoImage(file = "KoalaPlate.png")
koalaplate = koalaplate.subsample(2)

slothplate = PhotoImage(file = "SlothPlate.png")
slothplate = slothplate.subsample(2)

girlpot = PhotoImage(file = "GirlPot.png")
girlpot = girlpot.subsample(2)

boypot = PhotoImage(file = "BoyPot.png")
boypot = boypot.subsample(2)

kanpot = PhotoImage(file = "KanPot.png")
kanpot = kanpot.subsample(2)

koalapot = PhotoImage(file = "KoalaPot.png")
koalapot = koalapot.subsample(2)

slothpot = PhotoImage(file = "SlothPot.png")
slothpot = slothpot.subsample(2)

#Key Presses (left and right)
root.bind('<a>', moveLeft)
root.bind('<d>', moveRight) 

#Start time countdown
count3 = gamearea.create_text(200,300, text = "3", font = ("rockwell", 50), fill = "white", state = HIDDEN)
count2 = gamearea.create_text(200,300, text = "2", font = ("rockwell", 50), fill = "white", state = HIDDEN)
count1 = gamearea.create_text(200,300, text = "1", font = ("rockwell", 50), fill = "white", state = HIDDEN)

#Lives count
lives = PhotoImage(file = "Lives.png")
lives = lives.subsample(5)
lives1 = gamearea.create_image(310,30,image = lives, state = HIDDEN)
lives2 = gamearea.create_image(345,30,image = lives, state = HIDDEN)
lives3 = gamearea.create_image(380,30,image = lives, state = HIDDEN)

#3b Falling Gifts image import
apple = PhotoImage(file = "Apple.png")
apple = apple.subsample(5)
giftList.append(apple)

banana = PhotoImage(file = "Banana.png")
banana = banana.subsample(5)
giftList.append(banana)

strawberry = PhotoImage(file = "Strawberry.png")
strawberry = strawberry.subsample(5)
giftList.append(strawberry)

gift2 = PhotoImage(file = "Gift2.png")
gift2 = gift2.subsample(5)
giftList.append(gift2)

kiwi = PhotoImage(file = "Kiwi.png")
kiwi = kiwi.subsample(5)
giftList.append(kiwi)

candy = PhotoImage(file = "Candy.png")
candy = candy.subsample(5)
giftList.append(candy)

candycane = PhotoImage(file = "CandyCane.png")
candycane = candycane.subsample(5)
giftList.append(candycane)

chocolate = PhotoImage(file = "Chocolate.png")
chocolate = chocolate.subsample(5)
giftList.append(chocolate)

emoji1 = PhotoImage(file = "Emoji1.png")
emoji1 = emoji1.subsample(13)
giftList.append(emoji1)

emoji2 = PhotoImage(file = "Emoji2.png")
emoji2 = emoji2.subsample(5)
giftList.append(emoji2)

bomb = PhotoImage(file = "Bomb.png")
bomb = bomb.subsample(5)
giftList.append(bomb)
giftList.append(bomb)
giftList.append(bomb)

blast = PhotoImage(file = "Blast.png")
blast = blast.subsample(8)

mainloop()


#Last canvas: the end game tab
root = Tk()
end = Canvas (root, width = 400, height = 620, bg = "light yellow")
end.pack() 

#Cursor shape
root.configure(cursor = "heart")

#background
endBack = PhotoImage(file = "Background2.gif")
endBack = endBack.subsample(3)
showendBack = end.create_image(200,310,image = endBack)

trans2 = PhotoImage(file = "Translucent2.png")
trans2 = trans2.subsample(1)
showtrans2 = end.create_image(202,312, image = trans2)

#if the player wins
if win == True:
    winsound.PlaySound("Applause", winsound.SND_ASYNC | winsound.SND_ALIAS ) #sound effect
    #show texts
    winning1 = end.create_text(210,160, text = "YOU WON!", font = ("showcard gothic", 45), fill = "black")
    winning = end.create_text(200,150, text = "YOU WON!", font = ("showcard gothic", 45), fill = "white")
    
    happy = PhotoImage(file = "Happy.png")
    happy = happy.subsample(6)
    showhappy = end.create_image(200,270, image = happy)
    
    root.update()
    time.sleep(1.5)    
    
#if the player loses
else:
    winsound.PlaySound("Lose", winsound.SND_ASYNC | winsound.SND_ALIAS ) #sound effect
    #showtexts
    losing1 = end.create_text(210,160, text = "YOU LOST!", font = ("showcard gothic", 45), fill = "black")    
    losing = end.create_text(200,150, text = "YOU LOST!", font = ("showcard gothic", 45), fill = "white")  
    
    sad = PhotoImage(file = "Sad.png")
    sad = sad.subsample(4)
    showsad = end.create_image(200,270, image = sad)   
    
    root.update()
    time.sleep(1.75)      
    
#show the username, final score, and lives left
username1 = end.create_text(200,360, text = user, font = ("forte", 20), fill = "white")
username2 = end.create_text(200,395, text = "Your final score is " + str(score_num), font = ("forte", 20), fill = "white")
username3 = end.create_text(200,430, text = "You have " + str(lives_num) + " lives left", font = ("forte", 20), fill = "white")

#show the text: thank you for playing
thanks11 = end.create_text(210,490, text = "THANK U", font = ("showcard gothic", 30), fill = "black")
thanks1 = end.create_text(200,485, text = "THANK U", font = ("showcard gothic", 30), fill = "light blue")
thanks22 = end.create_text(210,540, text = "FOR PLAYING", font = ("showcard gothic", 30), fill = "black")
thanks2 = end.create_text(200,535, text = "FOR PLAYING", font = ("showcard gothic", 30), fill = "light blue")

#Easter egg button
easterEgg = end.create_window(45,65, window = (Button(root, text = "!!!", font = ("helvetica, 7"), bg = "gray", command = showEasterEgg)))

#Exit Button
exit = end.create_window(355,565, window = (Button(root, text = "Exit", font = ("helvetica, 7"), bg = "light yellow", command = exiting)))



mainloop()
