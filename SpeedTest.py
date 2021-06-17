#test
# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

# creating window using gui
window = Tk()
  
# the size of the window is defined
window.geometry("850x230")

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
        if len(entry.get()) == len(words[word]):
  
            # here start time is when the window
            # is opened and end time is when
            # window is destroyed
            end = timer()

            # we deduct the start time from end
            # time and calculate results using
            # timeit function
            LIM = 5
            time = end-start
            time_for_speed = end-start
            time = str(end-start)[:LIM]
            time += "s"

            speed = Label(window, text=time, font="times 12")
            speed.place(x=100, y=150)
            print(time)

            numRight = 0
            for i in range(len(words[word])):
                if words[word][i] == entry.get()[i]:
                    numRight += 1
            accuracy = numRight/(len(words[word]))*100
            accuracy = str(accuracy)[:LIM]
            accuracy += "%"
            acc = Label(window, text = accuracy, font="times 12")
            acc.place(x=250,y=150)
            print("Accuracy:",accuracy)

            wPm = 0
            numWords = 1
            for i in range(len(words[word])):
                if(words[word][i].isspace()):
                    numWords=numWords+1
            wPm = time_for_speed / numWords
            wPm = wPm / 60
            wPm = str(wPm)[:LIM]
            speedz = Label(window, text = wPm, font="times 12")
            speedz.place(x=120,y=170)
            print("WPM:",wPm)
            
        else:
            print("Wrong Input")
    
    def reset():

        print("reset")

    words = ['Quizzical twins proved my hijack-bug fix.', 'Waxy and quivering, jocks fumble the pizza.', 'Sympathizing would fix Quaker objectives.',
             'Watch “Jeopardy!”, Alex Trebek’s fun TV quiz game.', 'Few black taxis drive up major roads on quiet hazy nights.', 'The quick brown fox jumps over the lazy dog',
             'Grumpy wizards make toxic brew for the evil queen and jack.', 'A quick movement of the enemy will jeopardize six gunboats.']
  
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
        if len(entry.get()) == len(words[word]):
            #print("Match!")
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

    userAcc = Label(window, text="Accuracy: ", font="times 12")
    userAcc.place(x=10,y=190)

    wpmSpeed = Label(window, text="Words Per Minute: ", font="times 12")
    wpmSpeed.place(x=10,y=170)


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
