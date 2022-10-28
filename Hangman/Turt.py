from turtle import*
speed(1.5)
title("HANGMAN")
#hideturtle()
screen = Screen()
screen.screensize(200,200)
screen.bgcolor("orange")
width(15)
pu();goto(0,-150);pd()
bk(160);fd(80);lt(90)
fd(240);rt(90)
fd(140);rt(90)
color("red");width(5)
fd(40);rt(90);circle(30);lt(90)
pu();fd(20);rt(90);pd()
# step 1
color("cyan");width(3)
circle(20);lt(90)
color("black")
pu();fd(14);lt(90);fd(6);pd();circle(2)
pu();bk(12);rt(180);pd();circle(2)
pu();goto(60,-10);pd();lt(90);color("cyan")
# step 2
fd(70)
# step 3
lt(30);fd(70);bk(70);rt(30)
# step 4
rt(30);fd(70);bk(70);lt(30)
# step 5
bk(50);lt(120);fd(60);bk(60)
# step 6 
lt(120);fd(60);bk(60);rt(60)
# step 7
pu();color("black");goto(72,10);pd();goto(48,0)
pu();goto(-150,120);pd();color("maroon")
write("GAME OVER !!",font=("Arial", 40, "normal"))