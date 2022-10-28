# program init
from time import*
import tkinter as tk
from tkinter import simpledialog
TK = tk.Tk()
TK.withdraw()
inputw = simpledialog.askstring(title="HANGMAN Pop-Up",prompt="Type Your Word !")
#inputw = input("Type Your Word : ")
#print (inputw)
lenw = len(inputw)
#print(lenw)
print ("you need to insert",lenw,"letters")
#for i in range(lenw):
#    print(inputw[i])
def Hangman(num):
    if num == 1 :
        # step 1
        color("blue");width(3)
        circle(20);lt(90)
        color("black")
        pu();fd(14);lt(90);fd(6);pd();circle(2)
        pu();bk(12);rt(180);pd();circle(2)
        pu();goto(60,-10);pd();lt(90);color("blue")
    if num == 2 :
        # step 2
        fd(70)
    if num == 3 :
        # step 3
        lt(30);fd(70);bk(70);rt(30)
    if num == 4 :
        # step 4
        rt(30);fd(70);bk(70);lt(30)
    if num == 5 :
        # step 5
        bk(50);lt(120);fd(60);bk(60)
    if num == 6 :
        # step 6 
        lt(120);fd(60);bk(60);rt(60)
    if num == 7 :
        # step 7
        pu();color("black");goto(72,10);pd();goto(50,0)
        pu();goto(-150,120);pd();color("maroon")
        write("GAME OVER !!",font=("Arial", 40, "normal"))
limit = 7
rightGuessCount = 0
wrongGuessCount = 0
oldRGC = 0
gameOn = 1

# turtle init
from turtle import*
import turtle
speed(0)
title("HANGMAN")
hideturtle()
screen = Screen()
screen.screensize(200,200)
screen.bgcolor("orange")
width(13)
pu();goto(0,-150);pd()
bk(160);fd(80);lt(90)
fd(240);rt(90)
fd(140);rt(90)
color("red");width(5)
fd(40);rt(90);circle(30);lt(90)
pu();fd(20);rt(90);pd()
speed(100)

# second turtle init
tu=Turtle()
tu.hideturtle()
tu.speed(0)
tu.pu();tu.goto(-200,-250);tu.pd()
a = 400/(lenw*2)
tu.width(4)
for i in range (lenw*2) :
    if i%2==0 :
        tu.color("black");tu.fd(a)
    else :
        tu.color("orange");tu.fd(a)
#tu.goto(-190+(a*x),-240)
tu.color("black")
# game start
while gameOn :
    guess = input("Guess a letter : ")
    oldRGC = rightGuessCount
    for i in range (lenw):
        if guess == inputw[i] :
            rightGuessCount += 1
            print ("You Guessed ", rightGuessCount , " letter(s) right on the",i+1,"place")
            tu.pu();tu.goto(-200+(2*a*i)+a/2,-245);tu.pd()
            tu.write(guess,font=("Arial", 20, "normal"))
            #inputw[i] = None
    if oldRGC == rightGuessCount :
        print("Wrong Guess !")
        wrongGuessCount += 1
        Hangman(wrongGuessCount)
    if rightGuessCount == lenw :
        print ("!!!!! YOU WON !!!!!")
        pu();goto(-150,120);pd();color("maroon")
        write("YOU WON !!!",font=("Arial", 40, "normal"))
        gameOn = 0
    if wrongGuessCount == limit :
        print ("You Lost :( ")
        gameOn = 0
print("<<<  Game Over :)  >>>")
sleep(6)