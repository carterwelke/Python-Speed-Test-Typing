# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

class Title(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        # don't assume that self.parent is a root window.
        # instead, call `winfo_toplevel to get the root window
        self.winfo_toplevel().title("Typing Speed Game")

        # this adds something to the frame, otherwise the default
        # size of the window will be very small
        label = Entry(self)
        label.pack(side="top", fill="x")

# creating window using gui
window = Tk()
title=Title(window)

# the size of the window is defined
window.geometry("850x230")

start = 0.0

# defining the function for the test
def game():
    global start
    def check_result():
        if len(entry.get()) == len(words[word]):
  
            # here start time is when the window
            # is opened and end time is when
            # window is destroyed
            print("stopping timer!")
            end = timer()

            # we deduct the start time from end
            # time and calculate results using
            # timeit function
            LIM = 5
            time = end-start
            time_for_speed = end-start
            time = str(end-start)[:LIM]
            time += "s"
            
            #calculate speed and place in window
            speed = Label(window, text=time, font="times 12")
            speed.place(x=100, y=150)
            print("Time:",time)

            #calculate accuracy and place in window
            numRight = 0
            for i in range(len(words[word])):
                if words[word][i] == entry.get()[i]:
                    numRight += 1
            accuracy = numRight/(len(words[word]))*100
            accuracy = str(accuracy)[:LIM]
            accuracy += "%"
            acc = Label(window, text = accuracy, font="times 12")
            acc.place(x=80,y=190)
            print("Accuracy:",accuracy)

            #calculate WPM and place in window
            wPm = 0
            numWords = 1
            for i in range(len(words[word])):
                if(words[word][i].isspace()):
                    numWords=numWords+1
            wPm = time_for_speed / numWords
            wPm = wPm * 60
            wPm = str(wPm)[:LIM]
            speedz = Label(window, text = wPm, font="times 12")
            speedz.place(x=130,y=170)
            print("WPM:",wPm)
        else:
            print("Wrong Input")

    #reset game, reset sentence and text input
    def reset():
        wordToType.destroy()
        entry.destroy()
        game()
    
    def checkInput(var, indx, mode):
        if len(entry.get()) == len(words[word]):
            #print("Match!")
            check_result()
        # start timer using timeit function
        global start
        if len(entry.get()) == 1:
            print("starting timer!")
            start = timer()
    
    words = ['Quizzical twins proved my hijack-bug fix', 
    'Waxy and quivering, jocks fumble the pizza', 
    'Sympathizing would fix Quaker objectives',
    'Watch “Jeopardy!”, Alex Trebek’s fun TV quiz game', 
    'Few black taxis drive up major roads on quiet hazy nights', 
    'The quick brown fox jumps over the lazy dog',
    'Grumpy wizards make toxic brew for the evil queen and jack', 
    'A quick movement of the enemy will jeopardize six gunboats']
  
    # Give random words for testing the speed of user
    word = random.randint(0, (len(words)-1))
   
    # use label method of tkinter for labling in window
    wordToType = Label(window, text=words[word], font="times 20")
    wordToType.place(x=20, y=10)
    # place of labeling in window

    directions = Label(window, text="Type here:", font="times 16")
    directions.place(x=80, y=80)

    inputStr = StringVar()
    entry = Entry(window, textvariable=inputStr)
    entry.place(x=180, y=85, width = 350)
    
    inputStr.trace_add('write',checkInput)

    restartButton = Button(window, text="Try Again", command=reset, width=12, bg='grey')
    restartButton.place(x=550, y=80)

    userSpeed = Label(window, text="User Speed: ", font="times 12")
    userSpeed.place(x=10,y=150)

    userAcc = Label(window, text="Accuracy: ", font="times 12")
    userAcc.place(x=10,y=190)

    wpmSpeed = Label(window, text="Words Per Minute: ", font="times 12")
    wpmSpeed.place(x=10,y=170)

    window.mainloop()

# start game    
game()