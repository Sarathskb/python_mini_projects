from tkinter import *
import random
wd=Tk()
wd.title("Dice_Game")
wd.geometry('550x570')
a=Frame(wd,bg='black',height=550,width=490)
a.pack(side=TOP)


pc_info=[1,2,3,4,5,6]


l5=Label(a,text='')

    
a1=StringVar()

a2=StringVar()

a3=StringVar()

score=0
score1=0

def play1():
    global score
    roll=random.choice(pc_info)
    if roll==1:
       
        l5.config(text="Player1 OUT")
        l5.place(x=170,y=180,width=105)
        b2.configure(state=ACTIVE)
        b1.configure(state=DISABLED)
        restart.configure(state=DISABLED)
        a1.set(score)
        
        
    else:
        score=score+roll
        l5.config(text=roll)
        l5.place(x=190,y=180,width=34,height=35)
        a1.set(score)
        e1=Entry(a,text=a1,font=('times',15))
        e1.place(x=220,y=140,width=64,height=35)

def play2():
    global score1
    roll=random.choice(pc_info)
    if roll==1:
        l5.config(text="player2 OUT")
        l5.place(x=170,y=180,width=105)
        b2.configure(state=DISABLED)
        b1.configure(state=DISABLED)
        restart.configure(state=ACTIVE)
        a2.set(score1)
        if(score1>score):
            l8.configure(text="Player 2 Win")

            
            g=max(score1,score)
            a3.set(g)
           
            
        else:
            
            l8.configure(text="Player 1 Win")
           
            
            g=max(score1,score)
            a3.set(g)
            
        
       

        
    else:
        score1=score1+roll
        l5.config(text=roll)
        l5.place(x=190,y=180,width=34,height=35)
        a2.set(score1)
        e1=Entry(a,text=a2,font=('times',15))
        e1.place(x=220,y=140,width=64,height=35)






p=''
def restart():
    global score1,score,p
    b1.configure(state=ACTIVE)
    score=0
    score1=0
    p=''
    a3.set(p)
 
    a2.set(score)
    a1.set(score1)
    l5.config(text=p)
    l8.config(text=p)
    
    
    
    


#scoreboard
l6=Label(a,text="player1 score")
l6.place(x=40,y=160)

e2=Entry(a,text=a1)
e2.place(x=40,y=190,width=44,height=35)


l7=Label(a,text="player2 score")
l7.place(x=350,y=160)

e3=Entry(a,text=a2)
e3.place(x=350,y=190,width=44,height=35)


l9=Label(a,text="HIGH SCORE",font=('times',9,'bold'))
l9.place(x=120,y=300,width=110,height=35)


e4=Entry(a,text=a3,fg='green',font=('times',25,'bold'))
e4.place(x=240,y=300,width=60,height=35)
#creater name label
s=Label(a,text=" Ceated By SKB ",bg="gray",fg="red",font=('times',14,'bold'))
s.place(x=10,y=520,width=470,height=20)

#labels
l10=Label(a,text=" DICE ROLL GAME ",bg="red",font=('times',14,'bold'),fg='white')
l10.place(x=140,y=10,width=190)
l1=Label(a,text="player 1",font=('times',14,'bold'))
l1.place(x=40,y=80,width=105,height=35)


l2=Label(a,text="vs",font=('times',14,'bold'))
l2.place(x=230,y=80,width=60,height=35)


l3=Label(a,text="player 2",font=('times',14,'bold'))
l3.place(x=350,y=80,width=105,height=35)

l4=Label(a,text='SCORE')
l4.place(x=150,y=140,width=64,height=35)

l8=Label(a,text=" ",bg="green",fg="red",font=('times',14,'bold'))
l8.place(x=150, y=240,width=115,height=35)

#button

b1=Button(a,text='Roll player1',command=play1,state=ACTIVE)
b1.place(x=40,y=420,width=80,height=35)


b2=Button(a,text='Roll player2',command=play2,state=DISABLED)
b2.place(x=390,y=420,width=80,height=35)

restart=Button(a,text='Restart',command=restart,state=DISABLED,bg='red',font=('times',14,'bold'))
restart.place(x=190,y=420,width=80,height=35)

wd.mainloop()
