import ipaddress
import tkinter as tk

def del_value():
    '''Удаление содержимого поля'''
    return address_entry.delete(0, tk.END)

def columnconf(index,size):
    '''Функция размера колонок'''
    return win.grid_columnconfigure(index, minsize=size)

def rowconf(index,size):
    '''Функция размера рядов'''
    return win.grid_rowconfigure(index, minsize=size)

def conv_hex_system():
    '''Функция конвертации адреса в шестнадцатеричную систему'''
    address = address_entry.get()
    result = []
    try:
        address = str(ipaddress.ip_address(address))
        func_ch_add = lambda x: x.split(sep='.')
        temp = [hex(int(elem))[2:] for elem in func_ch_add(address)]
        for elem in temp:
            if len(elem) < 2:
                while len(elem) != 2:
                    elem = '0' + elem
                result.append(elem)
            elif len(elem) == 2:
                result.append(elem)
        address = '.'.join(result)
        label_result['text']= f'Your address is \n{address}'
    except ValueError:
        label_result['text']='Введите корректный адрес'

def conv_bin_system():
    '''Функция конвертации адреса в двоичную систему'''
    address = address_entry.get()
    result = []
    try:
        address = str(ipaddress.ip_address(address))
        func_ch_add = lambda x: x.split(sep='.')
        temp = [bin(int(elem))[2:] for elem in func_ch_add(address)]
        for elem in temp:
            if len(elem) < 8:
                while len(elem) != 8:
                    elem = '0' + elem
                result.append(elem)
            elif len(elem) == 8:
                result.append(elem)
        address = '.'.join(result)
        label_result['text']= f'Your address is \n{address}'
    except ValueError:
        label_result['text']='Введите корректный адрес'

def select_num_system():
    num_system = int_value.get()
    if num_system == 2:
        conv_bin_system()
    else:
        conv_hex_system()

win = tk.Tk()
win.title('Converting IPv4 address')
win.geometry('300x300')
win.resizable(False, False)

int_value = tk.IntVar()

address_entry = tk.Entry(win, font=('Calibri', 15),bd = 4)
address_entry.grid(column=0, row=0, columnspan=2, sticky='wens')

radiobutton_bin = tk.Radiobutton(win, text='to double system',variable=int_value, value=2, command=select_num_system, cursor="cross")
radiobutton_bin.grid(column=0,row=1)

radiobutton_hex = tk.Radiobutton(win, text='to hex system',variable=int_value, value=16, command=select_num_system, cursor="cross")
radiobutton_hex.grid(column=1, row=1)

delete_button = tk.Button(win, text='Delete content field', command=del_value)
delete_button.grid(column=0, row=2, columnspan=2,ipadx=5, ipady=5)

label_result = tk.Label(win, font = ('Calibri',12),bg='gray')
label_result.grid(column=0, row=3, columnspan=2, sticky='wens', pady=20)

columnconf(0, 150)
columnconf(1, 150)

rowconf(0, 50)
rowconf(1, 50)
rowconf(2, 50)
rowconf(3, 170)

win.mainloop()