import tkinter as tk
from tkinter import ttk
import pandas as pd

# Base Window
root = tk.Tk()
root.title('리듬 끝말잇기')
root.geometry('800x400')
root.resizable(False, False)

# List of fonts
font1 = ('여기어때 잘난체', 24)

# Table Headers
tree = ttk.Treeview(
    root, 
    columns=('title', 'composer', 'time', 'game', 'section'), 
    displaycolumns=('title', 'time', 'game', 'section'), 
    show='headings', 
    selectmode='browse'
    )
tree.column('title', width=250)
tree.column('time', width=50)
tree.column('game', width=70)
tree.column('section', width=200)
tree.heading('title', text='제목', anchor='w')
tree.heading('time', text='시간', anchor='w')
tree.heading('game', text='수록', anchor='w')
tree.heading('section', text='목차', anchor='w')

# Song list
songlist = pd.read_excel('list.xlsx').values.tolist()
for item in songlist:
    tree.insert('', tk.END, values=(item[0], item[1], "{}:{:02}".format(item[2], item[3]), item[4], item[5]))

# Placing widgets on the base window
tree.grid(row=0, column=0, sticky='nswe', padx=(10, 0), pady=(10, 0))

scroll = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scroll.set)
scroll.grid(row=0, column=1, sticky='ns')

root.mainloop()