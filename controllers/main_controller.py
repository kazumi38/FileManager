import tkinter as tk
from tkinter import ttk
import customtkinter
from CTkListbox import *
import os

class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view