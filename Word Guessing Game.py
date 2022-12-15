"""
Created on Mon Feb 21 01:55:42 2022

@author: Kshiti
"""

import tkinter as gui
from tkinter import messagebox;
import mysql.connector as sql
import random

app=gui.Tk()
app.title("Word Guessing Game")
app.geometry("700x400")

messagebox.showinfo("Instructions","Instructions : \n\nYou will be given 5 chances to guess the word.\n\nYou can enter one letter per chance.\n\nMake sure to enter the letters in lower-case\n\nThe number of chances remaining will be your score")

#------ D A T A B A S E  S E T U P -------------
try:
    mydb=sql.connect(host="localhost",
                      user="root",
                      password="admin", 
                      database="project")
    mycur=mydb.cursor()
except:
    mydb=sql.connect(host="localhost",
                      user="root",
                      password="admin")
    mycur=mydb.cursor()
    mycur.execute("CREATE DATABASE project")
    mycur.execute("USE project")

def game():
        
    #----------- G A M E  S E T T I N G S -----------
    wordlist = ['strong','television','mother','zebra','miracle','science','geography','thousand','currency','foreign','intelligent','particle','feminine','computer','calculus','trousers','scissors','alphabet','musician','criminal','children','teachers','students','vehicles','terrific','adjust','moment','prescribe','standard','multiply','division','arrogant','preserve','aggregate','average','measure','composition','insurance','history','mathematics','patience','problem','essence','entertainment','rythm','official','parents','students','principal','trouble','resonance','religion','belief','receive','budget','mindful','meaning','surround','stretch','suggest','casual','conflict','depend','disaster','envelope','gorvernment','hilarious','horror','lavish','leather','museum','november','august','resist','trouble','umbrella','variety','weather','material','tourist']
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    wsel = random.randint(0,len(wordlist)-1)
    #------------------------------------------
    word = wordlist[wsel]
    #print(len(wordlist))
    #print(word)
    score = 5
    dashword = ''
    dashwordlist=[]
    #----------- D E S I G N ------------------
    for letter in word:
        dashwordlist.append(' __ ')
    for dash in dashwordlist:
        dashword=dashword+dash
    #print(dashwordlist)
    #print(dashword)
    wordlabel.configure(text=dashword)
    #print('\nchances left - ', score)
    scorelabel.configure(text=score)
    #---------------- G A M E --------------------------
    while ' __ ' in dashwordlist:
        dashword=''
        guess = gui.simpledialog.askstring("Guess", "Guess a Letter",parent=app)
        if guess in alphabets:
            alphabets.remove(guess)
        else:
            if guess not in word:
                score+=1
            gui.messagebox.showerror("Word Guessing Game","You have already guessed this letter")
        for guessl in range(0,len(word)):
            if word[guessl]==guess:
                dashwordlist[guessl]=guess+' '
        for dashg in dashwordlist:
            dashword=dashword+dashg
        #print(dashword)
        wordlabel.configure(text=dashword)
        #print(dashwordlist)
        if guess not in word:
            score = score-1
        scorelabel.configure(text=score)
        if score ==0:
            gui.messagebox.showinfo("Word Guessing Game","YOU LOSE, the word was {}".format(word))
            break
    if score!=0:
        gui.messagebox.showinfo("Word Guessing Game","YOU WIN")
    #--------- E N T E R I N G  S C O R E ---------------
    name = gui.simpledialog.askstring("Info", "Enter your Name",parent=app)
    try:
        mycur.execute("CREATE TABLE LEADERBOARD(NAME VARCHAR(20) PRIMARY KEY,SCORE NUMERIC(65))")
        mycur.execute("INSERT INTO LEADERBOARD VALUES('{}',{})".format(name,score))
        mydb.commit()
        gui.messagebox.showinfo("Word Guessing Game","Your score has been added to the leaderboard successfully")
    except: 
        try:
            mycur.execute("SELECT * FROM LEADERBOARD WHERE NAME='{}'".format(name))
            row=mycur.fetchall()
            iscore=row[0][1]
            mycur.execute("UPDATE LEADERBOARD SET SCORE={} WHERE NAME='{}'".format(iscore+score,name))
            mydb.commit()
            gui.messagebox.showinfo("Word Guessing Game","Your score has been added to the leaderboard successfully")
        except:
            mycur.execute("INSERT INTO LEADERBOARD VALUES('{}',{})".format(name,score))
            mydb.commit()
            gui.messagebox.showinfo("Word Guessing Game","Your score has been added to the leaderboard successfully")

def instruction():
        gui.messagebox.showinfo("Instructions","Instructions : \n\nYou will be given 5 chances to guess the word.\n\nYou can enter one letter per chance.\n\nMake sure to enter the letters in lower-case\n\nThe number of chances remaining will be your score")

def playb():
    try:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin", 
                          database="project")
        mycur=mydb.cursor()
    except:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin")
        mycur=mydb.cursor()
        mycur.execute("CREATE DATABASE project")
        mycur.execute("USE project")
        
    lbnamelabel.configure(text="")
    label2_1.configure(text="")
    lbscorelabel.configure(text="")
    label2_2.configure(text="")
    label1.configure(text="Chances : ")
    game()
    
def disleadb():
    try:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin", 
                          database="project")
        mycur=mydb.cursor()
    except:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin")
        mycur=mydb.cursor()
        mycur.execute("CREATE DATABASE project")
        mycur.execute("USE project")

    mycur.execute("SELECT * FROM LEADERBOARD")
    label2_1.configure(text="Name")
    label2_2.configure(text="Score")
    wordlabel.configure(text="")
    scorelabel.configure(text="")
    label1.configure(text="")
    lbnamelabel.configure(text="")
    lbscorelabel.configure(text="")
    for cell in mycur:
        lbnamelabel.configure(text=lbnamelabel.cget("text")+"{}\n".format(cell[0]))
        lbscorelabel.configure(text=lbscorelabel.cget("text")+"{}\n".format(cell[1]))
    mycur.close()
    
def remnameb():
    try:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin", 
                          database="project")
        mycur=mydb.cursor()
    except:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin")
        mycur=mydb.cursor()
        mycur.execute("CREATE DATABASE project")
        mycur.execute("USE project")

    rname = gui.simpledialog.askstring("Word Guessing Game", "Enter your Name")
    mycur.execute("SELECT * FROM LEADERBOARD")
    c=0
    for cell in mycur:
        if cell[0]==rname:
            c+=1
    if c>0:
        mycur.execute("DELETE FROM LEADERBOARD WHERE NAME='{}'".format(rname))
        gui.messagebox.showinfo("Word Guessing Game","Your score has been deleted from the leaderboard successfully")
        mydb.commit()
    else:
        gui.messagebox.showerror("Word Guessing Game","Your name does not exist in the leaderboard")
            

def clearleadb():
    try:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin", 
                          database="project")
        mycur=mydb.cursor()
    except:
        mydb=sql.connect(host="localhost",
                          user="root",
                          password="admin")
        mycur=mydb.cursor()
        mycur.execute("CREATE DATABASE project")
        mycur.execute("USE project")
        
    mycur.execute('SELECT * FROM LEADERBOARD')
    records=mycur.fetchall()
    for record in records:
        cname=record[0]
        mycur.execute("DELETE FROM LEADERBOARD WHERE NAME='{}'".format(cname))
        gui.messagebox.showinfo("Word Guessing Game","Leaderboard has been cleared successfully")
        mydb.commit()
    
wordlabel = gui.Label(app,text="")
wordlabel.place(x=300,y=100)

label1 = gui.Label(app,text="")
label1.place(x=300,y=200)
scorelabel = gui.Label(app,text="")
scorelabel.place(x=370,y=200)

instbutton = gui.Button(app,text="Instructions",command=instruction,height=2)
instbutton.place(x=60,y=300)

playbutton = gui.Button(app,text="Play",command=playb,height=2,width=7)
playbutton.place(x=150,y=300)

disleadbutton = gui.Button(app,text="Display Leaderboard",command=disleadb,height=2)
disleadbutton.place(x=230,y=300)

label2_1 = gui.Label(app,text="")
label2_1.place(x=100,y=50)
label2_2 = gui.Label(app,text="")
label2_2.place(x=200,y=50)
lbnamelabel = gui.Label(app)
lbnamelabel.place(x=100,y=100)
lbscorelabel = gui.Label(app)
lbscorelabel.place(x=200,y=100)

remnamebutton = gui.Button(app,text="Remove Name from\nLeaderboard",command=remnameb)
remnamebutton.place(x=370,y=300)

clearleadbutton = gui.Button(app,text="Clear Leaderboard",command=clearleadb,height=2)
clearleadbutton.place(x=510,y=300)

app.mainloop()
