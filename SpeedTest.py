
# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

import keyboard

# creating window using gui
window = Tk()
  
# the size of the window is defined
window.geometry("450x200")

x = 0
  
# defining the function for the test
def game():
    '''
    global x
    # defining function for results of test
    if x != 0:
        x2.pack_forget()
        x = x+1
        '''
    def check_result():
        if entry.get() == words[word]:
  
            # here start time is when the window
            # is opened and end time is when
            # window is destroyed
            end = timer()
  
            # we deduct the start time from end
            # time and calculate results using
            # timeit function
            LIM = 4
            time = end-start
            time = str(end-start)[:LIM]
            
            t = Label(window, text=time, font="times 12")
            t.place(x=100, y=150)
            print(time)
        else:
            print("Wrong Input")
    
    def reset():

        print("reset")

    words = ['programming', 'coding', 'algorithm',
             'systems', 'python', 'software']
  
    # Give random words for testing the speed of user
    word = random.randint(0, (len(words)-1))
  
    # start timer using timeit function
    start = timer()
    
    #windows = Tk()
    #windows.geometry("450x200")
  
    # use lable method of tkinter for labling in window
    x2 = Label(window, text=words[word], font="times 20")
  
    # place of labling in window
    x2.place(x=150, y=10)
    x3 = Label(window, text="Start Typing", font="times 20")
    x3.place(x=10, y=50)

    def checkInput(var, indx, mode):
        if entry.get() == words[word]:
            print("Match!")
            check_result()
    
    inputStr = StringVar()
    entry = Entry(window, textvariable=inputStr)
    entry.place(x=280, y=55)
     
    inputStr.trace_add('write',checkInput)
    '''
    # buttons to submit output and check results
    b2 = Button(window, text="Done",
                command=check_result, width=12, bg='grey')
    b2.place(x=150, y=100)
    '''
    def reset():
        x2.destroy()
        entry.destroy()
        game()
    
    b3 = Button(window, text="Try Again", 
                command=reset, width=12, bg='grey')
    b3.place(x=250, y=100)

    userSpeed = Label(window, text="User Speed: ", font="times 12")
    userSpeed.place(x=10,y=150)


    window.mainloop()
    

  
'''  
x1 = Label(window, text="Lets start playing..", font="times 20")
x1.place(x=10, y=50)
  
b1 = Button(window, text="Go", command=game, width=12, bg='grey')
b1.place(x=150, y=100)
'''
game()
# calling window
#window.mainloop()