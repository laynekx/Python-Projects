from tkinter import *

def button_clicked():
    user_temp = float(user_input.get())
    if radio_state.get() == 1:
        temp_convert = round((user_temp*(9/5)+32), 1)
        temp.config(text=f"{temp_convert}°F")
    else:
        temp_convert = round(((user_temp-32)/(1.8)),1)
        temp.config(text=f"{temp_convert}°C")
    
window = Tk()
window.title("Temperature Converter")
window.config(padx=20, pady=20)

equal = Label(text="is equal to")
equal.grid(column=2, row=0)

user_input = Entry(width=7)
user_input.grid(column=0, row=0)

temp = Label(text="0")
temp.grid(column=3, row=0)

radio_state = IntVar()
radio_state.set("1")
radiobutton1 = Radiobutton(text="to °F", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="to °C", value=2, variable=radio_state)
radiobutton1.grid(column=1, row=1)
radiobutton2.grid(column=1, row=2)

button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=3)

convert = Label(text="°C/°F")
convert.grid(column=1, row=0)

window.mainloop()


