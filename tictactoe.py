from Tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
from random import randint

class main:
   
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.label=Label(self.frame, text='Tic Tac Toe Game', height=6, bg='black', fg='blue')
        self.label.pack(fill="both", expand=True)
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        self.Start1=Button(self.frameb, text='Click here to start\ndouble player', height=4, command=self.start1,bg='white', fg='purple')
        self.Start1.pack(fill="both", expand=True, side=RIGHT)
        self.Start2=Button(self.frameb, text='Click here to start\nsingle player', height=4, command=self.start2,bg='purple', fg='white')
        self.Start2.pack(fill="both", expand=True, side=LEFT)     
        self._board()

    def start1(self):
        self.canvas.delete(ALL)
        self.label['text']=('Tic Tac Toe Game')
        self.canvas.bind("<ButtonPress-1>", self.sgplayer)  
        self._board()
        self.TTT=[[0,0,0],[0,0,0],[0,0,0]]
        self.i=0
        self.j=False

    def start2(self):
        self.canvas.delete(ALL)
        self.label['text']=('Tic Tac Toe Game')
        self.canvas.bind("<ButtonPress-1>", self.dgplayer)  
        self._board()
        self.TTT=[[0,0,0],[0,0,0],[0,0,0]]
        self.i=0
        self.j=False
        self.trigger=False

    def end(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.j=True
        
    
    def _board(self):
        self.canvas.create_rectangle(0,0,300,300, outline="black")
        self.canvas.create_rectangle(100,300,200,0, outline="black")
        self.canvas.create_rectangle(0,100,300,200, outline="black")
        
    def sgplayer(self,event):
        for k in range(0,300,100):
            for j in range(0,300,100):
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    if self.canvas.find_enclosed(k,j,k+100,j+100)==():
                        if self.i%2==0:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="black")
                            self.TTT[Y1][X1]+=1
                            self.i+=1
                        else:                         
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="black")
                            self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="black")
                            self.TTT[Y1][X1]+=9
                            self.i+=1
        self.check()

    def dgplayer(self,event):
        for k in range(0,300,100):
            for j in range(0,300,100):
                if self.i%2==0:
                    if event.x in range(k,k+100) and event.y in range(j,j+100):
                        if self.canvas.find_enclosed(k,j,k+100,j+100)==():
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="black")
                            self.TTT[Y1][X1]+=1
                            self.i+=1
                            self.check()
                            self.trigger=False                           
                else:
                    print(self.i)
                    self.check()
                    print("checked")
                    self.AIcheck()
                    print("AIchecked")
                    self.trigger=False
                    
                    

                        
                        
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
