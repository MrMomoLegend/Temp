from tkinter import *
def drpdwn():

	root = Tk()

	root.geometry("200x200")

	def show1():
		label.config(text=clicked.get())
		root.destroy()

	options = [
		"add",
		"subraction",
		"multiplication"
	]

	clicked = StringVar()

	clicked.set("Select")

	drop = OptionMenu(root, clicked, *options)
	drop.pack()

	button = Button(root, text="click Me", command=show1).pack()

	label = Label(root, text=" ")
	label.pack()

	root.mainloop()
	return clicked.get()

