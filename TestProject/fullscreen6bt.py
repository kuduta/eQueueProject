import tkinter as tk


HEIGH=700
WIDTH=700

root = tk.Tk()
root.attributes('-fullscreen', True)  ##ให้เต็มจอ
canvas = tk.Canvas(root,height=HEIGH , width=WIDTH)
canvas.pack()

background_image= tk.PhotoImage(file='./landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#nnn= tk.font(fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold")
#frame = tk.Frame(root)
frame = tk.Frame(root,bg='Blue')
frame.place(relx=0.12, rely=0.18, relwidth=0.75, relheight=0.75)

#helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
button1 = tk.Button(frame, text="1.ตรวจแบบ/เขียนแบบ", fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold")
button1.place(relx=0, rely=0, relwidth=1, relheight=0.160)
button2 = tk.Button(frame, text='2.รับชำระ', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold ")
button2.place(relx=0, rely=0.1683, relwidth=1, relheight=0.160)
button3 = tk.Button(frame, text='3.ขอเลขประจำตัวผู้เสียภาษี', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold ")
button3.place(relx=0, rely=0.3366, relwidth=1, relheight=0.160)
button4 = tk.Button(frame, text='4.จดทะเบียนภาษีมูลค่าเพิ่ม', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold ")
button4.place(relx=0, rely=0.5049, relwidth=1, relheight=0.160)
button5 = tk.Button(frame, text='5.ติดต่องานสำรวจ/เร่งรัดฯ', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold ")
button5.place(relx=0, rely=0.6732, relwidth=1, relheight=0.160)
button6 = tk.Button(frame, text='6.อื่นๆ', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 50 bold ")
button6.place(relx=0, rely=0.8415, relwidth=1, relheight=0.160)


label = tk.Label(root, text='ใส่ตัววิ่งด้านล่าง', fg = "#ffffff",bg = "#306eff",font = "AngsanaUPC 40 bold ")
label.place(relx=0.0, rely=0.935, relwidth=1, relheight=0.063)

root.mainloop()