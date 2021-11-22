import tkinter as tk
import ipaddress

def conv_addr():
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

def del_value():
    '''Удаление содержимого поля'''
    return address_entry.delete(0, tk.END)

def columnconf(index,size):
    '''Функция размера колонок'''
    return win.grid_columnconfigure(index, minsize = size)

def rowconf(index,size):
    '''Функция размера рядов'''
    return win.grid_rowconfigure(index, minsize = size)

win = tk.Tk()
win.title('Converting IPv4 address')
win.geometry('300x300')
win.resizable(False, False)

address_entry = tk.Entry(win, font=('Calibri', 15),bd = 4)
address_entry.grid(column=0, row=0, columnspan=2, sticky='wens')

convert_button = tk.Button(win, text='Convert your address', command=conv_addr).grid(column=0, row=1, ipadx=5, ipady=5)
delete_button = tk.Button(win, text='Delete content field', command=del_value).grid(column=1, row=1, ipadx=5, ipady=5)

label_result = tk.Label(win, font = ('Calibri',12))
label_result.grid(column=0, row=2, columnspan=2, sticky='wens')

columnconf(0,150)
columnconf(1,150)

rowconf(0,50)
rowconf(1,100)
rowconf(2,150)

win.mainloop()
