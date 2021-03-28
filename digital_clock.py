import turtle
import time

screen = turtle.Screen() #turtle screen
screen.bgcolor("black") #background of the screen
screen.setup(width=600, height=600) #geometry of the GUI
screen.title("Digital Watch") #title of the GUI
screen.tracer(0) #tracer for the GUI

Sui = turtle.Turtle() #the turtle
Sui .hideturtle() #make the turtle invisible
Sui .speed(0) #setting the speed to 0
Sui.pensize(3) #setting the pensize to 3


def myWatch(hrs, min, sec, Sui ): #function with 4 parameters

    Sui .up() #not ready to draw
    Sui .goto(0, 210) #positioning the turtle
    Sui.setheading(180) #setting the heading to 180
    Sui .color("red") #setting the color of the pen to red
    Sui.pendown() #starting to draw
    Sui .circle(210) #a circle with the radius 210

    Sui .up() #not ready to draw
    Sui .goto(0, 0) #positioning the turtle
    Sui .setheading(90) #same as seth(90) in newer version

    for z in range(12): #loop
        Sui .fd(190) #moving forward at 190 units
        Sui .pendown() #starting to draw
        Sui .fd(20) #forward at 20
        Sui .penup() #not ready to draw
        Sui .goto(0, 0) #positioning the turtle
        Sui .rt(30) #right at an angle of 30 degrees

    hands = [("white", 80, 12), ("white", 150, 60), ("white", 110, 60)] #the color and the hands set
    time_set = (hrs, min, sec) #setting the time

    for hand in hands: #loop
        time_part = time_set[hands.index(hand)] #time part in the hand index in hands of time_Set
        angle = (time_part/hand[2])*360 #setting the angle for the clock
        Sui .penup() #not ready to draw
        Sui .goto(0, 0) #positioning the turtle
        Sui .color(hand[0]) #setting the color of the hand
        Sui .setheading(90) #same as seth(90)
        Sui .rt(angle) #right at an angle of "right"
        Sui .pendown() #ready to draw
        Sui .fd(hand[1]) #forward at a unit of 1st index of the hand var


while True:
    hrs= int(time.strftime("%I")) #setting the hour from the time module
    min = int(time.strftime("%M")) #setting the minute from the time module
    sec = int(time.strftime("%S")) #setting the second as above

    myWatch(hrs, min, sec, Sui) #calling the ghanta_bana() function with the given parameters
    screen.update() #updating the scren
    time.sleep(1) #making the code sleep for a second with the time module
    Sui .clear() #clearing the pen