import tkinter as tk
from tkinter import ttk
import customtkinter
from CTkListbox import *
import os

FONT_TYPE = "Yu Gothic"

# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
        
#         view = FileView.FileView()
#         model = FileModel.FileModel()
#         controller = FileController.FileController(model, view)

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15)
        self.csv_filepath = None

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # フォームサイズ設定
        self.geometry("1000x800")
        self.title("File Manager")

        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(0, weight=1)

        # 1つ目のフレームの設定
        # stickyは拡大したときに広がる方向のこと。nsew で4方角で指定する。
        self.read_file_frame = ReadFileFrame(master=self, header_name="ファイル読み込み")
        self.read_file_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.show_dir_list = ShowDirList(master=self,header_name="show directory list")
        self.show_dir_list.grid(row=1, column=0, padx=(20,20), pady=(0,20),sticky="nsw", ipadx=40)

class ReadFileFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="ReadFileFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(0, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(0, weight=1)

        # フレームのラベルを表示
        self.label = customtkinter.CTkLabel(self, text=self.header_name, font=(FONT_TYPE, 11))
        self.label.grid(row=0, column=0, padx=20, sticky="w")

        # ファイルパスを指定するテキストボックス。これだけ拡大したときに、幅が広がるように設定する。
        self.textbox = customtkinter.CTkEntry(master=self, placeholder_text="CSV ファイルを読み込む", width=120, font=self.fonts)
        self.textbox.grid(row=1, column=0, padx=10, pady=(0,10), sticky="ew")

        # ファイル選択ボタン
        self.button_select = customtkinter.CTkButton(master=self, 
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),   # ボタンを白抜きにする
            command=self.button_select_callback, text="ファイル選択", font=self.fonts)
        self.button_select.grid(row=1, column=1, padx=10, pady=(0,10))
        
        # 開くボタン
        self.button_open = customtkinter.CTkButton(master=self, command=self.button_open_callback, text="開く", font=self.fonts)
        self.button_open.grid(row=1, column=2, padx=10, pady=(0,10))

    def button_select_callback(self):
        """
        選択ボタンが押されたときのコールバック。ファイル選択ダイアログを表示する
        """
        # エクスプローラーを表示してファイルを選択する
        file_name = ReadFileFrame.file_read()

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

class ShowDirList(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="ShowDirList", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fonts = (FONT_TYPE, 15)
        self.header_name = header_name

        # フォームのセットアップをする
        self.setup_form()

    def setup_form(self):
        # 行方向のマスのレイアウトを設定する。リサイズしたときに一緒に拡大したい行をweight 1に設定。
        self.grid_rowconfigure(1, weight=1)
        # 列方向のマスのレイアウトを設定する
        self.grid_columnconfigure(0, weight=1)
        
        ###Treeview Customisation (theme colors are selected)
        bg_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = self._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        
        # font_std = tk.font.Font(20)
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0, rowheight=30)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        ##Treeview widget data
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

    def show_value(selected_option):
        print(selected_option)


if __name__ == "__main__":
    app = App()
    app.mainloop()