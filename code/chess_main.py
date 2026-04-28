import os
import tkinter as tk
from tkinter import *


root=tk.Tk()
##root.overrideredirect(True)
##root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
#root.geometry("600x600")
frame=tk.Frame(root)
frame.pack()
frame2=tk.Frame(root,bg='grey')
frame2.pack()
root.title('chess')
string=""
label=Label(root,font=("arial",20,'roman'),text='CHESS')
label.pack()
def text():
    label['text']=string
 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "..", "images")


photows = PhotoImage(file=os.path.join(IMG_DIR, "wsainik.png"))
photobs = PhotoImage(file=os.path.join(IMG_DIR, "bsainik.png"))
photowg = PhotoImage(file=os.path.join(IMG_DIR, "wghoda.png"))
photobg = PhotoImage(file=os.path.join(IMG_DIR, "bghoda.png"))
photowu = PhotoImage(file=os.path.join(IMG_DIR, "wunth.png"))
photobu = PhotoImage(file=os.path.join(IMG_DIR, "bunth.png"))
photowh = PhotoImage(file=os.path.join(IMG_DIR, "whathi.png"))
photobh = PhotoImage(file=os.path.join(IMG_DIR, "bhathi.png"))
photowrani = PhotoImage(file=os.path.join(IMG_DIR, "wrani.png"))
photobrani = PhotoImage(file=os.path.join(IMG_DIR, "brani.png"))
photowraja = PhotoImage(file=os.path.join(IMG_DIR, "wraja.png"))
photobraja = PhotoImage(file=os.path.join(IMG_DIR, "braja.png"))
photot = PhotoImage(file=os.path.join(IMG_DIR, "transparent.png"))


bu_count=0
r1,c1,b1=0,0,0
#moves
moves=0
#photo list                     EVEN--BLACK , ODD-- WHITE
#p=[None,photows[1],photobs[2],photowg[3],photobg[4],photowu[5],photobu[6],   
#photowh[7],photobh[8],photowrani[9],photobrani[10],photowraja[11],photobraja[12]]
p=[photot,photows,photobs,photowg,photobg,photowu,photobu,photowh,photobh,photowrani,photobrani,photowraja,photobraja]
#configuration[row,col,bgc,position,photo]
t=[[[],[],[],[],[],[],[],[]],#null
   [[8,p[8]],[4,p[4]],[6,p[6]],[10,p[10]],[12,p[12]],[6,p[6]],[4,p[4]],[8,p[8]]],#1
   [[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]]],
   [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
   [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
   [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
   [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
   [[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]]],
   [[7,p[7]],[3,p[3]],[5,p[5]],[9,p[9]],[11,p[11]],[5,p[5]],[3,p[3]],[7,p[7]]]]
tprevious=()
#---------check(b[function call],row,column)
def check(b,i,j):
    global bu_count,r1,c1,b1,string,moves
    string=''
    text()
    bu_count+=1
    if bu_count%2==1:
        moves+=1
        r1=i
        c1=j
        b1=b
        print('r1==',r1,'c1--',c1)
        if b1==0:
            string='Invalid Move',r1,c1 
            text()
            print('Invalid Move 1',r1,c1)
            bu_count-=1
            moves-=1
            print('bu_count=',bu_count,'moves=',moves)
        elif moves%2==1 and b1%2==0:
            print('WHITE MOVE')
            string='WHITE MOVE'
            text()
            bu_count-=1
            moves-=1
            print('bu_count',bu_count,'moves=',moves)
        elif moves%2==0 and b1%2==1:
            print('BLACK MOVE')
            string='BLACK MOVE'
            text()
            bu_count-=1
            moves-=1
            print('bu_count',bu_count,'moves=',moves)
    else :#(bu_count%2==0)
        r2,c2=i,j
        print('r2',r2,'c2',c2)
        if (b1==1):sainik_w(r1,c1,r2,c2)
        elif(b1==2):sainik_b(r1,c1,r2,c2)
        elif(b1==3 or b1==4):ghoda(r1,c1,r2,c2)
        elif(b1==5 or b1==6):unth(r1,c1,r2,c2)
        elif(b1==7 or b1==8):
            b2=b
            hathi(r1,c1,r2,c2,b2)
        elif(b1==9 or b1==10):rani(r1,c1,r2,c2)
        elif(b1==11 or b1==12):raja(r1,c1,r2,c2)

def sainik_w(r1,c1,r2,c2):
    global bu_count,moves,string
    print(r1,c1,r2,c2)
    if r1==2 and r2==1 and c1==c2 and t[r2][c2-1][0]==0:promotion(r1,c1,r2,c2)
    elif r1==7 and (r1>r2>=r1-2) and c1==c2 and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)#hoz   2
    elif r2==r1-1 and (c2==c1+1 or c2==c1-1) and (t[r2][c2-1][0]!=0 and t[r2][c2-1][0]%2==0):exchange2(r1,c1,r2,c2)#across diagonal
    elif (r1>r2==r1-1) and c1==c2 and(t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)#hoz     1
    else:
            string='Invalid Move'
            text()
            print('Invalid Move 2',r1,c1)
            bu_count-=2
            moves-=1
            print('bu_count',bu_count,'moves',moves)
   
def sainik_b(r1,c1,r2,c2):
    global bu_count,moves,string
    if r1==7 and r2==8 and c1==c2 and t[r2][c2-1][0]==0:promotion(r1,c1,r2,c2)
    elif r1==2 and c1==c2 and (r1<r2<=r1+2)  and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)#hoz
    elif r2==r1+1 and (c2==c1-1 or c2==c1+1) and (t[r2][c2-1][0]!=0 and t[r2][c2-1][0]%2==1):exchange2(r1,c1,r2,c2)#across diagonal
    elif r1<r2==r1+1 and c1==c2 and t[r2][c2-1][0]==0 :exchange(r1,c1,r2,c2)#hoz
    else:
        string='Invalid Move',r1,c1
        text()
        print('Invalid Move 3')
        bu_count-=2
        moves-=1
        print('bu_count',bu_count,'moves',moves)
def promotion(r1,c1,r2,c2):
    print('')
    
def ghoda(r1,c1,r2,c2):
    global bu_count,moves,b1,string
    if b1%2==0:#black
        if r2==r1-2 and (c2==c1+1 or c2==c1-1) and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1-1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1+1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1+2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1-2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]%2==1):exchange2(r1,c1,r2,c2)
        elif r2==r1-1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]%2==1):exchange2(r1,c1,r2,c2)
        elif r2==r1+1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]%2==1):exchange2(r1,c1,r2,c2)
        elif r2==r1+2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]%2==1):exchange2(r1,c1,r2,c2)
        else:
            string='Invalid Move',r1,c1
            text()
            print('Invalid Move 4',r1,c1)
            bu_count-=2
            moves-=1
            print('bu_count',bu_count,'moves',moves)
    elif b1%2==1:#white
        if r2==r1-2 and (c2==c1+1 or c2==c1-1) and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1-1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1+1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1+2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]==0):exchange(r1,c1,r2,c2)
        elif r2==r1-2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]%2==0):exchange2(r1,c1,r2,c2)
        elif r2==r1-1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]%2==0):exchange2(r1,c1,r2,c2)
        elif r2==r1+1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]%2==0):exchange2(r1,c1,r2,c2)
        elif r2==r1+2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]%2==0):exchange2(r1,c1,r2,c2)
        else:
            string='Invalid Move',r1,c1
            text()
            print('Invalid Move 5',r1,c1)
            bu_count-=2
            moves-=1
            print('bu_count',bu_count,'moves',moves) 
##    if (r2==r1-2 and (c2==c1+1 or c2==c1-1) and (t[r2][c2-1][0]==0)) or (r2==r1-1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]==0)) or(r2==r1+1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]==0)) or(r2==r1+2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]==0)):exchange(r1,c1,r2,c2)
##    elif (r2==r1-2 and (c2==c1+1 or c2==c1-1) and (t[r2][c2-1][0]%2!=0)) or (r2==r1-1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]!=0)) or(r2==r1+1 and (c2==c1+2 or c2==c1-2)and (t[r2][c2-1][0]!=0)) or(r2==r1+2 and (c2==c1+1 or c2==c1-1)and (t[r2][c2-1][0]!=0)):exchange2(r1,c1,r2,c2)
def castling(r1,c1,r2,c2,b2):
    global string
    global tprevious,t
    tprevious=tuple(j for i in t for item in i for j in item)#fully converted into tuple(immu)
    string='castled'
    text()
    if r1==8 and c1==8:
        t[8][6]=t[r2][c2-1]
        t[8][5]=t[r1][c1-1]
        t[r1][c1-1]=[0,p[0]]
        t[r2][c2-1]=[0,p[0]]
    elif r1==8 and c1==1:
        t[8][1]=t[r2][c2-1]
        t[8][2]=t[r1][c1-1]
        t[r1][c1-1]=[0,p[0]]
        t[r2][c2-1]=[0,p[0]]
    elif r1==1 and c1==1:
        t[1][1]=t[r2][c2-1]
        t[1][2]=t[r1][c1-1]
        t[r1][c1-1]=[0,p[0]]
        t[r2][c2-1]=[0,p[0]]
    elif r1==1 and c1==8:
        t[1][6]=t[r2][c2-1]
        t[1][5]=t[r1][c1-1]
        t[r1][c1-1]=[0,p[0]]
        t[r2][c2-1]=[0,p[0]]
    buttondraw()

def hathi(r1,c1,r2,c2,b2):
    global bu_count,moves,string
    if (r1!=r2 and c1==c2) or (r1==r2 and c1!=c2):
        hc1=hathi_check(r1,c1,r2,c2)
        hc2=hc1[0]
        hc3=hc1[1]
        print('hc1',hc1,'hc2',hc2,'hc3',hc3)
    if (b1==7 and b2==11 and hc2 and (r1==r2==8 and (c1==1 or c1==8) and c2==5)):castling(r1,c1,r2,c2,b2)
    elif(b1==8 and b2==12 and hc2 and (r1==r2==1 and (c1==1 or c1==8) and c2==5)):castling(r1,c1,r2,c2,b2)
    elif r1!=r2 and c1==c2 and hc2 and hc3:exchange2(r1,c1,r2,c2)
    elif r1==r2 and c1!=c2 and hc2 and hc3:exchange2(r1,c1,r2,c2)
    elif r1!=r2 and c1==c2 and hc2:exchange(r1,c1,r2,c2)
    elif r1==r2 and c1!=c2 and hc2:exchange(r1,c1,r2,c2)
    else:
        string='Invalid Move',r1,c1 
        text()
        print('Invalid Move 6',r1,c1)
        bu_count-=2
        moves-=1
        print('bu_count',bu_count,'moves',moves) 
def hathi_check(r1,c1,r2,c2):
    print(r1,c1,r2,c2)
    hc=0#hathi count
    if b1==7 or b1==9:#for white hathi and white rani
        if r1==r2 and c1>c2:#towards left
            for i in range(c1-1,c2-1,-1):
                if t[r1][i-1][0]==0:
                    hc+=1
                else:break
            print('hc',hc)
            if hc==c1-c2 or (hc==c1-c2-1 and t[r2][c2-1][0]==11 and r1==r2==8):return [1,0]
            elif hc==c1-c2-1 and t[r2][c2-1][0]%2!=1:return [1,1]
            else:return [0,0]
        elif r1==r2 and c1<c2:#towards right
            for i in range(c1+1,c2+1):
                if t[r1][i-1][0]==0:
                    hc+=1
                else:break
            print('hc',hc)
            if hc==c2-c1 or (hc==c2-c1-1 and t[r2][c2-1][0]==11 and r1==r2==8):return [1,0]
            elif hc==c2-c1-1 and t[r2][c2-1][0]%2!=1:return [1,1]
            else:return [0,0]
        elif c1==c2 and r1>r2:#toward up
            for i in range(r1-1,r2-1,-1):
                if t[i][c1-1][0]==0:
                    hc+=1
                    print(hc)
                else:
                    break
            if hc==r1-r2:
                return [1,0]
            elif hc==r1-r2-1 and t[r2][c2-1][0]%2!=1:
                return [1,1]
            else:return [0,0]
        elif c1==c2 and r1<r2:#towards down
            for i in range(r1+1,r2+1):
                if t[i][c1-1][0]==0:
                    hc+=1
                else:
                    break
            if hc==r2-r1:
                return [1,0]
            elif hc==r2-r1-1 and t[r2][c2-1][0]%2!=1:
                return [1,1]
            else:return [0,0]
    elif b1==8 or b1==10:#for black hathi and black rani
        if r1==r2 and c1>c2:#towards left
            for i in range(c1-1,c2-1,-1):
                if t[r1][i-1][0]==0:
                    hc+=1
                else:
                    break
            if hc==c1-c2 or (hc==c1-c2-1 and t[r2][c2-1][0]==12 and r1==r2==1):
                return [1,0]
            elif hc==c1-c2-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:
                return [1,1]
            else:return [0,0]
        elif r1==r2 and c1<c2:#towards right
            for i in range(c1+1,c2+1):
                if t[r1][i-1][0]==0:
                    hc+=1
                else:
                    break
            if hc==c2-c1 or (hc==c2-c1-1 and t[r2][c2-1][0]==12 and r1==r2==1):
                return [1,0]
            elif hc==c2-c1-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:
                return [1,1]
            else:return [0,0]
        elif c1==c2 and r1>r2:#toward up
            for i in range(r1-1,r2-1,-1):
                if t[i][c1-1][0]==0:
                    hc+=1
                    print(hc)
                else:
                    break
            if hc==r1-r2:
                return [1,0]
            elif hc==r1-r2-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:
                return [1,1]
            else:return [0,0]
        elif c1==c2 and r1<r2:#towards down
            for i in range(r1+1,r2+1):
                if t[i][c1-1][0]==0:
                    hc+=1
                else:
                    break
            if hc==r2-r1:
                return [1,0]
            elif hc==r2-r1-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:
                return [1,1]
            else:return [0,0]
           
def unth(r1,c1,r2,c2):
    global bu_count,moves,string
    hc=0
    x=abs(r1-r2)
    if c2==c1+x or c2==c1-x:
        if b1==5 or  b1==9:#white unth and white rani
            if r2<r1 and c2>c1:#topright
                tc=c1+1#tempc
                for i in range(r1-1,r2-1,-1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc+1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=1 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 7',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves) 
            elif r2>r1 and c2<c1:#bottomleft
                tc=c1-1#tempc
                for i in range(r1+1,r2+1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc-1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=1 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 8',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves) 
            elif r2<r1 and c2<c1:#topleft
                tc=c1-1#tempc
                for i in range(r1-1,r2-1,-1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc-1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=1 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 9',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves) 
            elif r2>r1 and c2>c1:#bottomright
                tc=c1+1#tempc
                for i in range(r1+1,r2+1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc+1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=1 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 10',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves)
        elif b1==6 or  b1==10:#black unth and black rani
            if r2<r1 and c2>c1:#topright
                tc=c1+1#tempc
                for i in range(r1-1,r2-1,-1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc+1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 11',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves) 
            elif r2>r1 and c2<c1:#bottomleft
                tc=c1-1#tempc
                for i in range(r1+1,r2+1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc-1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 12',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves) 
            elif r2<r1 and c2<c1:#topleft
                tc=c1-1#tempc
                for i in range(r1-1,r2-1,-1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc-1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 13',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves) 
            elif r2>r1 and c2>c1:#bottomright
                tc=c1+1#tempc
                for i in range(r1+1,r2+1):
                    print(i,tc)
                    if t[i][tc-1][0]==0:
                        hc+=1
                        print(hc)
                        tc=tc+1
                    else:break
                if hc==x:exchange(r1,c1,r2,c2)
                elif hc==x-1 and t[r2][c2-1][0]%2!=0 and t[r2][c2-1][0]!=0:exchange2(r1,c1,r2,c2)
                else:
                    string='Invalid Move',r1,c1 
                    text()
                    print('Invalid Move 14',r1,c1)
                    bu_count-=2
                    moves-=1
                    print('bu_count',bu_count,'moves',moves)
    
def raja(r1,c1,r2,c2):
    global bu_count,moves,string
    if b1==11:
        if r1==r2 and abs(c1-c2)==1 and t[r2][c2-1][0]%2!=1:exchange2(r1,c1,r2,c2)
        elif c1==c2 and abs(r1-r2)==1 and t[r2][c2-1][0]%2!=1:exchange2(r1,c1,r2,c2)
        elif abs(r1-r2)==1 and abs(c1-c2)==1 and t[r2][c2-1][0]%2!=1:exchange2(r1,c1,r2,c2)
        elif r1==r2 and abs(c1-c2)==1 and t[r2][c2-1][0]==0:exchange(r1,c1,r2,c2)
        elif c1==c2 and abs(r1-r2)==1 and t[r2][c2-1][0]==0:exchange(r1,c1,r2,c2)
        elif abs(r1-r2)==1 and abs(c1-c2)==1 and t[r2][c2-1][0]==0:exchange(r1,c1,r2,c2)
        else:
            string='Invalid Move',r1,c1
            text()
            print('Invalid Move 14',r1,c1)
            bu_count-=2
            moves-=1
            print('bu_count',bu_count,'moves',moves)
    elif b1==12:
        if r1==r2 and abs(c1-c2)==1 and t[r2][c2-1][0]%2==1:exchange2(r1,c1,r2,c2)
        elif c1==c2 and abs(r1-r2)==1 and t[r2][c2-1][0]%2==1:exchange2(r1,c1,r2,c2)
        elif abs(r1-r2)==1 and abs(c1-c2)==1 and t[r2][c2-1][0]%2==1:exchange2(r1,c1,r2,c2)
        elif r1==r2 and abs(c1-c2)==1 and t[r2][c2-1][0]==0:exchange(r1,c1,r2,c2)
        elif c1==c2 and abs(r1-r2)==1 and t[r2][c2-1][0]==0:exchange(r1,c1,r2,c2)
        elif abs(r1-r2)==1 and abs(c1-c2)==1 and t[r2][c2-1][0]==0:exchange(r1,c1,r2,c2)
        else:
            string='Invalid Move',r1,c1 
            text()
            print('Invalid Move 14',r1,c1)
            bu_count-=2
            moves-=1
            print('bu_count',bu_count,'moves',moves)
def rani(r1,c1,r2,c2):
    global bu_count,moves,string
    x=abs(r1-r2)
    if (r1==r2 and c1!=c2) or (r1!=r2 and c1==c2):hathi(r1,c1,r2,c2,0)
    elif c2==c1+x or c2==c1-x:unth(r1,c1,r2,c2)
    else:
        string='Invalid Move',r1,c1
        text()
        print('Invalid Move 14',r1,c1)
        bu_count-=2
        moves-=1
        print('bu_count',bu_count,'moves',moves)

def exchange(r1,c1,r2,c2):
    global tprevious,t
    tprevious=tuple(j for i in t for item in i for j in item)#fully converted into tuple(immu)
    print(r1,c1,r2,c2)
    temp1=t[r2][c2-1]
    temp2=t[r1][c1-1]
    t[r1][c1-1]=temp1
    t[r2][c2-1]=temp2
    buttondraw()
def exchange2(r1,c1,r2,c2):
    global tprevious,t
    tprevious=tuple(j for i in t for item in i for j in item)#fully converted into tuple(immu)
    print(r1,c1,r2,c2)
    temp1=t[r2][c2-1]
    temp2=t[r1][c1-1]
    temp1[1]=p[0]
    temp1[0]=0
    t[r1][c1-1]=temp1
    t[r2][c2-1]=temp2
    buttondraw()

#   row=1

but=tk.Button(frame2,height=65,width=75,bg='grey',text='Hathi',command=lambda:check(t[1][0][0],1,1),image=t[1][0][1])
but.grid(row=1,column=1)
but=tk.Button(frame2,height=65,width=75,text='Ghoda',command=lambda:check(t[1][1][0],1,2),image=t[1][1][1])
but.grid(row=1,column=2)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Unth',command=lambda:check(t[1][2][0],1,3),image=t[1][2][1])
but.grid(row=1,column=3)
but=tk.Button(frame2,height=65,width=75,text='Rani',command=lambda:check(t[1][3][0],1,4),image=t[1][3][1])
but.grid(row=1,column=4)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Raja',command=lambda:check(t[1][4][0],1,5),image=t[1][4][1])
but.grid(row=1,column=5)
but=tk.Button(frame2,height=65,width=75,text='Unth',command=lambda:check(t[1][5][0],1,6),image=t[1][5][1])
but.grid(row=1,column=6)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Ghoda',command=lambda:check(t[1][6][0],1,7),image=t[1][6][1])
but.grid(row=1,column=7)
but=tk.Button(frame2,height=65,width=75,text='Hathi',command=lambda:check(t[1][7][0],1,8),image=t[1][7][1])
but.grid(row=1,column=8)
#black sainik---------check(a,function call,row,column) row=2
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][0][0],2,1),image=t[2][0][1])
but.grid(row=2,column=1)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][1][0],2,2),image=t[2][1][1])
but.grid(row=2,column=2)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][2][0],2,3),image=t[2][2][1])
but.grid(row=2,column=3)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][3][0],2,4),image=t[2][3][1])
but.grid(row=2,column=4)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][4][0],2,5),image=t[2][4][1])
but.grid(row=2,column=5)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][5][0],2,6),image=t[2][5][1])
but.grid(row=2,column=6)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][6][0],2,7),image=t[2][6][1])
but.grid(row=2,column=7)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][7][0],2,8),image=t[2][7][1])
but.grid(row=2,column=8)
#whitesainik row=7
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][0][0],7,1),image=t[7][0][1])
but.grid(row=7,column=1)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][1][0],7,2),image=t[7][1][1])
but.grid(row=7,column=2)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][2][0],7,3),image=t[7][2][1])
but.grid(row=7,column=3)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][3][0],7,4),image=t[7][3][1])
but.grid(row=7,column=4)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][4][0],7,5),image=t[7][4][1])
but.grid(row=7,column=5)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][5][0],7,6),image=t[7][5][1])
but.grid(row=7,column=6)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][6][0],7,7),image=t[7][6][1])
but.grid(row=7,column=7)
but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][7][0],7,8),image=t[7][7][1])
but.grid(row=7,column=8)
#emptybox   row=3
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][0][0],3,1),image=t[3][0][1])
but.grid(row=3,column=1)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][1][0],3,2),image=t[3][1][1])
but.grid(row=3,column=2)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][2][0],3,3),image=t[3][2][1])
but.grid(row=3,column=3)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][3][0],3,4),image=t[3][3][1])
but.grid(row=3,column=4)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][4][0],3,5),image=t[3][4][1])
but.grid(row=3,column=5)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][5][0],3,6),image=t[3][5][1])
but.grid(row=3,column=6)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][6][0],3,7),image=t[3][6][1])
but.grid(row=3,column=7)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][7][0],3,8),image=t[3][7][1])
but.grid(row=3,column=8)
#        row=4  
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][0][0],4,1),image=t[4][0][1])
but.grid(row=4,column=1)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][1][0],4,2),image=t[4][1][1])
but.grid(row=4,column=2)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][2][0],4,3),image=t[4][2][1])
but.grid(row=4,column=3)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][3][0],4,4),image=t[4][3][1])
but.grid(row=4,column=4)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][4][0],4,5),image=t[4][4][1])
but.grid(row=4,column=5)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][5][0],4,6),image=t[4][5][1])
but.grid(row=4,column=6)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][6][0],4,7),image=t[4][6][1])
but.grid(row=4,column=7)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][7][0],4,8),image=t[4][7][1])
but.grid(row=4,column=8)
#     row=5
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][0][0],5,1),image=t[5][0][1])
but.grid(row=5,column=1)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][1][0],5,2),image=t[5][1][1])
but.grid(row=5,column=2)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][2][0],5,3),image=t[5][2][1])
but.grid(row=5,column=3)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][3][0],5,4),image=t[5][3][1])
but.grid(row=5,column=4)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][4][0],5,5),image=t[5][4][1])
but.grid(row=5,column=5)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][5][0],5,6),image=t[5][5][1])
but.grid(row=5,column=6)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][6][0],5,7),image=t[5][6][1])
but.grid(row=5,column=7)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][7][0],5,8),image=t[5][7][1])
but.grid(row=5,column=8)
#     row=6
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][0][0],6,1),image=t[6][0][1])
but.grid(row=6,column=1)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][1][0],6,2),image=t[6][1][1])
but.grid(row=6,column=2)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][2][0],6,3),image=t[6][2][1])
but.grid(row=6,column=3)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][3][0],6,4),image=t[6][3][1])
but.grid(row=6,column=4)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][4][0],6,5),image=t[6][4][1])
but.grid(row=6,column=5)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][5][0],6,6),image=t[6][5][1])
but.grid(row=6,column=6)
but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][6][0],6,7),image=t[6][6][1])
but.grid(row=6,column=7)
but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][7][0],6,8),image=t[6][7][1])
but.grid(row=6,column=8)
#row=8
but=tk.Button(frame2,height=65,width=75,text='Hathi',command=lambda:check(t[8][0][0],8,1),image=t[8][0][1])
but.grid(row=8,column=1)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Ghoda',command=lambda:check(t[8][1][0],8,2),image=t[8][1][1])
but.grid(row=8,column=2)
but=tk.Button(frame2,height=65,width=75,text='Unth',command=lambda:check(t[8][2][0],8,3),image=t[8][2][1])
but.grid(row=8,column=3)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Rani',command=lambda:check(t[8][3][0],8,4),image=t[8][3][1])
but.grid(row=8,column=4)
but=tk.Button(frame2,height=65,width=75,text='Raja',command=lambda:check(t[8][4][0],8,5),image=t[8][4][1])
but.grid(row=8,column=5)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Unth',command=lambda:check(t[8][5][0],8,6),image=t[8][5][1])
but.grid(row=8,column=6)
but=tk.Button(frame2,height=65,width=75,text='Ghoda',command=lambda:check(t[8][6][0],8,7),image=t[8][6][1])
but.grid(row=8,column=7)
but=tk.Button(frame2,height=65,width=75,bg='grey',text='Hathi',command=lambda:check(t[8][7][0],8,8),image=t[8][7][1])
but.grid(row=8,column=8)

def back():
    global tprevious,t,bu_count,moves,string
    string=''
    text()
    p1=[[],[],[],[],[],[],[],[]]
    p2=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p3=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p4=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p5=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p6=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p7=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p8=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    p9=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    c=0
    for j in range(8): 
        p2[j][0]=tprevious[c]
        p2[j][1]=tprevious[c+1]
        c=c+2
    c=16
    for j in range(8,16):
        p3[j-8][0]=tprevious[c]
        p3[j-8][1]=tprevious[c+1]
        c=c+2
    c=32
    for j in range(16,24):
        p4[j-16][0]=tprevious[c]
        p4[j-16][1]=tprevious[c+1]
        c=c+2
    c=48
    for j in range(24,32):
        p5[j-24][0]=tprevious[c]
        p5[j-24][1]=tprevious[c+1]
        c=c+2
    c=64
    for j in range(32,40):
        p6[j-32][0]=tprevious[c]
        p6[j-32][1]=tprevious[c+1]
        c=c+2
    c=80
    for j in range(40,48):
        p7[j-40][0]=tprevious[c]
        p7[j-40][1]=tprevious[c+1]
        c=c+2
    c=96
    for j in range(48,56):
        p8[j-48][0]=tprevious[c]
        p8[j-48][1]=tprevious[c+1]
        c=c+2
    c=112
    for j in range(56,64):
        p9[j-56][0]=tprevious[c]
        p9[j-56][1]=tprevious[c+1]
        c=c+2
    t=[p1,p2,p3,p4,p5,p6,p7,p8,p9]#resultant list
##    for i in range(1,9):
##        for j in range(8):
##            print(t[i][j][0],end="")
##        print()
    buttondraw()
    bu_count-=2
    moves-=1
def replay():
    global t,bu_count,moves,string
    string=''
    text()
    t=[[[],[],[],[],[],[],[],[]],#null
    [[8,p[8]],[4,p[4]],[6,p[6]],[10,p[10]],[12,p[12]],[6,p[6]],[4,p[4]],[8,p[8]]],#1
    [[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]],[2,p[2]]],
    [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
    [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
    [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
    [[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]],[0,p[0]]],
    [[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]],[1,p[1]]],
    [[7,p[7]],[3,p[3]],[5,p[5]],[9,p[9]],[11,p[11]],[5,p[5]],[3,p[3]],[7,p[7]]]]
    buttondraw()
    bu_count=0
    moves=0
    
def buttondraw():
    but=tk.Button(frame2,height=1,width=5,font=("times new roman",22,'italic','bold'),bd=5,bg='grey',text='Back',command=lambda:back())#BACK BUTTON
    but.grid(row=7,column=9)
    but=tk.Button(frame2,height=1,width=5,font=("times new roman",22,'italic','bold'),bd=5,bg='grey',text='Replay',command=lambda:replay())
    but.grid(row=8,column=9)
##    for i in range(1,9):
##        for j in range(8):
##                print(t[i][j][0],end="")
##        print()
   #   row=1
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Hathi',command=lambda:check(t[1][0][0],1,1),image=t[1][0][1])
    but.grid(row=1,column=1)
    but=tk.Button(frame2,height=65,width=75,text='Ghoda',command=lambda:check(t[1][1][0],1,2),image=t[1][1][1])
    but.grid(row=1,column=2)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Unth',command=lambda:check(t[1][2][0],1,3),image=t[1][2][1])
    but.grid(row=1,column=3)
    but=tk.Button(frame2,height=65,width=75,text='Rani',command=lambda:check(t[1][3][0],1,4),image=t[1][3][1])
    but.grid(row=1,column=4)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Raja',command=lambda:check(t[1][4][0],1,5),image=t[1][4][1])
    but.grid(row=1,column=5)
    but=tk.Button(frame2,height=65,width=75,text='Unth',command=lambda:check(t[1][5][0],1,6),image=t[1][5][1])
    but.grid(row=1,column=6)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Ghoda',command=lambda:check(t[1][6][0],1,7),image=t[1][6][1])
    but.grid(row=1,column=7)
    but=tk.Button(frame2,height=65,width=75,text='Hathi',command=lambda:check(t[1][7][0],1,8),image=t[1][7][1])
    but.grid(row=1,column=8)
    #black sainik---------check(a,function call,row,column) row=2
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][0][0],2,1),image=t[2][0][1])
    but.grid(row=2,column=1)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][1][0],2,2),image=t[2][1][1])
    but.grid(row=2,column=2)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][2][0],2,3),image=t[2][2][1])
    but.grid(row=2,column=3)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][3][0],2,4),image=t[2][3][1])
    but.grid(row=2,column=4)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][4][0],2,5),image=t[2][4][1])
    but.grid(row=2,column=5)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][5][0],2,6),image=t[2][5][1])
    but.grid(row=2,column=6)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[2][6][0],2,7),image=t[2][6][1])
    but.grid(row=2,column=7)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[2][7][0],2,8),image=t[2][7][1])
    but.grid(row=2,column=8)
    #emptybox   row=3
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][0][0],3,1),image=t[3][0][1])
    but.grid(row=3,column=1)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][1][0],3,2),image=t[3][1][1])
    but.grid(row=3,column=2)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][2][0],3,3),image=t[3][2][1])
    but.grid(row=3,column=3)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][3][0],3,4),image=t[3][3][1])
    but.grid(row=3,column=4)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][4][0],3,5),image=t[3][4][1])
    but.grid(row=3,column=5)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][5][0],3,6),image=t[3][5][1])
    but.grid(row=3,column=6)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[3][6][0],3,7),image=t[3][6][1])
    but.grid(row=3,column=7)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[3][7][0],3,8),image=t[3][7][1])
    but.grid(row=3,column=8)
    #        row=4  
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][0][0],4,1),image=t[4][0][1])
    but.grid(row=4,column=1)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][1][0],4,2),image=t[4][1][1])
    but.grid(row=4,column=2)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][2][0],4,3),image=t[4][2][1])
    but.grid(row=4,column=3)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][3][0],4,4),image=t[4][3][1])
    but.grid(row=4,column=4)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][4][0],4,5),image=t[4][4][1])
    but.grid(row=4,column=5)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][5][0],4,6),image=t[4][5][1])
    but.grid(row=4,column=6)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[4][6][0],4,7),image=t[4][6][1])
    but.grid(row=4,column=7)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[4][7][0],4,8),image=t[4][7][1])
    but.grid(row=4,column=8)
    #     row=5
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][0][0],5,1),image=t[5][0][1])
    but.grid(row=5,column=1)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][1][0],5,2),image=t[5][1][1])
    but.grid(row=5,column=2)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][2][0],5,3),image=t[5][2][1])
    but.grid(row=5,column=3)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][3][0],5,4),image=t[5][3][1])
    but.grid(row=5,column=4)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][4][0],5,5),image=t[5][4][1])
    but.grid(row=5,column=5)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][5][0],5,6),image=t[5][5][1])
    but.grid(row=5,column=6)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[5][6][0],5,7),image=t[5][6][1])
    but.grid(row=5,column=7)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[5][7][0],5,8),image=t[5][7][1])
    but.grid(row=5,column=8)
    #     row=6
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][0][0],6,1),image=t[6][0][1])
    but.grid(row=6,column=1)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][1][0],6,2),image=t[6][1][1])
    but.grid(row=6,column=2)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][2][0],6,3),image=t[6][2][1])
    but.grid(row=6,column=3)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][3][0],6,4),image=t[6][3][1])
    but.grid(row=6,column=4)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][4][0],6,5),image=t[6][4][1])
    but.grid(row=6,column=5)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][5][0],6,6),image=t[6][5][1])
    but.grid(row=6,column=6)
    but=tk.Button(frame2,height=65,width=75,command=lambda:check(t[6][6][0],6,7),image=t[6][6][1])
    but.grid(row=6,column=7)
    but=tk.Button(frame2,height=65,width=75,bg='grey',command=lambda:check(t[6][7][0],6,8),image=t[6][7][1])
    but.grid(row=6,column=8)
    #whitesainik row=7
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][0][0],7,1),image=t[7][0][1])
    but.grid(row=7,column=1)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][1][0],7,2),image=t[7][1][1])
    but.grid(row=7,column=2)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][2][0],7,3),image=t[7][2][1])
    but.grid(row=7,column=3)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][3][0],7,4),image=t[7][3][1])
    but.grid(row=7,column=4)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][4][0],7,5),image=t[7][4][1])
    but.grid(row=7,column=5)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][5][0],7,6),image=t[7][5][1])
    but.grid(row=7,column=6)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Sainik',command=lambda:check(t[7][6][0],7,7),image=t[7][6][1])
    but.grid(row=7,column=7)
    but=tk.Button(frame2,height=65,width=75,text='Sainik',command=lambda:check(t[7][7][0],7,8),image=t[7][7][1])
    but.grid(row=7,column=8)
    #row=8
    but=tk.Button(frame2,height=65,width=75,text='Hathi',command=lambda:check(t[8][0][0],8,1),image=t[8][0][1])
    but.grid(row=8,column=1)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Ghoda',command=lambda:check(t[8][1][0],8,2),image=t[8][1][1])
    but.grid(row=8,column=2)
    but=tk.Button(frame2,height=65,width=75,text='Unth',command=lambda:check(t[8][2][0],8,3),image=t[8][2][1])
    but.grid(row=8,column=3)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Rani',command=lambda:check(t[8][3][0],8,4),image=t[8][3][1])
    but.grid(row=8,column=4)
    but=tk.Button(frame2,height=65,width=75,text='Raja',command=lambda:check(t[8][4][0],8,5),image=t[8][4][1])
    but.grid(row=8,column=5)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Unth',command=lambda:check(t[8][5][0],8,6),image=t[8][5][1])
    but.grid(row=8,column=6)
    but=tk.Button(frame2,height=65,width=75,text='Ghoda',command=lambda:check(t[8][6][0],8,7),image=t[8][6][1])
    but.grid(row=8,column=7)
    but=tk.Button(frame2,height=65,width=75,bg='grey',text='Hathi',command=lambda:check(t[8][7][0],8,8),image=t[8][7][1])
    but.grid(row=8,column=8) 

root.mainloop()










