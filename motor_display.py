from tkinter import*
import json

with open("imu_data.json", 'r') as f:
    data = json.load(f)

#Create new window
root = Tk()
root.geometry("1000x1000")
w = Canvas(root, width=1000, height=1000)
w.pack()


def update(time):
    testtactors=data[time]['signal_list']
    if testtactors[0] == 1:
        w.create_oval(500, 200, 550, 250, outline='red', fill='red')
    else:
        w.create_oval(500, 200, 550, 250, outline='black', fill='black')
    if testtactors[1] == 1:
        w.create_oval(614, 223, 664, 273, outline='red', fill='red')
    else:
        w.create_oval(614, 223, 664, 273, outline='black', fill='black')
    if testtactors[2] == 1:
        w.create_oval(712, 288, 762, 338, outline='red', fill='red')
    else:
        w.create_oval(712, 288, 762, 338, outline='black', fill='black')
    if testtactors[3] == 1:
        w.create_oval(777, 386, 827, 436, outline='red', fill='red')
    else:
         w.create_oval(777, 386, 827, 436, outline='black', fill='black')
    if testtactors[4] == 1:
        w.create_oval(800, 500, 850, 550, outline='red', fill='red')
    else:
        w.create_oval(800, 500, 850, 550, outline='black', fill='black')
    if testtactors[5] == 1:
        w.create_oval(777, 614, 827, 664, outline='red', fill='red')
    else:
        w.create_oval(777, 614, 827, 664, outline='black', fill='black')
    if testtactors[6] == 1:
        w.create_oval(712, 712, 762, 762, outline='red', fill='red')
    else:
        w.create_oval(712, 712, 762, 762, outline='black', fill='black')
    if testtactors[7] == 1:
        w.create_oval(614, 777, 664, 827, outline='red', fill='red')
    else:
        w.create_oval(614, 777, 664, 827, outline='black', fill='black')
    if testtactors[8] == 1:
        w.create_oval(500, 800, 550, 850, outline='red', fill='red')
    else:
        w.create_oval(500, 800, 550, 850, outline='black', fill='black')
    if testtactors[9] == 1:
        w.create_oval(386, 777, 436, 827, outline='red', fill='red')
    else:
        w.create_oval(386, 777, 436, 827, outline='black', fill='black')
    if testtactors[10] == 1:
        w.create_oval(288, 712, 338, 762, outline='red', fill='red')
    else:
        w.create_oval(288, 712, 338, 762, outline='black', fill='black')
    if testtactors[11] == 1:
        w.create_oval(223, 614, 273, 664, outline='red', fill='red')
    else:
        w.create_oval(223, 614, 273, 664, outline='black', fill='black')
    if testtactors[12] == 1:
        w.create_oval(200, 500, 250, 550, outline='red', fill='red')
    else:
        w.create_oval(200, 500, 250, 550, outline='black', fill='black')
    if testtactors[13] == 1:
        w.create_oval(223, 386, 273, 436, outline='red', fill='red')
    else:
        w.create_oval(223, 386, 273, 436, outline='black', fill='black')
    if testtactors[14] == 1:
        w.create_oval(288, 288, 338, 338, outline='red', fill='red')
    else:
        w.create_oval(288, 288, 338, 338, outline='black', fill='black')
    if testtactors[15] == 1:
        w.create_oval(386, 223, 436, 273, outline='red', fill='red')
    else:
        w.create_oval(386, 223, 436, 273, outline='black', fill='black')
        

    root.after(100, update, time+1)



update(0)

root.mainloop()
