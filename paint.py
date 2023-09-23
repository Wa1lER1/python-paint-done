import tkinter as tk

root = tk.Tk()
root.geometry("300x370")
root.title("Paint app")

color = "#00FF00"
draw = False

wide_x = 5
wide_y = 5

cnv = tk.Canvas(root, bg="white", height=300, width=300)
cnv.place(x=0, y=0)

f1 = tk.Text(root, height=1, width=10)
f1.place(x=90, y=310)

def change_color():
	global color
	global wide_x
	global wide_y
	color = f1.get('1.0', tk.END)[0:7]
	wide_x = 5
	wide_y = 5
	cnv_color.create_rectangle(0, 0, 20, 20, fill=color, outline='')

f_btn = tk.Button(text='Change', command=change_color)
f_btn.place(x=190, y=307)

def clean_all():
	cnv.create_rectangle(0, 0, 300, 300, fill='#FFFFFF', outline='')
	
f_btn_clean = tk.Button(text='Clean all', command=clean_all)
f_btn_clean.place(x=70, y=337)

def erase_set():
	global wide_x
	global wide_y
	global color

	wide_x = 10
	wide_y = 10
	color = '#FFFFFF'
	cnv_color.create_rectangle(0, 0, 20, 20, fill=color, outline='')

f_btn_erase = tk.Button(text='Erase', command=erase_set)
f_btn_erase.place(x=160, y=337)

def motion(event):
	if draw:
		x, y = event.x, event.y
		cnv.create_rectangle(x, y, x+wide_x, y+wide_y, fill=color, outline='')

def draw_flag(event):
	global draw
	if draw:
		draw = False
	else:
		draw = True

cnv_color = tk.Canvas(root, bg="white", height=20, width=20)
cnv_color.place(x=50, y=308)
cnv_color.create_rectangle(0, 0, 20, 20, fill=color, outline='')

root.bind('<Motion>', motion)
root.bind('q', draw_flag)		

root.mainloop()

