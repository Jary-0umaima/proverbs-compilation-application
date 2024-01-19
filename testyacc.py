import ply.yacc as yacc
from projetLex import tokens
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
import tkinter as tk
import speech_recognition as sr
import re
from PIL import Image, ImageTk
from tkinter import Toplevel, Label
import threading
from tkinter import TclError

global resultParser;global positionParserError
positionLexerError,positionParserError = dict(),dict()

# Grammar rules
def interface_compilateur():
    def p_proverb(p):
            '''proverb : proverb_1
                    | proverb_2
                    | proverb_3
                    | proverb_4
                    | proverb_5
                    | proverb_6
                    | proverb_7
                    | proverb_8
                    | proverb_9
                    | proverb_10
                    | prov1
                    | prov2
                    | prov3
                    | prov4
                    | prov5
                    | prov6
                    | prov7
                    | prov8
                    | prov9
                    | prov10'''
            # Process and interpret the proverb here
            p[0] = p[1]


        #proverb san numbre
        
    def p_proverb_1(p):
            'proverb_1 : ISSM1 FI3L1 HARF1 ISSM2'
            print("Parsing proverb_1:", p)
            # Ajoutez ici le traitement pour le proverbe 1
            p[0] = " ".join(p[1:])  

    def p_proverb_2(p):
            'proverb_2 : HARF2 FI3L2 ISSM3 FI3L3 ISSM4'
            # Ajoutez ici le traitement pour le proverbe 2
            p[0] = " ".join(p[1:])  
    def p_proverb_3(p):
            'proverb_3 : ISSM5 MODAF1 HARF3 ISSM6 MODAF2'
            # Ajoutez ici le traitement pour le proverbe 1
            p[0] = " ".join(p[1:])  

    def p_proverb_4(p):
            'proverb_4 : ISSM7 MODAF3 FI3L4 HARF1 ISSM8 MODAF2'
            # Ajoutez ici le traitement pour le proverbe 2
            p[0] = " ".join(p[1:])  
    def p_proverb_5(p):
            'proverb_5 : FI3L5 MAF3OLBIH1 FA FI3L5 MAF3OLBIH2'
            # Ajoutez ici le traitement pour le proverbe 1
            p[0] = " ".join(p[1:])  

    def p_proverb_6(p):
            'proverb_6 : FI3L6 HARF1 HARFNAFY FI3L7 MAF3OLBIH3 WAW HARFNAFY FI3L8 MAF3OLBIH4 '
            # Ajoutez ici le traitement pour le proverbe 2
            p[0] = " ".join(p[1:])  
    def p_proverb_7(p):
            'proverb_7 : ISSM9 KHABAR1 HARF1 ISSM10'
            # Ajoutez ici le traitement pour le proverbe 1
            p[0] = " ".join(p[1:])  

    def p_proverb_8(p):
            'proverb_8 : ISSM11 HARF1 ISSM12 MODAF4'
            # Ajoutez ici le traitement pour le proverbe 2
            p[0] = " ".join(p[1:])  
    def p_proverb_9(p):
            'proverb_9 : FI3L9 MAF3OLBIH5 FI3L10'
            # Ajoutez ici le traitement pour le proverbe 1
            p[0] = " ".join(p[1:])  

    def p_proverb_10(p):
            'proverb_10 : FI3L11 MAF3OLBIH6  ISSM13 HARF2 FI3L12'
            # Ajoutez ici le traitement pour le proverbe 2
            p[0] = " ".join(p[1:])  

        #def p_proverb_with_number(p):
        #   '''proverb_with_number : DELIMITER ISSM1 HARF1 FI3L1 ISSM2
        #                         | DELIMITER HARF2 FI3L2 ISSM3 FI3L3 ISSM4
        #                        | DELIMITER ISSM5 MODAF1 HARF3 ISSM6 MODAF2
            #                       | DELIMITER ISSM7 MODAF3 FI3L4 HARF1 ISSM8 MODAF2
            #                      | DELIMITER FI3L5 MAF3OLBIH1 FA FI3L5 MAF3OLBIH2
            #                     | DELIMITER FI3L6 HARF1 HARFNAFY FI3L7 MAF3OLBIH3 WAW HARFNAFY FI3L8 MAF3OLBIH4
            #                    | DELIMITER ISSM9 KHABAR1 HARF1 ISSM10
                #                   | DELIMITER ISSM11 HARF1 ISSM12 MODAF4
                #                  | DELIMITER FI3L9 MAF3OLBIH5 FI3L10
                #                 | DELIMITER FI3L11 MAF3OLBIH6 ISSM13 HARF2 FI3L12'''
            # Process and interpret the proverb with number here
            #pass
            
        #verfier est ce que le numbre est vrai ou faut 
        # Chaque proverbes avec numbre 

    def p_prov1(p):
            'prov1 :   DELIMITER proverb_1 '
            if(p[2]=='1'): 
                    print('الأفعال أبلغ من الأقوال 1')
            else:
                    print('erreur au niveau du delimiter de prov1,il faut mettre le delimiter 1')
                    
    def p_prov2(p):
            'prov2 :   DELIMITER proverb_2 '
            if(p[2]=='2'): 
                    print('إذا  تم العقل نقص الكلام2 ')
            else:
                    print('erreur au niveau du delimiter de prov2,il faut mettre le delimiter 2')
    def p_prov3(p):
            'prov3 :   DELIMITER proverb_3 '
            if(p[2]=='3'): 
                    print(' سلامة الإنسان في حلاوة اللسان 3')
            else:
                    print('erreur au niveau du delimiter de prov3,il faut mettre le delimiter 3')
    def p_prov4(p):
            'prov4 :   DELIMITER proverb_4 '
            if(p[2]=='4'): 
                    print(' عثرة القدم أسلم من عثرة اللسان4')
            else:
                    print('erreur au niveau du delimiter de prov4,il faut mettre le delimiter 4')
    def p_prov5(p):
            'prov5 :   DELIMITER proverb_5 '
            if(p[2]=='5'): 
                    print(' أساء سمعا فأساء إجابة5 ' )
            else:
                    print('erreur au niveau du delimiter de prov5,il faut mettre le delimiter 5')
    def p_prov6(p):
            'prov6 :   DELIMITER proverb_6'
            if(p[2]=='6'): 
                    print('احذروا من لا يرجى خيره ولا يؤمن شره 6')
            else:
                    print('erreur au niveau du delimiter de prov6,il faut mettre le delimiter 6')
                
    def p_prov7(p):
            'prov7 :   DELIMITER proverb_7'
            if(p[2]=='7'): 
                    print(' العتاب خير من الحقد7 ')
            else:
                    print('erreur au niveau du delimiter de prov7,il faut mettre le delimiter 7')

    def p_prov8(p):
            'prov8 :   DELIMITER proverb_8'
            if(p[2]=='8'): 
                    print('الجزاء من جنس العمل 8')
            else:
                    print('erreur au niveau du delimiter de prov8,il faut mettre le delimiter 8')


    def p_prov9(p):
            'prov9 :   DELIMITER proverb_9'
            if(p[2]=='9'): 
                    print('خالف هواك ترشد9')
            else:
                    print('erreur au niveau du delimiter de prov9,il faut mettre le delimiter 9')



    def p_prov10(p):
            'prov10 :   DELIMITER proverb_10'
            if(p[2]=='10'): 
                    print('اتق شر الحليم إذا غضب 10 ')
            else:
                    print('erreur au niveau du delimiter de prov10,il faut mettre le delimiter 10')

        # Error rule for syntax errors
    def p_error(p):
            
            global resultParser
            global positionParserError
            if p:
                positionParserError = {
                    "ligne": p.lineno,
                    "index": p.lexpos,
                    "value": p.value,
                    "length": len(p.value)
                }
            else:
                positionParserError = {
                    "ligne": "Unknown",
                    "index": "Unknown",
                    "value": "Unknown",
                    "length": "Unknown"
                }
            print("positionParserError = ", positionParserError)
            resultParser = "incorrect"

        # Build the parser
    parser = yacc.yacc()

        # Example usage of the parser
    '''
        data = 'إذا  تم العقل نقص الكلام'
        result = parser.parse(data)
        print(result)
        '''
    def p_undefined_proverb(p):
            '''undefined_proverb : DELIMITER UNDEFINED_PROVERB'''
            p[0] = " ".join(p[1:])
            raise ValueError("Proverbe Non Trouvé !")

    '''
        def parse_proverb():
            input_text = proverb_entry.get()
            try:
                result = parser.parse(input_text)
                messagebox.showinfo("Proverb Parsing Result", f" proverbe correcte\nResultat: {result}")
            except Exception as e:
                messagebox.showerror("Proverbe incorrecte", f"Error: {str(e)}")
        '''
    def parse_proverb():
            input_text = proverb_entry.get()
            try:
                result = parser.parse(input_text)
                if result:
                    messagebox.showinfo("Proverb Parsing Result", f"this is a proverb\n")
                # messagebox.showerror("Proverbe non défini", "Ce proverbe n'est pas défini dans le code.")
                else:
                    messagebox.showerror("Undefined proverb", "That is not a proverb !")
            except Exception as e:
                messagebox.showerror("Incorrect proverb", "The proverb is incorrect.")

    def get_proverb_from_voice_wrapper():
            get_proverb_from_voice(parser, result_text)

    window = CTk()
    window.geometry("300")
    window.title("Proverbs Compilation App") 
    set_appearance_mode("light")
        
    explanation_text = CTkLabel(window,text="  Proverbs compiler\n",font=("Arial", 20),
                                text_color="#5c5757") 
    explanation_text.grid(row=0, column=1, padx=10, pady=10)


    proverb_label = CTkLabel(master=window, text="Enter the proverb:", font=("Arial", 15),
                                text_color="#5c5757"
                                )
    proverb_label.grid(row=1, column=0, padx=1, pady=1)


    proverb_entry = CTkEntry(master=window, placeholder_text="Start typing a proverb ...",
                                width=200, text_color="#4b81ab"
                                )
    proverb_entry.grid(row=1, column=1, padx=10, pady=10)
    
    try:
        submit_img = Image.open("submitF.png")
        parse_button = CTkButton(master=window, text="Compile", corner_radius=32, image=CTkImage(dark_image=submit_img),
                                fg_color="transparent", hover_color="#4b81ab", border_color="#485188",
                                border_width=2, command=parse_proverb, text_color="black", width=100
                                )
        parse_button.grid(row=2, column=1, columnspan=2, pady=10)
    except TclError as e:
        parse_button = CTkButton(master=window, text="compile", corner_radius=32,
                                        fg_color="transparent", hover_color="#4b81ab", border_color="#485188",
                                        border_width=2, command=parse_proverb, text_color="black", width=100
                                        )
        parse_button.grid(row=2, column=1, columnspan=2, pady=10)


    def get_selected_language(event):
            global selected_language
            selected_language = language_menu.get() 
            
    languages = ['French', 'English', 'Moroccan(Darija)'] 
        
    language_menu = CTkComboBox(master=window, values=languages, command=get_selected_language)
    language_menu.grid(row=3, column=3, sticky='ne', padx=1, pady=10)

    equivalents = {
            'الأفعال أبلغ من الأقوال': {
                'French': 'Les actes valent mieux que les paroles.', # Ron Dennis
                'English': 'Actions speak louder than words', # Anthony of Padua
                'Moroccan(Darija)': 'الفعال زين الا زين لا'
                #'Moroccan(Darija)': 'لا زين الا زين الفعال'
            },
            'إذا  تم العقل نقص الكلام': {
                'French': 'La parole est d\'argent, le silence est d\'or.', 
                'English': 'Silence is golden when the mind is mature.', 
                'Moroccan(Darija)': 'فاتت اللي المعلية من أحسن باقية اللي الكلمة'
                #'Moroccan(Darija)': 'الكلمة اللي باقية أحسن من المعلية اللي فاتت'
            },
            'سلامة الإنسان في حلاوة اللسان': {
                'French': 'La prudence est la garde de la langue.',
                'English': 'the tongue that heals is a tree of live, but a devious tongue breaks the spirit.',
                'Moroccan(Darija)': 'فالدية يدوز لحلو اللسان'
                #'Moroccan(Darija)': 'اللسان لحلو يدوز فالدية'
            },
            'عثرة القدم أسلم من عثرة اللسان': {
                'French': 'La langue n\'a pas d\'os, mais elle peut casser les tiens',
                'English': 'Sticks and stones may break my bones, but words will never hurt me.',
                'Moroccan(Darija)': 'عظم مافيه اللسان'
                #'Moroccan(Darija)': 'اللسان مافيه عظم'
            },
            'أساء سمعا فأساء إجابة': {
                'French': 'Tourner sept fois sa langue dans sa bouche avant de parler',
                'English': 'Think before you speak',
                'Moroccan(Darija)': 'الجواب حقق السمع حقق لي'
                #'Moroccan(Darija)': 'لي حقق السمع حقق الجواب'
            },
            'احذروا من لا يرجى خيره ولا يؤمن شره': {
                'French': 'Chien qui aboie ne mord pas.',
                'English': 'All bark and no bite.', # a refaire
                'Moroccan(Darija)': 'السكوتي الواد على دوز لا و الهرهوري الواد على دوز'
                #'Moroccan(Darija)': 'دوز على الواد الهرهوري و لا دوز على الواد السكوتي' # a refaire
            },
            'العتاب خير من الحقد': {
                'French': 'Qui aime bien châtie bien',
                'English': 'A stitch in time saves nine.',
                'Moroccan(Darija)': 'كذاب من حسن قاصح'
                #'Moroccan(Darija)': 'قاصح حسن من كذاب'
            },
            'الجزاء من جنس العمل': {
                'French': 'On récolte ce que l\'on sème',
                'English': 'You reap what you sow',
                'Moroccan(Darija)': 'الواد تيحمل قطرة قطرة'
                #'Moroccan(Darija)': 'قطرة قطرة تيحمل الواد'
            },
            'خالف هواك ترشد': {
                'French': 'Résister au premier désir est le commencement de la vertu',
                'English': 'Resist the devil, and he will flee from you.',
                'Moroccan(Darija)': 'نصو تخلي رخصو غواك لي'
                #'Moroccan(Darija)': 'لي غواك رخصو تخلي نصو'
            },
            'اتق شر الحليم إذا غضب': {
                'French': 'Méfie-toi de l\'eau qui dort',
                'English': 'Beware of the fury of a patient man.',
                'Moroccan(Darija)': 'الرخام يثقب الدوام'
                #'Moroccan(Darija)': 'الدوام يثقب الرخام'
            }
                
        }

    '''
        result_text = CTkTextbox(master=window, scrollbar_button_color="#FFCC70", corner_radius=16,
                                border_color="#FFCC70", border_width=2, height=50, width=200)
        result_text.grid(row=4, column=0, columnspan=3, pady=10)
        result_text.grid_remove()
        '''


    def get_equivalent_proverb():
            input_text = proverb_entry.get().strip()
            selected_language = language_menu.get()
            result_text.delete(1.0, tk.END)
            
            found_proverb = False
            
            if input_text in equivalents:
                langues = equivalents[input_text]
                if selected_language in langues:
                    translation = langues[selected_language]
                    #result_text.insert(tk.END, f"Proverbe : {input_text}\n")
                    result_text.insert(tk.END, f"Equivalent in {selected_language} Culture: \n --> {translation}\n")
                    found_proverb = True
            
            if not found_proverb:
                result_text.insert(tk.END, f"This Proverb is not valid\n")
                
            
            result_text.grid(row=4, column=0, columnspan=2, pady=10)

    # vocal
    def get_proverb_from_voice(parser, result_text):
            recognizer = sr.Recognizer()

            with sr.Microphone() as source:
                print("Say a proverb :")
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language='ar')
                proverb_entry.delete(0, tk.END)
                proverb_entry.insert(0, text)

            except sr.UnknownValueError:
                messagebox.showerror("Error", "Unable to understand audio")
            except sr.RequestError as e:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"Error during query : {e}")

        # Bouton pour obtenir l'équivalent du proverbe dans la langue sélectionnée

    get_equivalent_button = CTkButton(master=window, text="Obtain the equivalent in ...... culture ", corner_radius=32,
                                        fg_color="transparent", hover_color="#4b81ab", border_color="#485188",
                                        border_width=2, command=get_equivalent_proverb, text_color="black"
                                        )
    get_equivalent_button.grid(row=3, column=1, columnspan=2, pady=10)

        # Zone de texte pour afficher les résultats
    result_text = CTkTextbox(master=window, scrollbar_button_color="#FFCC70", corner_radius=16,
                                border_color="#5c5757", border_width=2, height=100, width=200)
    result_text.grid(row=4, column=2, columnspan=3, pady=10, sticky="nsew")
    result_text.grid_remove()
    try:    
        icon_vocal = Image.open("vocal2.png")
        icon_vocal = CTkImage(icon_vocal)
                #icon_vocal = icon_vocal.resize((40, 40))
                #icon_vocal = ImageTK.PhotoImage(icon_vocal)
        vocal_button = CTkButton(master=window, corner_radius=32, image=icon_vocal, text="",
                                fg_color="transparent", hover_color="#4b81ab", border_color="#485188",
                                border_width=2, command=get_proverb_from_voice_wrapper,  width=20
                                )
        vocal_button.grid(row=1, column=2, columnspan=2, pady=10)
    except TclError as e:
        vocal_button = CTkButton(master=window, corner_radius=32,text="!!", text_color="red",
                                fg_color="transparent", hover_color="#4b81ab", border_color="#485188",
                                border_width=2, command=get_proverb_from_voice_wrapper,  width=20
                                )
        vocal_button.grid(row=1, column=2, columnspan=2, pady=10) 

    proverb_label.grid(row=1, column=0, padx=1, pady=1)
    proverb_entry.grid(row=1, column=1, padx=10, pady=10)
    parse_button.grid(row=2, column=1, columnspan=2, pady=10)



    window.mainloop()