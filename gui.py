#16CSU225
#NEHAL BIRLA
#PYTHON PROJECT

#GUI
inx = None
file = None
pic = None
from tkinter import  *
from tkinter import  messagebox
import sys
sys.path.append('C:/Users/naveen/Desktop/code/python/python project')
from python_project import *

top = Tk(className = 'login')
top.geometry('500x500')
m = '#%02x%02x%02x' % (192,192,192)
top.config(bg = m)
top.resizable(False,False)
bullet = '\u2022'
l = Label(top,text = 'Phone\n Directory',bg=m)
l.config(font = ('Times New Roman',50))
l.pack()
l1 = Label(top,text = 'Login',bg=m)
l1.config(font = ('Times New Roman',20))
l1.pack()
l1.place(x=210,y=190)
l2 = Label(top,text = 'Enter password :',bg=m)
l2.config(font = ('Times New Roman',13))
l2.pack()
l2.place(x = 100,y=300)
e = Entry(top,show=bullet)
e.pack()
e.place(x = 218,y=302)


def login() :
    with open('psd','r') as fw :
        psd = fw.read()
    s = e.get()

    
    if s == psd :
        print('yes')
        #print(psd)
        e.delete(0,'end')
        top.withdraw()
        tuple1()
    elif len(s) == 0 :
        messagebox.showerror(title = 'Login Failed',message = 'Password can not be null')
        print('null')
    else :
        messagebox.showerror(title = 'Login Failed',message = 'Wrong Password')
        print('no')


pas_screen=lab1=lab2=lab3=ent1=ent2=ent3=None

    
def cp() :
    
    old = ent1.get()
    new = ent2.get()
    new1 = ent3.get()
    with open('psd','r') as fw :
        psd = fw.read()
    if old != psd :
        messagebox.showerror(title= ' ' ,message = 'Wrong old password')
    elif new1 != new :
        messagebox.showerror(title= ' ' ,message = 'new password does not match')
    else :
        with open('psd','w') as fw :
            psd = fw.write(new)
        messagebox.showinfo(title='successful',message='password changed')
        disable_event0()
    

def disable_event0() :
    top.deiconify()
    pas_screen.destroy()        
    

def change() :
    top.withdraw()
    global pas_screen,lab1,lab2,lab3,ent1,ent2,ent3
    pas_screen = Toplevel()
    pas_screen.geometry('170x170')
    lab1 = Label(pas_screen,text = 'Enter old password')
    lab1.pack()

    ent1 = Entry(pas_screen,show=bullet)
    ent1.pack()

    lab2 = Label(pas_screen,text='Enter new password')
    lab2.pack()

    ent2 = Entry(pas_screen,show=bullet)
    ent2.pack()

    lab3 = Label(pas_screen,text='Enter new password again')
    lab3.pack()

    ent3 = Entry(pas_screen,show=bullet)
    ent3.pack()

    butt = Button(pas_screen,text ='OK',command = cp)
    butt.pack()
    pas_screen.resizable(False,False)

    pas_screen.protocol("WM_DELETE_WINDOW", disable_event0)



b = Button(top, text = 'Login',command = login)
b.pack()
b.place(y=360,x = 150)
b1 = Button(top,text = 'Exit',command = top.destroy)
b1.pack()
b1.place(x = 360,y = 360,width = 40)

b3 = Button(top,text='Change Password',command = change)
b3.pack()
b3.place(x=225,y=360)



def disable_event():
    w1.withdraw()
    top.deiconify()



bl=w1=ep=lp=lf=ef=ll=el=lpno=epno=la=ea=lc=ec = None

def Tuple(l,ix) :
    global bl,w1,ep,lp,lf,ef,ll,el,lpno,epno,la,ea,lc,ec
    if w1 == None :
        w1 = Toplevel()
        w1.geometry('500x445')
        w1.resizable(False,False)
   # l = firstTuple()
    #global inx
    #inx = ix
    s = 'Entry Number : '+str(ix)
    bl = Label(w1,text = s)
    bl.pack()
    bl.config(font = ('Times New Roman',20))
    
    
    lp = Label(w1,text = 'P.ID.')
    lp.pack()
    lp.place(x = 75,y = 70) 
    ep = Entry(w1)
    ep.insert(0,l[0])
    ep.configure(state = 'readonly',width = 8)
    ep.pack()
    ep.place(x = 125,y = 71)
    lp.config(font = ('Times New Roman',12))
    ep.config(font = ('Times New Roman',12))


    lf = Label(w1,text = 'First Name')
    lf.pack()
    lf.place(x = 42,y=110)
    ef = Entry(w1)
    ef.insert(0,l[1])
    ef.configure(state = 'readonly',width = 13)
    ef.pack()
    ef.place(x = 124,y = 112)
    lf.config(font = ('Times New Roman',12))
    ef.config(font = ('Times New Roman',12))

    ll = Label(w1,text = 'Last Name')
    ll.pack()
    ll.place(x = 43,y=150)
    el = Entry(w1)
    el.insert(0,l[2])
    el.configure(state = 'readonly',width = 13)
    el.pack()
    el.place(x = 125,y = 151)
    ll.config(font = ('Times New Roman',12))
    el.config(font = ('Times New Roman',12))

    lpno = Label(w1,text = 'Phone Number')
    lpno.pack()
    lpno.place(x = 19,y=190)
    epno = Entry(w1)
    epno.insert(0,l[3])
    epno.configure(state = 'readonly',width = 13)
    epno.pack()
    epno.place(x = 125,y = 190)
    lpno.config(font = ('Times New Roman',12))
    epno.config(font = ('Times New Roman',12))

    la = Label(w1,text = 'Address')
    la.pack()
    la.place(x = 58,y=230)
    ea = Entry(w1)
    ea.insert(0,l[4])
    ea.configure(state = 'readonly',width = 25)
    ea.pack()
    ea.place(x = 125,y = 230)
    la.config(font = ('Times New Roman',12))
    ea.config(font = ('Times New Roman',12))

    lc = Label(w1,text = 'City')
    lc.pack()
    lc.place(x = 83,y=270)
    ec = Entry(w1)
    ec.insert(0,l[5])
    ec.configure(state = 'readonly',width = 15)
    ec.pack()
    ec.place(x = 125,y = 271)
    lc.config(font = ('Times New Roman',12))
    ec.config(font = ('Times New Roman',12))

    bf = Button(w1,text = 'first',command = tuple1,width=13,height=2)
    bf.pack()
    bf.place(y=350,x = 35)
    
    bn = Button(w1,text = 'Next',command = nextEntry,width=13,height=2)
    bn.pack()
    bn.place(y=350,x = 245)


    bp = Button(w1,text = 'Previous',command = prevEntry,width=13,height=2)
    bp.pack()
    bp.place(y=350,x = 140)


    bla = Button(w1,text = 'Last',command = tuplel,width=13,height=2)
    bla.pack()
    bla.place(y=350,x = 350)

    bi = Button(w1,text = 'Add',command = Insert,width=13,height=2)
    bi.pack()
    bi.place(y=393,x = 35)
    
    bu = Button(w1,text = 'Update',command = Update,width=13,height=2)
    bu.pack()
    bu.place(y=393,x = 245)


    bd = Button(w1,text = 'Delete',command = Delete,width=13,height=2)
    bd.pack()
    bd.place(y=393,x = 140)


    bs = Button(w1,text = 'Search',command = Search,width=13,height=2)
    bs.pack()
    bs.place(y=393,x = 350)

    w1.protocol("WM_DELETE_WINDOW", w1.withdraw)

    can = Canvas(w1,bg = 'pink',height = 125,width = 125)
    can.pack()
    can.place(x=360,y=40)
    global pic
    pic = l[6]
    if pic == '-\n' :
        print('yes')
        msg = Message(w1,text = 'No photo')
        msg.pack()
        msg.place(x = 394,y = 95)
    else :
        try :
            global file
            file = PhotoImage(file = pic[:-1])
            img = can.create_image(64,64,image = file)
        except :
            msg = Message(w1,text = 'No photo')
            msg.pack()
            msg.place(x = 394,y = 95)
    w1.protocol("WM_DELETE_WINDOW", disable_event)



def tuple1() :
    l = firstTuple()
    global inx
    if len(l) == 0 :
        messagebox.showerror(title = ' ',message = 'Empty Database')
    else :
    
        global bl,ep,lp,lf,ef,ll,el,lpno,epno,la,ea,lc,ec
        if inx is not None :
            bl.destroy()
            ep.destroy()
            lp.destroy()
            lf.destroy()
            ef.destroy()
            ll.destroy()
            el.destroy()
            lpno.destroy()
            epno.destroy()
            la.destroy()
            ec.destroy()
            ea.destroy()
            la.destroy() 
        inx = 1
        if w1 is not None :
            w1.deiconify()
        Tuple(l,inx)


def tuplel() :
    l = lastTuple()
    lt = readFile()
    global inx
    if len(l) == 0 :
        messagebox.showerror(title = ' ',message = 'Empty Database')
    else :
        
        global bl,ep,lp,lf,ef,ll,el,lpno,epno,la,ea,lc,ec
        if inx is not None :
            bl.destroy()
            ep.destroy()
            lp.destroy()
            lf.destroy()
            ef.destroy()
            ll.destroy()
            el.destroy()
            lpno.destroy()
            epno.destroy()
            la.destroy()
            ec.destroy()
            ea.destroy()
            la.destroy() 
        inx = len(lt)
        Tuple(l,inx)



def nextEntry() :
    global inx
    l = nextTuple(inx)
    if l == None :
        messagebox.showerror(title = ' ',message = 'Database Finished')
    else :
        global bl,ep,lp,lf,ef,ll,el,lpno,epno,la,ea,lc,ec
        bl.destroy()
        ep.destroy()
        lp.destroy()
        lf.destroy()
        ef.destroy()
        ll.destroy()
        el.destroy()
        lpno.destroy()
        epno.destroy()
        la.destroy()
        ec.destroy()
        ea.destroy()
        la.destroy()
        inx += 1
        Tuple(l,inx)



def prevEntry() :
    l = prevTuple()
    if l == None :
        messagebox.showerror(title = ' ',message = 'Database Finished')
    else :
        global bl,inx,ep,lp,lf,ef,ll,el,lpno,epno,la,ea,lc,ec
        bl.destroy()
        ep.destroy()
        lp.destroy()
        lf.destroy()
        ef.destroy()
        ll.destroy()
        el.destroy()
        lpno.destroy()
        epno.destroy()
        la.destroy()
        ec.destroy()
        ea.destroy()
        la.destroy()
        inx -= 1
        Tuple(l,inx)

w2=bl1=ep1=lp1=lf1=ef1=ll1=el1=lpno1=epno1=la1=ea1=lc1=ec1=lpi1=epi1=None


def Insert() :
    global bl1,w1,ep1,lp1,lf1,ef1,ll1,el1,lpno1,epno1,la1,ea1,lc1,ec1,lpi1,epi1,w2
    w1.withdraw()
    w2 = Toplevel()
    w2.geometry('500x400')
    w2.resizable(False,False)
   

    bl1 = Label(w2,text = 'Enter the values')
    bl1.pack()
    bl1.config(font = ('Times New Roman',20))
    
    
    lp1 = Label(w2,text = 'P.ID.')
    lp1.pack()
    lp1.place(x = 75,y = 70) 
    ep1 = Entry(w2)

    ep1.pack()
    ep1.place(x = 125,y = 71)
    lp1.config(font = ('Times New Roman',12))
    ep1.config(width = 8,font = ('Times New Roman',12))
    

    lf1 = Label(w2,text = 'First Name')
    lf1.pack()
    lf1.place(x = 42,y=110)
    ef1 = Entry(w2)

    ef1.pack()
    ef1.place(x = 124,y = 112)
    lf1.config(font = ('Times New Roman',12))
    ef1.config(width = 13,font = ('Times New Roman',12))
    

    
    ll1 = Label(w2,text = 'Last Name')
    ll1.pack()
    ll1.place(x = 43,y=150)
    el1 = Entry(w2)

    el1.pack()
    el1.place(x = 125,y = 151)
    ll1.config(font = ('Times New Roman',12))
    el1.config(width = 13,font = ('Times New Roman',12))
    

    
    lpno1 = Label(w2,text = 'Phone Number')
    lpno1.pack()
    lpno1.place(x = 19,y=190)
    epno1 = Entry(w2)

    epno1.pack()
    epno1.place(x = 125,y = 190)
    lpno1.config(font = ('Times New Roman',12))
    epno1.config(font = ('Times New Roman',12),width = 13)
    
    
    la1 = Label(w2,text = 'Address')
    la1.pack()
    la1.place(x = 58,y=230)
    ea1 = Entry(w2)

    ea1.pack()
    ea1.place(x = 125,y = 230)
    la1.config(font = ('Times New Roman',12))
    ea1.config(width = 25,font = ('Times New Roman',12))
    
    lc1 = Label(w2,text = 'City')
    lc1.pack()
    lc1.place(x = 83,y=270)
    ec1 = Entry(w2)

    ec1.pack()
    ec1.place(x = 125,y = 271)
    lc1.config(font = ('Times New Roman',12))
    ec1.config(width = 15,font = ('Times New Roman',12))
    
    lpi1 = Label(w2,text = 'Image')
    lpi1.pack()
    lpi1.place(x = 82,y = 310)
    epi1 = Entry(w2)
    epi1.pack()
    epi1.place(x = 125,y = 311)
    lpi1.config(font = ('Times New Roman',12))
    epi1.config(width =8 ,font = ('Times New Roman',12))

    bo = Button(w2,width = 5,text = 'OK',command = add)
    bo.pack()
    bo.place(y=350,x=150)

    bc = Button(w2,width = 6,text = 'Cancel',command = disable_event1)
    bc.pack()
    bc.place(y=350,x=300)


    w2.protocol("WM_DELETE_WINDOW", disable_event1)



def disable_event1() :
    w2.destroy()
    tuple1()
    w1.deiconify()
    
    
def add() :
    p = ep1.get()
    pi = epi1.get()
    c = ec1.get()
    ad = ea1.get()
    pn = epno1.get()
    l = el1.get()
    f = ef1.get()
    t = insertTable(p,f,l,pn,ad,c,pi)
    if t != 'tuple added' :
        messagebox.showerror(title = 'try again',message = t)
    else :
        messagebox.showinfo(title=' ',message = t)
        w2.destroy()
        w1.deiconify()
    
e0=w3=None



def Search() :
    w1.withdraw()
    global e0,w3
    w3 = Toplevel()
    w3.geometry('200x170')
    l = Label(w3,text = 'Enter P.ID.',font=('Times new roman',12))
    l.pack()
    l.place(x=58,y=30)
    e0 = Entry(w3,font=('times new roman',12))
    e0.pack()
    e0.place(x=15,y=60)
    b = Button(w3,text = 'OK',command = Find,width = 5)
    b.pack()
    b.place(x=35,y=110)
    bc = Button(w3,text = 'Cancel',command= disable_event3,width=5)
    bc.pack()
    bc.place(x=110,y=110)
    w3.protocol("WM_DELETE_WINDOW", disable_event3)
    


def disable_event3() :
    w3.destroy()
    w1.deiconify()


def Find() :
    p = e0.get()
    l = search(p)
    if l == 'no entry found' :
        messagebox.showerror(title='try again',message = 'no entry found with P.ID. '+p.upper())
    else :
        global bl,inx
        bl.destroy()
        l1 = l.pop(0)
        inx = l.pop()
        w3.destroy()
        Tuple(l1,inx)
        w1.deiconify()
    


def Delete() :
    res = messagebox.askquestion(title= 'Delete',message = 'Are you sure you want to delete this record?')
    if res == 'yes' :
        p = ep.get()
        dele = delete(p)
        if dele == 'deleted' :
            messagebox.showinfo(title = 'done',message = 'deleted')
            nextEntry()
            prevEntry()
           
        else :
            messagebox.showerror(title = 'not deleted',message = dele)
    

def Update() :
    resu = messagebox.askquestion(title= 'Update',message = 'Are you sure you want to update this record?')
    if resu == 'yes' :
        
        
        global bl1,w1,ep1,lp1,lf1,ef1,ll1,el1,lpno1,epno1,la1,ea1,lc1,ec1,lpi1,epi1,w2
        w1.withdraw()
        w2 = Toplevel()
        w2.geometry('500x400')
        w2.resizable(False,False)
       

        bl1 = Label(w2,text = 'Enter the values')
        bl1.pack()
        bl1.config(font = ('Times New Roman',20))
        
        
        lp1 = Label(w2,text = 'P.ID.')
        lp1.pack()
        lp1.place(x = 75,y = 70) 
        ep1 = Entry(w2)

        ep1.pack()
        ep1.place(x = 125,y = 71)
        ep1.insert(0,ep.get())
        lp1.config(font = ('Times New Roman',12))
        ep1.config(width = 8,font = ('Times New Roman',12),state='readonly')
        

        lf1 = Label(w2,text = 'First Name')
        lf1.pack()
        lf1.place(x = 42,y=110)
        ef1 = Entry(w2)

        ef1.pack()
        ef1.place(x = 124,y = 112)
        ef1.insert(0,ef.get())
        lf1.config(font = ('Times New Roman',12))
        ef1.config(width = 13,font = ('Times New Roman',12))
        

        
        ll1 = Label(w2,text = 'Last Name')
        ll1.pack()
        ll1.place(x = 43,y=150)
        el1 = Entry(w2)

        el1.pack()
        el1.place(x = 125,y = 151)
        el1.insert(0,el.get())
        ll1.config(font = ('Times New Roman',12))
        el1.config(width = 13,font = ('Times New Roman',12))
        

        
        lpno1 = Label(w2,text = 'Phone Number')
        lpno1.pack()
        lpno1.place(x = 19,y=190)
        epno1 = Entry(w2)

        epno1.pack()
        epno1.place(x = 125,y = 190)
        epno1.insert(0,epno.get())
        lpno1.config(font = ('Times New Roman',12))
        epno1.config(font = ('Times New Roman',12),width = 13)
        
        
        la1 = Label(w2,text = 'Address')
        la1.pack()
        la1.place(x = 58,y=230)
        ea1 = Entry(w2)

        ea1.pack()
        ea1.place(x = 125,y = 230)
        ea1.insert(0,ea.get())
        la1.config(font = ('Times New Roman',12))
        ea1.config(width = 25,font = ('Times New Roman',12))
        

        
        lc1 = Label(w2,text = 'City')
        lc1.pack()
        lc1.place(x = 83,y=270)
        ec1 = Entry(w2)

        ec1.pack()
        ec1.place(x = 125,y = 271)
        ec1.insert(0,ec.get())
        lc1.config(font = ('Times New Roman',12))
        ec1.config(width = 15,font = ('Times New Roman',12))
        

        lpi1 = Label(w2,text = 'Image')
        lpi1.pack()
        lpi1.place(x = 82,y = 310)
        epi1 = Entry(w2)
        epi1.pack()
        epi1.place(x = 125,y = 311)
        epi1.insert(0,pic)
        lpi1.config(font = ('Times New Roman',12))
        epi1.config(width =8 ,font = ('Times New Roman',12))
        
            
       

        bo = Button(w2,width = 5,text = 'OK',command = updateTuple)
        bo.pack()
        bo.place(y=350,x=150)

        bc = Button(w2,width = 6,text = 'Cancel',command = disable_event1)
        bc.pack()
        bc.place(y=350,x=300)

        

        w2.protocol("WM_DELETE_WINDOW", disable_event1)



def updateTuple() :
    p = ep1.get()
    pi = epi1.get()
    c = ec1.get()
    ad = ea1.get()
    pn = epno1.get()
    la = el1.get()
    f = ef1.get()
    l = update(p,f,la,pn,ad,c,pi)
    messagebox.showinfo(title= ' ',message  = 'Updated')
    disable_event1()
    
        
top.mainloop()
