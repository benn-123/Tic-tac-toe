turn = 1 #Whether it's player 1 or 2's turn

board = [ [0,0,0], [0,0,0], [0,0,0] ] #Empty board at the start

mode = "title-screen" # used to switch between game modes

score1 = 0 #Player 1 score

score2 = 0 #Player 2 score

def setup():
    size(600,600)
    
def draw():
    global mode, counter, score1, score2
    
    if mode == "title-screen":
        background(255,255,255)
        #Tic tac toe title
        fill(0,0,0)
        textSize(60)
        text("TIC TAC TOE",119,90)
        
        #Instructions
        fill(255,255,255)
        rect(50,150,500,200)
        fill(0,0,0)
        textSize(25)
        text("INSTRUCTIONS",200,175)
        textSize(20)
        text("1. Player 1 goes first",50,210)
        text("2. Player 2 goes second",50,235)
        text("3. Keep alternating until one of the players has",50,260)
        text("    drawn a row of 3 symbols or nobody can move",50,282)
        textSize(23)
        text("Player 1 = X      Player 2 = X", 140,310)
        text("    Click r to restart",180,340)
        
        #start button
        fill(25,163,203)
        rect(200,400,200,150)
        fill(0,0,0)
        textSize(50)
        text("Start",240,490)
    
    if mode == "game-over1": #If player 1 wins
        background(255,255,255)
        fill(0,0,0)
        textSize(80)
        text("Game Over", 100,200)
        textSize(50)
        text("Player 1 wins!!!",130,350)
        text("Click r to restart",110,500)
        textSize(25)
        text(" Player 1 score:", 40,420) #Display scores
        text(score1/71,225,420)
        text(" Player 2 score:", 340,420)
        text(score2,525,420)
        
    if mode == "game-over2": #If player 2 wins
        background(255,255,255)
        fill(0,0,0)
        textSize(80)
        text("Game Over", 100,200)
        textSize(50)
        text("Player 2 wins!!!",130,350)
        text("Click r to restart",110,500)
        textSize(25)
        text(" Player 1 score:", 40,420)
        text(score1/71,225,420)
        text(" Player 2 score:", 340,420)
        text(score2,525,420)
        
    if mode == "game-over3": #If there is a tie
        background(255,255,255)
        fill(0,0,0)
        textSize(80)
        text("Game Over", 100,200)
        textSize(50)
        text("Tie game :(",170,350)
        text("Click r to restart",110,500)
        textSize(25)
        text(" Player 1 score:", 40,420)
        text(score1/71,225,420)
        text(" Player 2 score:", 340,420)
        text(score2,525,420)
    
    #Pauses the screen for a short time to show winners 
    if mode == "pause1":
        println((frameCount, counter))
        # check if the pause is done
        if frameCount > counter + 70:
            mode = "game-over1"
            
    if mode == "pause2":
        println((frameCount, counter))
        # check if the pause is done
        if frameCount > counter + 70:
            mode = "game-over2"
    
    if mode == "pause3":
        println((frameCount, counter))
        # check if the pause is done
        if frameCount > counter + 70:
            mode = "game-over3"
    
    if mode == "game-on" or mode =="pause1" or mode == "pause 2":  
        background(255,255,255)
        #Draws the grid
        strokeWeight(5)
        line(0, 200, 600, 200)  
        line(0, 400, 600, 400) 
        line(200, 0, 200 ,600) 
        line(400, 0, 400, 600) 
        strokeWeight(1)
        
        #Draws the X's and O's
        for y in range(3):
            for x in range(3):
                strokeWeight(12)
                if board[y][x] == 2:
                    ellipse((x*200)+100,(y*200)+100,80,80)
                elif board[y][x] == 1:
                    line((x*200)+50,(y*200)+50,(x*200)+140,(y*200)+140)
                    line((x*200)+140,(y*200)+50,(x*200)+50,(y*200)+140)
                    strokeWeight(1)
    
   
        strokeWeight(1)
        #Player 1 win combinations  
        if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
            fill(0,0,0)
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line(50,100,550,100)
            score1 += 1 #Increase score
            # pause counter
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
            
        elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line(50,300,550,300)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
        
        elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line(50,500,550,500)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
        
        elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line (100,50,100,550)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
    
        elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line (300,50,300,550)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
        
        elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line (500,50,500,550)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
            
        elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line (40,40,560,560)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
            
        elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
            textSize(65)
            text("PLAYER 1 WINS!!!",50,200)
            line (560,40,40,560)
            score1 += 1 #Increase score
            if mode != "pause1":
                mode = "pause1"
                counter = frameCount
            
        #Player 2 win combinations    
        elif board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
            fill(0,0,0)
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line(50,100,550,100)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
            
        elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line(50,300,550,300)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
        
        elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line(50,500,550,500)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
        
        elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line (100,50,100,550)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
    
        elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line (300,50,300,550)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
        
        elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line (500,50,500,550)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
            
        elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line (40,40,560,560)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
            
        elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
            textSize(65)
            text("PLAYER 2 WINS!!!",50,200)
            line (560,40,40,560)
            score2 += 1 #Increase score
            if mode != "pause2":
                mode = "pause2"
                counter = frameCount
        
        #If there is a tie
        elif board[0][0] != 0 and board[0][1] != 0  and board[0][2] != 0  and board[1][0] != 0  and board[1][1] != 0  and board[1][2] != 0 and board[2][0] != 0  and board[2][1] != 0  and board[2][2] != 0:
                textSize(65)
                text("Tie Game :(",110,200)
                if mode != "pause3":
                    mode = "pause3"
                    counter = frameCount
        
        
def mousePressed():
    global mode,turn, win
    
    if mode== "title-screen": #Start button
        if (mouseX > 200 and mouseX < 400) and (mouseY > 400 and mouseY < 550):
            mode= "game-on"
    
    elif mode == "game-on":
        if board[mouseY/200][mouseX/200] == 0:
            board[mouseY/200][mouseX/200] = turn
            turn_switch()

def keyPressed():
    global mode
    #If the mode is game-on or game-over, the function will run
    if mode == "game-on" or mode == "game-over1" or mode == "game-over2" or mode == "game-over3":
        if (key == 'R' or key == 'r'): #When r is clicked, the game is restarted
            game_reset()
               
    
def turn_switch(): #Switches between player 1 and 2's turn
    global turn
    if turn== 1:
            turn=2
    elif turn== 2:
        turn= 1
            
def game_reset(): #Restarts the game
    global mode,board,turn
    board = [ [0,0,0], [0,0,0], [0,0,0] ]
    turn = 1
    mode = "game-on" #Reset to game-on screen
