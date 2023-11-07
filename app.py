import customtkinter

from views.root_view import RootView
from models.main_model import MainModel
from controllers.main_controller import MainController

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.model = MainModel()
        
        self.view = RootView()
        # self.view.grid(row=0, column=0, padx=10, pady=10)
        
        controller = MainController(self.view, self.model)
        
        

if __name__ == "__main__":
    app = App()
    app.view.mainloop()