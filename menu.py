import ply.yacc as yacc
#from lex_context import context_tokens
from pyarabic import *
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
import tkinter as tk
from PIL import Image
from tkinter import Tk, Button, Toplevel
import speech_recognition as sr
import re
from PIL import Image, ImageTk
from tkinter import Toplevel, Label
import threading

global resultParser;global positionParserError

positionLexerError,positionParserError = dict(),dict()

import tkinter as tk
from customtkinter import *
#from testyacc import interface_compilateur
#from testContext import interface_context


def ouvrir_interface_context():
        from testContext import interface_context
        interface_context()

def ouvrir_interface_conpilateur():
        from testyacc import interface_compilateur
        icon_vocal = Image.open("vocal2.png")
        interface_compilateur()
        pass
    
menu = CTk()
menu.geometry("1000")
menu.title("Proverbs PlatForm ") 
set_appearance_mode("light")
# ---------------------------------------------
explanation_text = CTkLabel(menu,text="Welcome to our cross-cultural proverb generation and verification app\n",font=("Arial", 20),
                         text_color="#5c5757") 
explanation_text.grid(row=0, column=0, padx=10, pady=10)
# ---------------------------------------------
descriptive2 = (
        "Select this option to generate "
         "a proverb in the language\nof your choice depending on the situation you provide."
    )
descriptive2_label = CTkLabel(master=menu, text=descriptive2, font=("Arial", 15),
                         text_color="#5c5757"
                         )
descriptive2_label.grid(row=1, column=0, padx=10, pady=10)

loop_img = Image.open("interog.png")
submit_button1 = CTkButton(master=menu, text="Find a proverb for your situation",fg_color="transparent",hover_color="#4b81ab",image=CTkImage(dark_image=loop_img),
                          border_width=2, border_color="#485188", text_color="black",command=ouvrir_interface_context)
submit_button1.grid(row=2, column=0, pady=10)
# ---------------------------------------------
descriptive1 = (
                "Choose this option to submit a text and check if it is a proverb.\n"
                 "If so, find out its equivalent in other cultures"
                )
descriptive1_label = CTkLabel(master=menu, text=descriptive1, font=("Arial", 15),
                         text_color="#5c5757"
                         )
descriptive1_label.grid(row=3, column=0, padx=10, pady=10)

compile_img = Image.open("compile3.png")
submit_button2 = CTkButton(master=menu, text="Compile your proveb",fg_color="transparent",hover_color="#4b81ab",image=CTkImage(dark_image=compile_img),
                          border_width=2, border_color="#485188" , text_color="black", command=ouvrir_interface_conpilateur,)
submit_button2.grid(row=4, column=0, pady=10)

menu.mainloop() 
    
