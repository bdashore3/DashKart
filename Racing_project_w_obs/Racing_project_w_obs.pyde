"""
(c) Brian Dashore and Rudra Amin
01/25/2018
A fun racing game for ages 5-99
"""
add_library('sound')#to add sound
#various variables for moving, car points, obstacle points, and obstacle moves
ob1_x = 380
ob1_y = 56
ob2_x = 125
ob2_y = 310
ob3_x = 55
ob3_y = 513
ob4_x = 295
ob4_y = 570
ob5_x = 365
ob5_y = 597
ob6_x = 444
ob6_y = 626
ob7_x = 547
ob7_y = 442
ob8_x = 600
ob8_y = 360
ob9_x = 547
ob9_y = 301
ob10_x = 596
ob10_y = 226
ob1_move = 2
ob3_move = 2
ob4_move = 2
ob5_move = 2
ob6_move = 2
ob7_move = 2
ob8_move = 2
ob9_move = 2
ob10_move = 2
score1=False
score2=False
lap_1=0
lap_2=0
left=False
right=False
up=False
down=False
leftarr=False
rightarr=False
uparr=False
downarr=False
car1_height = 20
car1_width=20
car1_x=245
car1_y=64
car1_move=15
barrier_x=0
barrier_y=0
barrier_width=700
barrier_height=700
car2_height = 20
car2_width=20
car2_x=244
car2_y=119
car2_move=15
def setup():
    global sf#global sound variable
    size(700,700)
    frameRate(60)#for moving the cars
    # sf = SoundFile(this, "Wario.mp3")#our sound to be played with the game
    # sf.play()
def draw():
    global right,car1_ms, ob1_y, ob3_x, ob4_y, ob5_y, ob6_y, ob7_x, ob8_x, ob9_x, ob10_x, ob1_move, ob3_move, ob4_move, ob5_move, ob6_move, ob7_move, ob8_move, ob9_move, ob10_move  
    fill(255)
    rect(0,0,700,700)#Boundary rect for collisions
    fill(0)
    rect(52,40,600,620) #road
    rect(294,40,25,115) #boundary for anti cheat mechanism
    fill(0,255,0)
    rect(182,155,350,400)#middle part
    fill(0)
    textSize(25)
    text("Welcome to Dashkart",225,342)
    for count in range(94,575,50):#every count creates road lines
        fill(255,255,0)
        rect(count, 604, 30, 10)
    for count1 in range(108,568,50):
        fill(255,255,0)
        rect(count1, 94, 30, 10)
    for count2 in range(94,620,50):
        fill(255,255,0)
        rect(585, count2, 10, 30)
    for count3 in range(110,601,50):
        fill(255,255,0)
        rect(109, count3, 10, 30)
    fill(0)
    rect(300,90,40,30)#covers up road lines at finish
    rect(359,94,40,30)#covers up road lines at finish
    fill(255,165,0)
    rect(ob1_x,ob1_y, 20, 20)#any rect with "ob" contains obstacle coords
    fill(75,0,130)
    rect(ob2_x, ob2_y, 55, 55)
    fill(165,42,42)
    rect(ob3_x, ob3_y, 50, 20)
    fill(219,112,147)
    rect(ob4_x, ob4_y, 20, 20)
    fill(219,112,147)
    rect(ob5_x, ob5_y, 20, 20)
    fill(219,112,147)
    rect(ob6_x, ob6_y, 20, 20)
    fill(77,109,109)
    rect(ob7_x, ob7_y, 50, 20)
    fill(77,109,109)
    rect(ob8_x, ob8_y, 50, 20)
    fill(77,109,109)
    rect(ob9_x, ob9_y, 50, 20)
    fill(77,109,109)
    rect(ob10_x, ob10_y, 50, 20)
    fill(220,20,60)
    rect(130, 206, 40, 50)
    fill(255,255,0)
    triangle(135, 210, 165, 210, 150, 250)
    fill(220,20,60)
    rect(220, 580, 50, 40)
    fill(255,255,0)
    triangle(225, 585, 225, 615, 265, 600) 
    fill(220,20,60)
    rect(454, 51, 50, 40)
    fill(255,255,0)
    triangle(499, 56, 499, 86, 459, 71)#for speed
    for checker in range(321,365,15):#creates finish line
        for checker1 in range(40,155,20):
            fill(255)
            rect(checker,checker1,10,10)
    fill(255,0,0)#red car
    rect(car1_x,car1_y,car1_width,car1_height)
    fill(135,206,235)#blue car
    rect(car2_x,car2_y,car2_width,car2_height)
    fill(255,0,0)
    move1()#reference (function name) to see comments
    move2()
    isCollision()
    score()
    lap1()
    lap2()
    fill(255,0,0)#score system
    textSize(20)
    text("Lap:"+str(lap_1), 34,680)
    fill(125,150,255)
    textSize(20)
    text("Lap:"+str(lap_2), 552,680)
    ob1_y += ob1_move#obstacle movement
    if ob1_y < 38 or ob1_y + 20 > 158:
        ob1_move *= -1
    ob3_x += ob3_move
    if ob3_x < 51 or ob3_x + 50 > 182:
        ob3_move *= -1
    ob4_y += ob4_move
    if ob4_y < 554 or ob4_y + 20 > 660:
        ob4_move *= -1
    ob5_y += ob5_move
    if ob5_y < 554 or ob5_y + 20 > 660:
        ob5_move *= -1
    ob6_y += ob6_move
    if ob6_y < 554 or ob6_y + 20 > 660:
        ob6_move *= -1
    ob7_x += ob7_move
    if ob7_x < 532 or ob7_x + 50 > 653:
        ob7_move *= -1
    ob8_x += ob8_move
    if ob8_x < 532 or ob8_x + 50 > 653:
        ob8_move *= -1
    ob9_x += ob9_move
    if ob9_x < 532 or ob9_x + 50 > 653:
        ob9_move *= -1
    ob10_x += ob10_move
    if ob10_x < 532 or ob10_x + 50 > 653:
        ob10_move *= -1
    game_over()
    print(mouseX,mouseY)
def keyPressed():#if keys are pressed
    global leftarr,rightarr,uparr,downarr
    global up,down,left,right
    if key=='w':
        up=True#sets bool up from false to true
    elif key=='a':
        left=True
    elif key=='s':
        down=True
    elif key=='d':
        right=True
    if key==CODED:
        if keyCode==UP:
            uparr=True
        elif keyCode==LEFT:
            leftarr=True
        elif keyCode==DOWN:
            downarr=True
        elif keyCode==RIGHT:
            rightarr=True

def keyReleased(): #makes the cars not move infinitely
    global up,down,left,right,uparr,downarr,leftarr,rightarr
    if key=='w':
        up=False
    elif key=='a':
        left=False
    elif key=='s':
        down=False
    elif key=='d':
        right=False
    if key==CODED:
        if keyCode==UP:
            uparr=False
        elif keyCode==LEFT:
            leftarr=False
        elif keyCode==DOWN:
            downarr=False
        elif keyCode==RIGHT:
            rightarr=False

def move1(): #allows for movement of red car without interference with the keyboard
    global car1_x,car1_y,car1_move,right
    if up==True:
        car1_y-=car1_move
    if down==True:
        car1_y+=car1_move
    if left==True:
        car1_x-=car1_move
    
    if right==True and car1_y>=0 and car1_y<=557 and car1_x<318 and car1_x>273:
        right=False
    elif right==True:
        car1_x+=car1_move
    
    
def move2():#allows for movement of blue car without interference from the keyboard
    global car2_x,car2_y,car2_move,rightarr
    if uparr==True:
        car2_y-=car2_move
    if downarr==True:
        car2_y+=car2_move
    if leftarr==True:
        car2_x-=car2_move
    if rightarr==True and car2_y>=0 and car2_y<=557 and car2_x<318 and car2_x>273:
        rightarr=False
    elif rightarr==True:
        car2_x+=car2_move
        
def isCollision(): #collision for everything
    global ob2_x, ob2_y, ob1_x, ob1_y, car1_height, car1_width, car1_x, car1_y, car1_move, car2_move, barrier_x, barrier_y, barrier_width, barrier_height, car2_height, car2_width, car2_x, car2_y
    if ((car1_x < 52) or (car1_x + car1_width > 652) or (car1_y < 40) or (car1_y + car1_height > 660)):
        car1_move = 0.5
    elif ((car1_x + 20 > 182) and (car1_y > 155) and (car1_x < 532) and (car1_y < 555)):
        car1_move = 0.5
    elif ((car1_x > 268) and (car1_y > 46) and (car1_x < 270) and (car1_y < 120)):
        car1_move = 0.5
    else:
        car1_move = 3
    if ((car2_x < 52) or (car2_x + car2_width > 652) or (car2_y < 40) or (car2_y + car2_height > 660)):
        car2_move = 0.5
    elif ((car2_x + 20 > 182) and (car2_y > 155) and (car2_x < 532) and (car2_y < 555)):
        car2_move = 0.5
    else:
        car2_move = 3            
    
    #obstacles
    #ob1 (orange near finish line)
    if ((car2_x < ob1_x + 20) and (car2_x > ob1_x) and (((car2_y < ob1_y + 20) and (car2_y > ob1_y)) or ((car2_y + 20 > ob1_y) and (car2_y +20 < ob1_y + 20)))):
        car2_x=244
        car2_y=119
    if ((car1_x < ob1_x + 20) and (car1_x > ob1_x) and (((car1_y < ob1_y + 20) and (car1_y > ob1_y)) or ((car1_y + 20 > ob1_y) and (car1_y +20 < ob1_y + 20)))):
        car1_x = 245
        car1_y = 64
    #ob2 (purple rectangle sludge (to remain in place))
    if ((car1_y + 20 > ob2_y) and (car1_y < ob2_y + 55) and (car1_x + 20 > ob2_x) and (car1_x < ob2_x + 55)):
        car1_move = 0.5
    if ((car2_y + 20 > ob2_y) and (car2_y < ob2_y + 55) and (car2_x + 20 > ob2_x) and (car2_x < ob2_x + 55)):
        car2_move = 0.5
    #ob3 (brown rectangle (moving))
    if ((car1_y + 20 > ob3_y) and (car1_y < ob3_y + 20) and (car1_x + 20 > ob3_x) and (car1_x < ob3_x + 50)):
        car1_x = 110
        car1_y = 430
    if ((car2_y + 20 > ob3_y) and (car2_y < ob3_y + 20) and (car2_x + 20 > ob3_x) and (car2_x < ob3_x + 50)):
        car2_x = 110
        car2_y = 430
    #ob4 (left pink square (moving))
    if ((car1_x + 20 > ob4_x) and (car1_x < ob4_x + 20) and (car1_y + 20 > ob4_y) and (car1_y < ob4_y + 20)):
        car1_move = 0.5
    if ((car2_x + 20 > ob4_x) and (car2_x < ob4_x + 20) and (car2_y + 20 > ob4_y) and (car2_y < ob4_y + 20)):
        car2_move = 0.5
    #ob5 (middle pink square (moving))
    if ((car1_x + 20 > ob5_x) and (car1_x < ob5_x + 20) and (car1_y + 20 > ob5_y) and (car1_y < ob5_y + 20)):
        car1_move = 0.5
    if ((car2_x + 20 > ob5_x) and (car2_x < ob5_x + 20) and (car2_y + 20 > ob5_y) and (car2_y < ob5_y + 20)):
        car2_move = 0.5
    #ob6 (right pink square (moving))
    if ((car1_x + 20 > ob6_x) and (car1_x < ob6_x + 20) and (car1_y + 20 > ob6_y) and (car1_y < ob6_y + 20)):
        car1_move = 0.5
    if ((car2_x + 20 > ob6_x) and (car2_x < ob6_x + 20) and (car2_y + 20 > ob6_y) and (car2_y < ob6_y + 20)):
        car2_move = 0.5
    #ob7 (bottom gray rectangle (moving))
    if ((car1_y + 20 > ob7_y) and (car1_y < ob7_y + 20) and (car1_x + 20 > ob7_x) and (car1_x < ob7_x + 50)):
        car1_x = 576
        car1_y = 567
    if ((car2_y + 20 > ob7_y) and (car2_y < ob7_y + 20) and (car2_x + 20 > ob7_x) and (car2_x < ob7_x + 50)):
        car2_x = 576
        car2_y = 567
    #ob8 (2nd bottom gray rectangle (moving))
    if ((car1_y + 20 > ob8_y) and (car1_y < ob8_y + 20) and (car1_x + 20 > ob8_x) and (car1_x < ob8_x + 50)):
        car1_x = 576
        car1_y = 475
    if ((car2_y + 20 > ob8_y) and (car2_y < ob8_y + 20) and (car2_x + 20 > ob8_x) and (car2_x < ob8_x + 50)):
        car2_x = 576
        car2_y = 475
    #ob9 (2nd top gray rectangle (moving))
    if ((car1_y + 20 > ob9_y) and (car1_y < ob9_y + 20) and (car1_x + 20 > ob9_x) and (car1_x < ob9_x + 50)):
        car1_x = 576
        car1_y = 390
    if ((car2_y + 20 > ob9_y) and (car2_y < ob9_y + 20) and (car2_x + 20 > ob9_x) and (car2_x < ob9_x + 50)):
        car2_x = 576
        car2_y = 390
    #ob10 (top gray rectangle (moving))
    if ((car1_y + 20 > ob10_y) and (car1_y < ob10_y + 20) and (car1_x + 20 > ob10_x) and (car1_x < ob10_x + 50)):
        car1_x = 576
        car1_y = 330
    if ((car2_y + 20 > ob10_y) and (car2_y < ob10_y + 20) and (car2_x + 20 > ob10_x) and (car2_x < ob10_x + 50)):
        car2_x = 576
        car2_y = 330        
                
    #speed up zones
    #speed zone 1 (just before purple sludge)
    if ((car1_y + 20 > 206) and (car1_y < 256) and (car1_x + 20 > 130) and (car1_x < 170)):
        car1_move = 10
    if ((car2_y + 20 > 206) and (car2_y < 256) and (car2_x + 20 > 130) and (car2_x < 170)):
        car2_move = 10
    #speed zone 2 (just before pink squares)
    if ((car1_x + 20 > 220) and (car1_x < 270) and (car1_y + 20 > 580) and (car1_y < 620)):
        car1_move = 10
    if ((car2_x + 20 > 220) and (car2_x < 270) and (car2_y + 20 > 580) and (car2_y < 620)):
        car2_move = 10    
    #speed zone 3 (just before orange square)(474, 51, 50, 40)
    if ((car1_x + 20 > 454) and (car1_x < 507) and (car1_y + 20 > 51) and (car1_y < 91)):
        car1_move = 10
    if ((car2_x + 20 > 454) and (car2_x < 507) and (car2_y + 20 > 51) and (car2_y < 91)):
        car2_move = 10    
    
def score(): #adds score
    global score1,score2
    if ((car1_x == 320) and (car1_y>40) and (car1_y<160)):
        score1=True
    elif ((car1_x == 321) and (car1_y>40) and (car1_y<160)):
        score1=True
    elif ((car1_x == 319) and (car1_y>40) and (car1_y<160)):
        score1=True
    else:
        score1=False
    if ((car2_x == 320) and (car2_y>40) and (car2_y<160)):
        score2=True
    elif ((car2_x == 321) and (car2_y>40) and (car2_y<160)):
        score2=True
    elif ((car2_x == 319) and (car2_y>40) and (car2_y<160)):
        score2=True
    else:
        score2=False
        
def lap1(): #score display for red car
    global lap_1
    if score1==True:
        lap_1+=1
def lap2(): #score display for blue car
    global lap_2
    if score2==True:
        lap_2+=1
def game_over(): #after 5 laps, game ends
    global lap_1
    if lap_1>=5 or lap_2>=5:
        fill(255)
        rect(0,0,width,height)
        if lap_1>=5:
            fill(255,0,0)
            textSize(32)
            text("You Won!",274,324)
            fill(135,206,235)
            textSize(32)
            text("Better Luck next time!",183,430)
        if lap_2>=5:
            fill(255,0,0)
            textSize(32)
            text("Better luck next time!",183,430)
            fill(135,206,235)
            textSize(32)
            text("You Won!",274,324)

    


   
        
