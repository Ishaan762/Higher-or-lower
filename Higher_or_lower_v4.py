from tkinter import *
from tkinter.ttk import *
from PIL import *
import random
import os
from playsound import playsound
class Game(object):
    def __init__(self,root):
        self.c=0
        self.root=root
        self.canvas=Canvas(self.root,width=150,height=200)
        self.canvas.place(x=150,y=150,anchor=NW)
        self.btn=PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + "\Cards\hbtn.png")
        self.Btn=PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + "\Cards\lbtn.png")

        self.i_label = Label(image=self.btn)
        self.I_label=Label(image=self.Btn)
        self.c2=Canvas(self.root,width=150,height=200)
        self.c2.place(x=300,y=150,anchor=NW)
        self.img2=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"\\Cards\\back.png")
        self.imgoncanvas2=self.c2.create_image(20,20,anchor=NW,image=self.img2)

        self.highb = Button(root,image=self.btn, command=self.onclickhighb)
        self.lowb = Button(root,image=self.Btn, command=self.onclicklowb)
        self.highb.place(x=150,y=500, anchor=CENTER)
        self.lowb.place(x=450,y=500, anchor=CENTER)

        self.life=5
        self.score=0
        self.life_and_score=Label(root,text="Life: "+str(self.life)+" Score: "+str(self.score))
        self.life_and_score.place(x=300,y=400,anchor=CENTER)

        self.msglabel=Label(root,text="")
        self.msglabel.place(x=300,y=450,anchor=CENTER)

        self.value=""

        self.cards_in_deck={"sa":1,"s2":2,"s3":3,"s4":4,"s5":5,"s6":6,"s7":7,"s8":8,"s9":9,"s10":10,"sj":11,"sq":12,"sk":13,
        "ha":1,"h2":2,"h3":3,"h4":4,"h5":5,"h6":6,"h7":7,"h8":8,"h9":9,"h10":10,"hj":11,"hq":12,"hk":13,
        "ca":1,"c2":2,"c3":3,"c4":4,"c5":5,"c6":6,"c7":7,"c8":8,"c9":9,"c10":10,"cj":11,"cq":12,"ck":13 ,
        "da":1,"d2":2,"d3":3,"d4":4,"d5":5,"d6":6,"d7":7,"d8":8,"d9":9,"d10":10,"dj":11,"dq":12,"dk":13}
        self.cards_in_stack={}
        self.curr_card=random.choice(list(self.cards_in_deck.keys()))
        self.cards_in_stack.update({self.curr_card:self.cards_in_deck[self.curr_card]})
        self.cards_in_deck.pop(self.curr_card)
        self.rand_card=random.choice(list(self.cards_in_deck.keys()))
        self.img=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"\\Cards\\"+self.curr_card+".png")
        self.imgoncanvas=self.canvas.create_image(20,20,anchor=NW,image=self.img)

    def updatemsglabel(self,msg):
        self.msglabel["text"]=msg

    def updatecard(self,card):
        global url
        url=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"\\Cards\\"+card+".png")
        self.canvas.itemconfig(self.imgoncanvas,image=url)

    def updatescoreandlife(self,score):
        self.life_and_score["text"]="Life: "+str(self.life)+" Score: "+str(score)

    def onclickhighb(self):
        if self.ishigher():
            self.correct()
        else:
            self.wrong()

    def onclicklowb(self):
        if self.islower():
            self.correct()
        else:
            self.wrong()

    def correct(self):
        self.c+=1
        self.freeze()
        if self.c==1:
            playsound("E:\\S1.mp3")
        elif self.c==2:
            playsound("E:\\S2.mp3")
        elif self.c==3:
            playsound("E:\\S3.mp3")
        elif self.c==4:
            playsound("E:\\S4.mp3")
        elif self.c==5:
            playsound("E:\\S5.mp3")
        elif self.c==6:
            playsound("E:\\S6.mp3")
        elif self.c==7:
            playsound("E:\\S7.mp3")
        elif self.c==8:
            playsound("E:\\S8.mp3")
        elif self.c==9:
            playsound("E:\\S9.mp3")
        elif self.c>=10:
            playsound("E:\\S10.mp3")
        else:
            None
        self.updatemsglabel("You are correct!")
        self.score+=1
        self.updatescoreandlife(self.score)
        if len(self.cards_in_deck)==0:
            self.revealcard(self.rand_card)
            self.end()
        else:
            self.revealcard(self.rand_card)
            self.root.after(2000,self.next)
            self.root.after(2000,self.go)
            if self.score%5==0 and self.score!=5:
                def exchange_it():
                    self.score-=10
                    self.life+=1
                    self.updatescoreandlife(self.score)    
                    exchange.destroy()
                def No_exchange():
                    exchange.destroy()
                
                exchange=Tk()
                exchange.title('DEAL WITH THE DEVIL')
                exchange_instructions=f'''You have {self.score} number of cards
Do you want to exchange 10 cards from your stack to gain 1 life??'''

                exchange_label=Label(exchange,compound =CENTER,text=exchange_instructions,font='Arial 15')
                exchange_label.pack()
                yes=Button(exchange,text='Yes',command=exchange_it)
                yes.pack()
                no=Button(exchange,text='No',command=No_exchange)
                no.pack()

    def wrong(self):
        self.c=0
        self.freeze()
        playsound("E:\\Failure.mp3")
        self.updatemsglabel("You are wrong!")
        self.life-=1
        self.updatescoreandlife(self.score)
        if self.life==0:            
            self.revealcard(self.rand_card)
            self.end()
        else:
            self.revealcard(self.rand_card)
            self.root.after(2000,self.next)
            self.root.after(2000,self.go)

    def initialize(self):
        self.curr_card=self.rand_card
        self.cards_in_stack.update({self.curr_card:self.cards_in_deck[self.curr_card]})
        self.cards_in_deck.pop(self.curr_card)
        self.rand_card=random.choice(list(self.cards_in_deck.keys()))

    def ishigher(self):
        if self.cards_in_stack[self.curr_card]<self.cards_in_deck[self.rand_card]:
            return True
        elif self.cards_in_stack[self.curr_card]>self.cards_in_deck[self.rand_card]:
            return False
        else:
            return True
    def islower(self):
        if self.cards_in_stack[self.curr_card]>self.cards_in_deck[self.rand_card]:
            return True
        elif self.cards_in_stack[self.curr_card]<self.cards_in_deck[self.rand_card]:
            return False
        else:
            return True
    
    def go(self):
        self.highb["state"]=ACTIVE
        self.lowb["state"]=ACTIVE
    
    def freeze(self):
        self.highb["state"]=DISABLED
        self.lowb["state"]=DISABLED
        

    def end(self):
        self.highb["state"]=DISABLED
        self.lowb["state"]=DISABLED
        playsound("E:\mixkit-arcade-retro-game-over-213.wav")
        if self.life==0:
            self.updatemsglabel("Better luck next time! Your score was "+str(self.score))# Display lose msg to frontend
        else:
            self.updatemsglabel("Congratulations, you won!")# Display win msg to frontend

    def revealcard(self,card):
        global url2
        url2=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"\\Cards\\"+card+".png")
        self.c2.itemconfig(self.imgoncanvas2,image=url2)

    def next(self):
        global url2
        self.updatemsglabel("")
        url2=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"\\Cards\\back.png")
        self.c2.itemconfig(self.imgoncanvas2,image=url2)
        self.initialize()
        self.updatecard(self.curr_card)

root=Tk()
root.title("Higher or Lower")
root.geometry("600x600")
def redirect():
    t1=Toplevel(root)
    t1.geometry('900x250')
    t1.title("Welcome to the Game")
    rno='''                                  
                                               Instructions
    1.The card on the left symbolizes the current card
    2.The card on the right symbolizes the next card
    3.You need to guess whether the next card will be higher or lower than present card
    4.If next card is same as previous you get bonus point
    4.Correct guess gives you a point
    5.Wrong guess leads to loss of 1 life
                                                Good Luck!'''
    lb1=Label(t1,compound =CENTER,text=rno,font='Arial 15')
    lb1.pack()
    okay=Button(t1,text='OKAY',command=t1.destroy)
    okay.pack()
obj=Game(root)
instructions=Button(root,text='INSTRUCTIONS',command=redirect)
instructions.place(x=600,y=0,anchor=NE)
root.mainloop()  