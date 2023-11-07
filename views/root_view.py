import customtkinter
from views.manager_view import ManagerView

class RootView(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # FONT_TYPE = "meiryo"
        FONT_TYPE = "Yu Gothic"
    
        self.fonts = (FONT_TYPE, 15)
        self.csv_filepath = None

        start_width = 1000
        start_height = 800
        min_width = 950
        min_height = 775

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("File Manager")
        
        self.protocol('WM_DELETE_WINDOW', quit)
        
        print("create main windows")
        
        self.main_frame = ManagerView(master=self, header_name="File Manager View")
        self.main_frame.grid(row=0, column=0, padx=(0,0), pady=(0,0),sticky="nsew", ipadx=40)
        print("manager view")
        
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        
    def quit(self):
        self.quit()
        self.destroy()
