from Tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
from board import Board
from player import Player
import math

class main:
   
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.label=Label(self.frame, text="Master Yunrui's Gomoku Game", height=6, bg='black', fg='pink')
        self.label.pack(fill="both", expand=True)
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        self.Start1=Button(self.frameb, text='Click here to start\n may the plump be with you...', height=4, command=self.start1,bg='white', fg='purple')
        self.Start1.pack(fill="both", expand=True, side=RIGHT)
        self._board()

    def start1(self):
        self.canvas.delete(ALL)
        self.canvas.bind("<ButtonPress-1>", self.multiplayer)  
        self._board()
        self.board=Board() 
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.turn = 1
        self.j=False
        self.Start1['text']=("Click To Restart")


    def end(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.j=True
        
    
    def _board(self):
        for i in xrange(0,300,20):
            self.canvas.create_line(i,0,i,300)

        for j in xrange(0,300,20):
            self.canvas.create_line(0,j,300,j)
    
    def distance(self,x1,y1,x2,y2):
        return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))


        
    def multiplayer(self,event):

        x = event.x
        y = event.y
        for j in range(0,300,20):
            for i in range(0,300,20):
                if (self.distance(x,y,i,j)<5):
                    if self.turn==1:
                        print("click",i,j)
                        self.canvas.create_oval( i+5, j+5, i-5, j-5, width=2, outline="black")
                        self.player1.move(self.board,i/20,j/20)
                        self.turn=2
                        if self.player1.win(self.board,i/20,j/20):
                            self.label['text']=('Play 1 Wins')

                            print("Player 1 wins")
                            self.end()
                    else:
                        print("click",i,j)
                        self.canvas.create_oval( i+5, j+5, i-5, j-5, width=2, outline="pink")
                        self.player2.move(self.board,i/20,j/20)
                        self.turn=1
                        if self.player2.win(self.board,i/20,j/20):
                            self.label['text']=('Play 2 Wins')
                            print("Player 2 wins")
                            self.end()
        
        print(x,y,self.canvas.find_closest(x,y)[0])

    def check(self):
        #horizontal check
        for i in range(0,3):
            if sum(self.TTT[i])==27:
                self.label['text']=('2nd player wins!')
                self.end()
            if sum(self.TTT[i])==3:
                self.label['text']=('1st player wins!')
                self.end()
        #vertical check
        #the matrix below transposes self.TTT so that it could use the sum fucntion again
        self.ttt=[[row[i] for row in self.TTT] for i in range(3)]
        for i in range(0,3):            
            if sum(self.ttt[i])==27:
                self.label['text']=('2nd player wins!')
                self.end()
            if sum(self.ttt[i])==3:
                self.label['text']=('1st player wins!')
                self.end()
        #check for diagonal wins
        if self.TTT[1][1]==9:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('2nd player wins!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('2nd player wins!')
                self.end()
        if self.TTT[1][1]==1:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('1st player wins!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('1st player wins!')
                self.end()
        #check for draws
        if self.j==False:
            a=0
            for i in range(0,3):
                a+= sum(self.TTT[i])
            if a==41:
                self.label['text']=("It's a pass!")
                self.end()

                
    def AIcheck(self):
        #This is built on the self.check function
        self.ttt=[[row[i] for row in self.TTT] for i in range(3)]
        #DEFENSE
        #this is the horizontal checklist    
        for h in range(0,3): 
            k=0
            j=0            
            if sum(self.TTT[h])==2:
                while k <3:
                    if k==h:
                        while j <3:
                            if self.trigger==False:
                                if self.TTT[k][j]==0:
                                    self.cross(j,k)
                                    break
                            j+=1
                    k+=1
        #this is the vertical checklist
        for h in range(0,3):
            k=0
            j=0
            if sum(self.ttt[h])==2:                        
                while k <3:
                    if k==h:
                        while j <3:
                            if self.trigger==False:
                                if self.ttt[k][j]==0:
                                    self.cross(k,j)
                                    break
                            j+=1
                    k+=1                    
        #this is the diagonal checklist
        if self.TTT[1][1]==1:
            if self.TTT[0][0]==1:
                if self.trigger==False:
                    if self.TTT[2][2]==0:
                        self.cross(2,2)
            if self.TTT[0][2]==1:
                if self.trigger==False:
                    if self.TTT[2][0]==0:
                        self.cross(0,2)
            if self.TTT[2][0]==1:
                if self.trigger==False:
                    if self.TTT[0][2]==0:
                        self.cross(2,0)
            if self.TTT[2][2]==1:
                if self.trigger==False:
                    if self.TTT[0][0]==0:
                        self.cross(0,0)
                        
        if self.TTT[1][1]==0:
            if self.trigger==False:
                self.cross(1,1)
                self.trigger=True
        else:
            if self.trigger==False:
                self.randmove()

    def cross(self, k, j):
        # k is the x coords
        # j is the y coords
        X=(200*k+100)/2
        Y=(200*j+100)/2
        X1=int(k)
        Y1=int(j)
        self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="black")
        self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="black")
        self.TTT[Y1][X1]+=9
        self.check()
        self.i+=1
        self.trigger=True
         

    def randmove(self):
        while True:
            k=(randint(0,2))
            j=(randint(0,2))
            if self.TTT[j][k]==0:
                X=(200*k+100)/2
                Y=(200*j+100)/2
                self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="black")
                self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="black")
                self.TTT[j][k]+=9
                self.check()
                self.i+=1
                self.trigger=True
                break
            else:
                k=(randint(0,2))*100
                j=(randint(0,2))*100
                
root=Tk()
app=main(root)
root.mainloop()
