import tkinter as tk
from tkinter import ttk
import customtkinter
from CTkListbox import *
import os

FONT_TYPE = "Yu Gothic"

class ManagerView(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="ReadFileFrame", **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name
        self.fonts = (FONT_TYPE, 15)
        self.setup_form()
        
    def setup_form(self):
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # settring upper tool bar. 
        self.tool_frame = customtkinter.CTkFrame(self)
        self.tool_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self, text=self.header_name, font=self.fonts)
        self.label.grid(row=0, column=0, padx=20, sticky="w")
        self.textbox = customtkinter.CTkEntry(master=self, placeholder_text="CSV ファイルを読み込む", width=120, font=self.fonts)
        self.textbox.grid(row=1, column=0, padx=10, pady=(0,10), sticky="ew")
        self.button_select = customtkinter.CTkButton(master=self, 
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            command=self.button_select_callback, text="ファイル選択", font=self.fonts)
        self.button_select.grid(row=1, column=1, padx=10, pady=(0,10))
        self.button_open = customtkinter.CTkButton(master=self, command=self.button_open_callback, text="開く", font=self.fonts)
        self.button_open.grid(row=1, column=2, padx=10, pady=(0,10))
        
        # setting left side bar. (dir list)
        self.show_dir_list = customtkinter.CTkFrame(self)
        self.show_dir_list.grid(row=1, column=0, padx=(20,20), pady=(0,20),sticky="nsw", ipadx=40)
    
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0, rowheight=30)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.treeview = ttk.Treeview(self, height=30,show="tree")
        self.treeview.grid(padx=10)
        self.treeview.insert('', '0', 'i1', text ='Python')
        self.treeview.insert('', '1', 'i2', text ='Customtkinter')
        self.treeview.insert('', '2', 'i3', text ='Tkinter')
        self.treeview.insert('i2', 'end', 'Frame', text ='Frame')
        self.treeview.insert('i2', 'end', 'Label', text ='Label')
        self.treeview.insert('i3', 'end', 'Treeview', text ='Treeview')
        self.treeview.move('i2', 'i1', 'end')
        self.treeview.move('i3', 'i1', 'end')

        self.treeview.grid(row=0, column=0, padx=0, pady=(0,10), sticky="w")
    
    # must need moving function to controller
    def button_select_callback(self):
        """
        選択ボタンが押されたときのコールバック。ファイル選択ダイアログを表示する
        """
        # エクスプローラーを表示してファイルを選択する
        file_name = ManagerView.file_read()

        if file_name is not None:
            # ファイルパスをテキストボックスに記入
            self.textbox.delete(0, tk.END)
            self.textbox.insert(0, file_name)

    def button_open_callback(self):
        """
        開くボタンが押されたときのコールバック。暫定機能として、ファイルの中身をprintする
        """
        file_name = self.textbox.get()
        if file_name is not None or len(file_name) != 0:
            with open(file_name) as f:
                data = f.read()
                print(data)
            
    @staticmethod
    def file_read():
        """
        ファイル選択ダイアログを表示する
        """
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = tk.filedialog.askopenfilename(filetypes=[("csvファイル","*.csv")],initialdir=current_dir)

        if len(file_path) != 0:
            return file_path
        else:
            # ファイル選択がキャンセルされた場合
            return None
