
from tkinter import *
from threading import Thread
from time import sleep

def gotoPosition(oldPosition, newPosition):
   
    startingX = oldPosition[0]
    startingY = oldPosition[1]
    endingX = newPosition[0]
    endingY = newPosition[1] 
    
    print('Starting X = ' + str(startingX))
    print('Starting Y = ' + str(startingY))
    print('Ending X = ' + str(endingX))
    print('Ending Y = ' + str(endingY))
    
    
    diffX = endingX - startingX
    diffY = endingY - startingY   
    x = startingX
    y = startingY
    circleSize = 4
    
    c.create_oval(x-circleSize, y-circleSize, x+circleSize, y+circleSize, fill='red')
    
    reachX = 0
    reachY = 0
    while reachX == 0 or reachY == 0:
        
        if diffX < 0: 
            if x <= endingX:
                reachX = 1
            else: 
                x -= 1
        elif diffX > 0:
            if x >= endingX:
                reachX = 1
            else: 
                x += 1
        else:
            reachX = 1
            
        if diffY < 0:  
            if y <= endingY:
                reachY = 1
            else:
                y -= 1
        elif diffY > 0:  
            if y >= endingY:
                reachY = 1
            else:
                y += 1
        else:
            reachY = 1  
                      
        dispX.set("X = " + str(x))
        dispY.set("Y = " + str(y))
        c.create_oval(x-circleSize, y-circleSize, x+circleSize, y+circleSize, fill='red')
        sleep(.001)

def runSnake():
    # Creates snake motion 
    # Assumes everything starts at (0,0)
    oldX = 0
    oldY = 0
    for y in range(512):
        x = 0
        for x in range(512):
            
            if y % 2 == 0:
                gotoPosition([oldX, oldY], [x,y])
                oldX = x
            else:
                leftX = 512 - x
                gotoPosition([oldX, oldY], [leftX,y])
                oldX = leftX
                
        oldY = y
    
    
    
    
def threaded_function():
    
    gotoPosition([256,512], [0,0])
    runSnake()
    

        
if __name__ == "__main__":

    thread1 = Thread(target = threaded_function)
    
    root = Tk()
    root.title('Main Window')
    root.geometry("300x150")
    changingText = StringVar()
    changingText.set("\n")
    labelText = Label(root, textvariable = changingText)
    labelText.pack()
    
    dispX = StringVar()
    dispX.set("X = ")
    xLabelText = Label(root, textvariable = dispX)
    xLabelText.pack()
    dispY = StringVar()
    dispY.set("Y = ")
    yLabelText = Label(root, textvariable = dispY)
    yLabelText.pack()

    second_window = Toplevel()
    second_window.title('Second window') 
    second_window.geometry("550x550")
    c = Canvas(second_window, height=512, width=512, bg='white')
    c.pack(fill=NONE, expand=True)

      
    thread1.start()
    root.mainloop()
    
    
    print("thread finished...exiting")