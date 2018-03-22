


from Tkinter import*


class RN():
	called=1

	def __init__(self,projectName,add_or_del):
		if RN.called:
			self.Console_Area()

	def hide(self):
    		self.withdraw()

	def Console_Area(self):
		RN.called=0
		RN.window = Toplevel()
		menu = Menu(RN.window)
		RN.window.title("Raw Data Area")

		#window.configure(menu = menu)
		RN.window.geometry('800x100')


		###### Icon for the main window ######
		winIcon = PhotoImage(file = 'shark.gif')
		RN.window.tk.call('wm', 'iconphoto', RN.window._w, winIcon)

		##### Labels for the Workspace and Projects #####
		Lbl_4digit_1 = Label(RN.window, text="0000", fg="Black", font="none 11")
		Lbl_4digit_1.grid(row = 0,column = 0,columnspan = 1,sticky = W)

		Lbl_4digit_2 = Label(RN.window, text="0000", fg="Black", font="none 11")
		Lbl_4digit_2.grid(row = 1,column = 0,columnspan = 1,sticky = W)

		Lbl_4digit_3 = Label(RN.window, text="0000", fg="Black", font="none 11")
		Lbl_4digit_3.grid(row = 2,column = 0,columnspan = 1,sticky = W)


		######################################################################################

		Lbl_space_1 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_1.grid(row = 0,column = 5,columnspan = 1,sticky = W)

		Lbl_space_2 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_2.grid(row = 1,column = 5,columnspan = 1,sticky = W)

		Lbl_space_3 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_3.grid(row = 2,column = 5,columnspan = 1,sticky = W)

		######################################################################################



		Lbl_2digit_1 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_1.grid(row = 0,column = 6,columnspan = 1,sticky = W)

		Lbl_2digit_2 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_2.grid(row = 1,column = 6,columnspan = 1,sticky = W)

		Lbl_2digit_3 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_3.grid(row = 2,column = 6,columnspan = 1,sticky = W)



		Lbl_2digit_4 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_4.grid(row = 0,column = 7,columnspan = 1,sticky = W)

		Lbl_2digit_5 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_5.grid(row = 1,column = 7,columnspan = 1,sticky = W)

		Lbl_2digit_6 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_6.grid(row = 2,column = 7,columnspan = 1,sticky = W)



		Lbl_2digit_7 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_7.grid(row = 0,column = 8,columnspan = 1,sticky = W)

		Lbl_2digit_8 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_8.grid(row = 1,column = 8,columnspan = 1,sticky = W)

		Lbl_2digit_9 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_9.grid(row = 2,column = 8,columnspan = 1,sticky = W)



		Lbl_2digit_10 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_10.grid(row = 0,column = 9,columnspan = 1,sticky = W)

		Lbl_2digit_11 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_11.grid(row = 1,column = 9,columnspan = 1,sticky = W)

		Lbl_2digit_12 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_12.grid(row = 2,column = 9,columnspan = 1,sticky = W)



		Lbl_2digit_13 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_13.grid(row = 0,column = 10,columnspan = 1,sticky = W)

		Lbl_2digit_14 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_14.grid(row = 1,column = 10,columnspan = 1,sticky = W)

		Lbl_2digit_15 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_15.grid(row = 2,column = 10,columnspan = 1,sticky = W)



		Lbl_2digit_15 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_15.grid(row = 0,column = 11,columnspan = 1,sticky = W)

		Lbl_2digit_16 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_16.grid(row = 1,column = 11,columnspan = 1,sticky = W)

		Lbl_2digit_17 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_17.grid(row = 2,column = 11,columnspan = 1,sticky = W)



		Lbl_2digit_18 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_18.grid(row = 0,column = 12,columnspan = 1,sticky = W)

		Lbl_2digit_19 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_19.grid(row = 1,column = 12,columnspan = 1,sticky = W)

		Lbl_2digit_20 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_20.grid(row = 2,column = 12,columnspan = 1,sticky = W)



		Lbl_2digit_21 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_21.grid(row = 0,column = 13,columnspan = 1,sticky = W)

		Lbl_2digit_22 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_22.grid(row = 1,column = 13,columnspan = 1,sticky = W)

		Lbl_2digit_23 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digit_23.grid(row = 2,column = 13,columnspan = 1,sticky = W)



		########################################################################################

		Lbl_space_4 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_4.grid(row = 0,column = 14,columnspan = 1,sticky = W)

		Lbl_space_5 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_5.grid(row = 1,column = 14,columnspan = 1,sticky = W)

		Lbl_space_6 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_6.grid(row = 2,column = 14,columnspan = 1,sticky = W)

		########################################################################################




		Lbl_2digi_1 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_1.grid(row = 0,column = 15,columnspan = 1,sticky = W)

		Lbl_2digi_2 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_2.grid(row = 1,column = 15, columnspan = 1,sticky = W)

		Lbl_2digi_3 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_3.grid(row = 2,column = 15,columnspan = 1,sticky = W)



		Lbl_2digi_4 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_4.grid(row = 0,column = 16,columnspan = 1,sticky = W)

		Lbl_2digi_5 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_5.grid(row = 1,column = 16,columnspan = 1,sticky = W)

		Lbl_2digi_6 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_6.grid(row = 2,column = 16,columnspan = 1,sticky = W)



		Lbl_2digi_7 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_7.grid(row = 0,column = 17,columnspan = 1,sticky = W)

		Lbl_2digi_8 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_8.grid(row = 1,column = 17,columnspan = 1,sticky = W)

		Lbl_2digi_9 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_9.grid(row = 2,column = 17,columnspan = 1,sticky = W)



		Lbl_2digi_10 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_10.grid(row = 0,column = 18,columnspan = 1,sticky = W)

		Lbl_2digi_11 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_11.grid(row = 1,column = 18,columnspan = 1,sticky = W)

		Lbl_2digi_12 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_12.grid(row = 2,column = 18,columnspan = 1,sticky = W)



		Lbl_2digi_13 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_13.grid(row = 0,column = 19,columnspan = 1,sticky = W)

		Lbl_2digi_14 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_14.grid(row = 1,column = 19,columnspan = 1,sticky = W)

		Lbl_2digi_15 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_15.grid(row = 2,column = 19,columnspan = 1,sticky = W)



		Lbl_2digi_15 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_15.grid(row = 0,column = 20,columnspan = 1,sticky = W)

		Lbl_2digi_16 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_16.grid(row = 1,column = 20,columnspan = 1,sticky = W)

		Lbl_2digi_17 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_17.grid(row = 2,column = 20,columnspan = 1,sticky = W)



		Lbl_2digi_18 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_18.grid(row = 0,column = 21,columnspan = 1,sticky = W)

		Lbl_2digi_19 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_19.grid(row = 1,column = 21,columnspan = 1,sticky = W)

		Lbl_2digi_20 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_20.grid(row = 2,column = 21,columnspan = 1,sticky = W)



		Lbl_2digi_21 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_21.grid(row = 0,column = 22,columnspan = 1,sticky = W)

		Lbl_2digi_22 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_22.grid(row = 1,column = 22,columnspan = 1,sticky = W)

		Lbl_2digi_23 = Label(RN.window, text="00", fg="Black", font="none 11")
		Lbl_2digi_23.grid(row = 2,column = 22,columnspan = 1,sticky = W)



		##################################################################################

		Lbl_space_7 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_7.grid(row = 0,column = 23,columnspan = 1,sticky = W)

		Lbl_space_8 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_8.grid(row = 1,column = 23,columnspan = 1,sticky = W)

		Lbl_space_9 = Label(RN.window, text="  ", fg="Black", font="none 11")
		Lbl_space_9.grid(row = 2,column = 23,columnspan = 1,sticky = W)

		##################################################################################




		Lbl_2dig_1 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_1.grid(row = 0,column = 24,columnspan = 1,sticky = W)

		Lbl_2dig_2 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_2.grid(row = 1,column = 24, columnspan = 1,sticky = W)

		Lbl_2dig_3 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_3.grid(row = 2,column = 24,columnspan = 1,sticky = W)



		Lbl_2dig_4 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_4.grid(row = 0,column = 25,columnspan = 1,sticky = W)

		Lbl_2dig_5 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_5.grid(row = 1,column = 25,columnspan = 1,sticky = W)

		Lbl_2dig_6 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_6.grid(row = 2,column = 25,columnspan = 1,sticky = W)



		Lbl_2dig_7 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_7.grid(row = 0,column = 26,columnspan = 1,sticky = W)

		Lbl_2dig_8 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_8.grid(row = 1,column = 26,columnspan = 1,sticky = W)

		Lbl_2dig_9 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_9.grid(row = 2,column = 26,columnspan = 1,sticky = W)



		Lbl_2dig_10 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_10.grid(row = 0,column = 27,columnspan = 1,sticky = W)

		Lbl_2dig_11 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_11.grid(row = 1,column = 27,columnspan = 1,sticky = W)

		Lbl_2dig_12 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_12.grid(row = 2,column = 27,columnspan = 1,sticky = W)



		Lbl_2dig_13 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_13.grid(row = 0,column = 28,columnspan = 1,sticky = W)

		Lbl_2dig_14 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_14.grid(row = 1,column = 28,columnspan = 1,sticky = W)

		Lbl_2dig_15 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_15.grid(row = 2,column = 28,columnspan = 1,sticky = W)



		Lbl_2dig_15 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_15.grid(row = 0,column = 29,columnspan = 1,sticky = W)

		Lbl_2dig_16 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_16.grid(row = 1,column = 29,columnspan = 1,sticky = W)

		Lbl_2dig_17 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_17.grid(row = 2,column = 29,columnspan = 1,sticky = W)



		Lbl_2dig_18 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_18.grid(row = 0,column = 30,columnspan = 1,sticky = W)

		Lbl_2dig_19 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_19.grid(row = 1,column = 30,columnspan = 1,sticky = W)

		Lbl_2dig_20 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_20.grid(row = 2,column = 30,columnspan = 1,sticky = W)



		Lbl_2dig_21 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_21.grid(row = 0,column = 31,columnspan = 1,sticky = W)

		Lbl_2dig_22 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_22.grid(row = 1,column = 31,columnspan = 1,sticky = W)

		Lbl_2dig_23 = Label(RN.window, text=".", fg="Black", font="none 11")
		Lbl_2dig_23.grid(row = 2,column = 31,columnspan = 1,sticky = W)
