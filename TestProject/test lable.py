import tkinter as tk
from tkinter import *
from datetime import datetime
HEIGH=700
WIDTH=700

root = tk.Tk()
#root.attributes('-fullscreen', True)  ##ให้เต็มจอ
canvas = tk.Canvas(root,height=HEIGH , width=WIDTH)
canvas.pack()

background_image= tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#nnn= tk.font(fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold")
#frame = tk.Frame(root)
frame = tk.Frame(root,bg='Blue')
frame.place(relx=0.01, rely=0.25, relwidth=0.75, relheight=0.5)

#helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)



##window = Tk()
#window.title('Clock')
#window.geometry('200x60')

lb_clock = Label(font='Impact 30 bold')
lb_clock.place(relx=0.18, rely=0.15,)

def tick():
    global curtime
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')
    lb_clock.config(text=ftime)
    lb_clock.after(1000, tick)      #ให้เรียกฟังก์ชันตัวมันเองทุก 1 วินาที

tick()          #เรียกฟังก์ชันขึ้นมาทำงานครั้งแรก



##button1 = tk.Button(frame, text="1.ตรวจแบบ/เขียนแบบ", fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold")
##button1.place(relx=0, rely=0, relwidth=1, relheight=0.9999)

label = tk.Label(root, text='ใส่ตัววิ่งด้านล่าง', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 40 bold ")
label.place(relx=0.0, rely=0.535, relwidth=1, relheight=0.063)
label = tk.Label(root, text='ใส่ตัววิ่งด้านล่าง', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 40 bold ")
label.place(relx=0.0, rely=0.935, relwidth=1, relheight=0.063)

root.mainloop()