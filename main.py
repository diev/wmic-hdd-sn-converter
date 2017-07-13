#! WMIC HDD SN Converter
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import re


def conv_and_copy():
    check_input(switch=1)


def just_conv():
    check_input(switch=0)


def check_input(switch):
    try:
        to_dec = str(whats_decode.get())
        dec_res = bytearray.fromhex(to_dec).decode()
        dec_len = len(dec_res)
        if dec_len <= 1:
            messagebox.showinfo('Information', 'Too short for WMIC HDD SN, try again')
        else:
            convert(dec_res, dec_len, switch)
    except ValueError:
        messagebox.showinfo('Information', 'Please input HEX value')


def convert(dec_res, dec_len, switch):
    ltr1 = 0
    ltr2 = 2
    dec_changed = []

    for count in range(dec_len):
        if ltr1 >= dec_len:
            break
        two_ltr = dec_res[ltr1:ltr2:1]
        a = two_ltr[0]
        b = two_ltr[1]
        mix_res = b, a
        dec_changed.append(mix_res)

        ltr1 += 2
        ltr2 += 2

    dec_changed = str(dec_changed).strip('[]')
    dec_changed = re.sub(r'\(', '', dec_changed)  # (
    dec_changed = re.sub(r'\)', '', dec_changed)  # )
    dec_changed = re.sub(r'\'', '', dec_changed)  # '
    dec_changed = re.sub(r',', '', dec_changed)  # ,
    dec_changed = re.sub(r' ', '', dec_changed)  # space

    if switch == 1:
        root.clipboard_clear()
        root.clipboard_append(dec_changed)
        root.update()

    view_res(dec_changed)


def view_res(dec_changed):
    result_dec_entry = Entry()
    result_dec_entry.insert(0, dec_changed)
    result_dec_entry.configure(state='readonly')
    result_dec_entry.place(relx=.1, rely=.6, height=25, width=230)


def destr_progr():
    root.destroy()


root = Tk()
root.title("WMIC HDD SN Converter")
root.geometry("300x300+50+50")

help_label = Label(text="Enter WMIC disk drive serial number")
help_label.place(relx=.08, rely=.0, height=60, width=250)
whats_decode = StringVar()
whats_decode_entry = Entry(textvariable=whats_decode)
whats_decode_entry.place(relx=.1, rely=.14, height=25, width=230)

conv_but = Button(text='Convert and copy to clipboard', height=1, width=20, command=conv_and_copy)
conv_but.place(relx=.1, rely=.24, height=25, width=230)
conv_but = Button(text='Just convert', height=1, width=20, command=just_conv)
conv_but.place(relx=.1, rely=.34, height=25, width=230)

view_label = Label(text="Result:")
view_label.place(relx=.07, rely=.52, height=30, width=250)
result_dec_entry = Entry()
result_dec_entry.configure(state='readonly')
result_dec_entry.place(relx=.1, rely=.6, height=25, width=230)
exit_but = Button(text='Exit', height=1, width=20, command=destr_progr)
exit_but.place(relx=.4, rely=.7, height=25, width=50)

root.mainloop()
