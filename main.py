from faulthandler import disable
import tkinter as tk
from tkinter import Frame, ttk
from turtle import width
from typing import Container
import pandas as pd

# Base Window (Object Oriented)
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Initialization
        self.title('리듬 끝말잇기')
        self.geometry('800x400')
        self.resizable(False, False)

        # Widget Initialization
        self.init_font()
        self.read_songlist()
        self.init_songlist()
        self.reset_songlist()
        self.init_gamelist()

    # List of fonts
    def init_font(self):
        self.font1 = ('여기어때 잘난체', 24)

    # Song list
    def read_songlist(self):
        songlist = pd.read_excel('list.xlsx').values.tolist()
        self.baseSL = []
        
        for item in songlist:
            if '있' in item[7] and item[3] * 60 + item[4] <= 180:
                self.baseSL.append((item[0], item[1], item[2],
                    '{}:{:02}'.format(item[3], item[4]), item[5], item[6],
                    item[8], item[9]))

    def init_songlist(self):
        self.table = ttk.Treeview(
            self,
            columns=('title', 'search', 'composer', 'time',
                'game', 'section', 'start', 'end'),
            displaycolumns=('title', 'time', 'game'),
            show='headings',
            selectmode='browse'
        )
        self.table.column('title', width=250)
        self.table.column('time', width=40)
        self.table.column('game', width=80)
        self.table.heading('title', text='곡명', anchor='w')
        self.table.heading('time', text='시간', anchor='w')
        self.table.heading('game', text='수록 게임', anchor='w')

        self.table.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky='nwse')
        scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, pady=(10, 0), sticky='ns')
    
    def reset_songlist(self):
        self.currentSL = self.baseSL
        self.table.delete(*self.table.get_children())
        for item in self.currentSL:
            self.table.insert('', tk.END, values=item)
        #self.update()

    def init_gamelist(self):
        listContainer = Frame(self)

        self.gamelist = ttk.Combobox(listContainer)
        self.gamelist['state'] = 'readonly'

        games = []
        for item in self.baseSL:
            if item[4] not in games:
                games.append(item[4])
        games.insert(0, '전체 게임')
        self.gamelist['values'] = games
        self.gamelist.current(0)

        self.sectionlist = ttk.Combobox(listContainer)
        self.sectionlist['state'] = 'disable'

        self.gamelist.pack(side='left', expand=True, fill=tk.X)
        self.sectionlist.pack(side='left', expand=True, fill=tk.X, padx=(10, 0))
        listContainer.grid(row=1, column=0, columnspan=2,
            padx=(10, 0), pady=(10, 0), sticky='nwse')

if __name__ == "__main__":
    app = App()
    app.mainloop()
