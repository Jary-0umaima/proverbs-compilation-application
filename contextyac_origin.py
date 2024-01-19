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

global resultParser;global positionParserError

positionLexerError,positionParserError = dict(),dict()

import tkinter as tk
from customtkinter import *




window = CTk()
window.geometry("300")
window.title("Context") 
set_appearance_mode("light")

def get_selected_language(event):
        global selected_language
        selected_language = language_menu.get() 

languages = ['Arab', 'French', 'English', 'Moroccan(Darija)'] 

language_menu = CTkComboBox(master=window, values=languages, command=get_selected_language)
language_menu.grid(row=2, column=3, sticky='ne', padx=1, pady=10)

proverb_label = CTkLabel(master=window, text="Enter context:", font=("Arial", 15), text_color="#5c5757")
proverb_label.grid(row=1, column=0, padx=1, pady=1)

proverb_entry = CTkEntry(master=window, placeholder_text="Enter a context .....", width=200, text_color="#4b81ab")
proverb_entry.grid(row=1, column=1, padx=10, pady=10)

contexts = {
        
        # ------- Context de proverbe 1 => الأفعال أبلغ من الأقوال ------
        'صدق ما تراه وانسى ما تسمعه': {
            'Arab': 'الأفعال أبلغ من الأقوال',
            'French': 'Les actes valent mieux que les paroles.',
            'English': 'Actions speak louder than words',
            'Moroccan(Darija)': 'لا زين الا زين الفعال'
        },
        'لقد جاءتني مشكلة ملحة وأنا في حاجة ماسة لمساعدة صديقتي، التي كانت دائمًا معي في  كل مكان اذهب اليه واحكي لها كل شيء . كنت أعلم جيدًا أن مستواها المادي جيد ، ولكن عندما طلبت منها المساعدة لشراء دواء لأمي، قالت لي بأسف أنها ليست قادرة على تقديم المساعدة المالية.': {
            'Arab': 'الأفعال أبلغ من الأقوال',
            'French': 'Les actes valent mieux que les paroles.',
            'English': 'Actions speak louder than words',
            'Moroccan(Darija)': 'لا زين الا زين الفعال'
        },
        'Mon amie fait toujours des promesses mais elle était absente lorsque j\'avais besoin d\'elle': {
            'Arab': 'الأفعال أبلغ من الأقوال',
            'French': 'Les actes valent mieux que les paroles.',
            'English': 'Actions speak louder than words',
            'Moroccan(Darija)': 'لا زين الا زين الفعال'
        },
        'Une amie ne parle pas beaucoup mais elle est toujours présente pour moi quand j\'ai besoin d\'elle.':{
            'Arab': 'الأفعال أبلغ من الأقوال',
            'French': 'Les actes valent mieux que les paroles.',
            'English': 'Actions speak louder than words',
            'Moroccan(Darija)': 'لا زين الا زين الفعال'
        },
        # ------- Context de proverbe 2 => إذا  تم العقل نقص الكلام ------
        'عندما يكتمل العقل يقل الكلام': {
            'Arab': 'إذا  تم العقل نقص الكلام',
            'French': 'La parole est d\'argent, le silence est d\'or.',
            'English': 'Silence is golden when the mind is mature.',
            'Moroccan(Darija)': 'الكلمة اللي باقية أحسن من المعلية اللي فاتت'
        },
        'كان في حينا شخص يتميز  بالحكمة و الرزانة كان   لا يتكلم من غير سبب واذ اتكلم كانت   كلماته متناغمة وتحمل معاني عميقة ومفيدة': {
            'Arab': 'إذا  تم العقل نقص الكلام',
            'French': 'La parole est d\'argent, le silence est d\'or.',
            'English': 'Silence is golden when the mind is mature.',
            'Moroccan(Darija)': 'الكلمة اللي باقية أحسن من المعلية اللي فاتت'
        },
        'j\'étais avec un groupe  discutant un sujet complexe. et ma cousine entre dans la conversation elle avait  une grande compréhension et maîtrise du sujet , les autres écoutaient avec attention. et elle exprimait ses idées de manière concise et précise, utilisant peu de mots pour transmettre des informations riches et claires.': {
            'Arab': 'إذا  تم العقل نقص الكلام',
            'French': 'La parole est d\'argent, le silence est d\'or.',
            'English': 'Silence is golden when the mind is mature.',
            'Moroccan(Darija)': 'الكلمة اللي باقية أحسن من المعلية اللي فاتت'
        },
        # ------- Context de proverbe 3 => سلامة الإنسان في حلاوة اللسان ------
        'Mon collègue au travail est connu pour sa politesse et sa douceur dans ses paroles, même dans les moments difficiles. Sa manière agréable de s\'exprimer lui a valu le respect de l\'équipe et contribue à maintenir un environnement de travail positif.': {
            'Arab': 'سلامة الإنسان في حلاوة اللسان',
            'French': 'La prudence est la garde de la langue.',
            'English': 'the tongue that heals is a tree of live, but a devious tongue breaks the spirit.',
            'Moroccan(Darija)': 'اللسان لحلو يدوز فالدية'
        },
        'تعلمت من تجاربي، ان الكلمات الطيبة والرقيقة تجلب البهجة والسعادة للآخرين، وتعكس مكانة وطيب النفس. كانت تلك اللحظات التي قدمت فيها كلمات الشكر والإشادة تعود علي بالرضا والسعادة الداخلية.':{
            'Arab': 'سلامة الإنسان في حلاوة اللسان',
            'French': 'La prudence est la garde de la langue.',
            'English': 'the tongue that heals is a tree of live, but a devious tongue breaks the spirit.',
            'Moroccan(Darija)': 'اللسان لحلو يدوز فالدية'
        },
        
        # ------- Context de proverbe 4 => عثرة القدم أسلم من عثرة اللسان ------
        'Mon collègue au travail est connu pour sa politesse et sa douceur dans ses paroles, même dans les moments difficiles. Sa manière agréable de s\'exprimer lui a valu le respect de l\'équipe et contribue à maintenir un environnement de travail positif.': {
            'Arab': 'عثرة القدم اسلم من عثرة اللسان',
            'French': 'La langue n\'a pas d\'os, mais elle peut casser les tiens',
            'English': 'Sticks and stones may break my bones, but words will never hurt me.',
            'Moroccan(Darija)': 'اللسان مافيه عظم'
        },
        'تشاجرت صديقتي مع فتاة من مدرستي فاذا ذلك الى انها قامت بسب تلك الفتاة ، حيث كان كلامها    الجارح سببًا في إحداث الأذى ل تلك الفتاة . تألمت صديقتي   لأنها شعرت بأثر كلماتها السلبية وكيف أنها تسببت في جرح تلك الفتاة':{
            'Arab': 'عثرة القدم اسلم من عثرة اللسان',
            'French': 'La langue n\'a pas d\'os, mais elle peut casser les tiens',
            'English': 'Sticks and stones may break my bones, but words will never hurt me.',
            'Moroccan(Darija)': 'اللسان مافيه عظم'
        },
        # ------- Context de proverbe 5 => أساء سمعا فأساء إجابة ------
         'Lors d\'une réunion, une personne a mal interprété les paroles d\'un collègue et a réagi de manière inappropriée sans clarification.': {
            'Arab': 'أساء سمعا فأساء إجابة',
            'French': 'Tourner sept fois sa langue dans sa bouche avant de parler',
            'English': 'Think before you speak',
            'Moroccan(Darija)': 'لي حقق السمع حقق الجواب'
        },
        'كان اخي قد نادا اختي باسمها كي يعاتبها على امور لم تفعلها  سمعته انا  وظننت  انه يتكلم معي فصرخت في وجهه   وكنت ساتشاجر معه فقال لي لم اناديك انت بل ناديت مريم فخجلت بعدها كثيرا':{
            'Arab': 'أساء سمعا فأساء إجابة',
            'French': 'Tourner sept fois sa langue dans sa bouche avant de parler',
            'English': 'Think before you speak',
            'Moroccan(Darija)': 'لي حقق السمع حقق الجواب'
        },
        # ------- Context de proverbe 6 => احذروا من لا يرجى خيره ولا يؤمن شره ------
        'Un groupe d\'étudiants travaille sur un projet en équipe. L\'un des membres semble peu impliqué dans le travail et ne contribue pas de manière significative. Les autres étudiants, connaissant son manque d\'engagement, décident de ne pas compter sur lui pour les tâches cruciales du projet.': {
            'Arab': 'احذروا من لا يرجى خيره ولا يؤمن شره',
            'French': 'Chien qui aboie ne mord pas.',
            'English': 'All bark and no bite.', # a refaire
            'Moroccan(Darija)': 'دوز على الواد الهرهوري و لا دوز على الواد السكوتي' # a refaire
        },
        'كان في حينا جارة كانت تؤدينا بصوت الموسقى الصاخبة ورميها للازبال والتحدث في اعراض الناس بالرغم من معاملتنا الحسنة  لها كما انها لم تصنع خيرا قط':{
            'Arab': 'احذروا من لا يرجى خيره ولا يؤمن شره',
            'French': 'Chien qui aboie ne mord pas.',
            'English': 'All bark and no bite.', # a refaire
            'Moroccan(Darija)': 'دوز على الواد الهرهوري و لا دوز على الواد السكوتي' # a refaire
        },
        # ------- Context de proverbe 7 => العتاب خير من الحقد ------
        'Lorsque deux amis proches traversent une période difficile en raison d\'un malentendu, au lieu de laisser la rancœur s\'installer, l\'un d\'eux décide d\'exprimer ses préoccupations ouvertement. ': {
            'Arab': 'العتاب خير من الحقد',
            'French': 'Qui aime bien châtie bien',
            'English': 'A stitch in time saves nine.',
            'Moroccan(Darija)': 'قاصح حسن من كذاب'
        },
        'ذات يوم ، كانت فيه صديقتي وأنا في خلاف بسيط. كانت الأمور تتصاعد وتزداد تعقيدًا مع مرور الوقت، لكن بدلاً من الحقد والغضب، قررت التحدث معها بصراحة وعتاب بناء.':{
            'Arab': 'العتاب خير من الحقد',
            'French': 'Qui aime bien châtie bien',
            'English': 'A stitch in time saves nine.',
            'Moroccan(Darija)': 'قاصح حسن من كذاب'
        },
        # ------- Context de proverbe 8 => الجزاء من جنس العمل------
        'في يوم من الأيام، كانت لدي فكرة مذهلة وقررت العمل عليها. أقنعت نفسي أنه يجب بذل الجهد والوقت لتحقيق هذا الهدف. بدأت العمل بجد وكنت متحمسًا للحظة التي سأنال فيها ثمار جهدي': {
            'Arab': 'الجزاء من جنس العمل',
            'French': 'On récolte ce que l\'on sème',
            'English': 'You reap what you sow',
            'Moroccan(Darija)': 'قطرة قطرة تيحمل الواد'
        },
        'Deux étudiants partagent des conditions d\'étude similaires, assistent aux mêmes cours et passent les mêmes examens. Cependant, leurs résultats divergent en raison de leur engagement et 	de leur approche envers les études.': {
            'Arab': 'الجزاء من جنس العمل',
            'French': 'On récolte ce que l\'on sème',
            'English': 'You reap what you sow',
            'Moroccan(Darija)': 'قطرة قطرة تيحمل الواد'
        },
        # ------- Context de proverbe 9 => خالف هواك ترشد------
        'Dans une situation financière délicate, une personne résiste à l\'envie d\'acheter quelque chose de cher qu\'elle ne peut pas vraiment se permettre. Plutôt que de succomber à l\'impulsion, elle prend du recul, réfléchit et opte pour une approche budgétaire plus raisonnable.': {
            'Arab': 'خالف هواك ترشد',
            'French': 'Résister au premier désir est le commencement de la vertu',
            'English': 'Resist the devil, and he will flee from you.',
            'Moroccan(Darija)': '9'
        },
        'في يوم من الأيام، وجدت نفسي محتارًا بين خيارين،في هذه اللحظة، نصحني ابي   بخوض طريق يخالف ميلي و هواي ، فلربما يكون الحكم في تجاوز هواي أفضل بالنهاية. قررت الاستماع إلى هذه النصيحة، حتى وإن كانت تعارض ما أرغب به': {
            'Arab': 'خالف هواك ترشد',
            'French': 'Résister au premier désir est le commencement de la vertu',
            'English': 'Resist the devil, and he will flee from you.',
            'Moroccan(Darija)': '9'
        },
        # ------- Context de proverbe 9 => اتق شر الحليم إذا غضب -----
        
        'Un professeur qui est de nature calme perd sa patience face à un comportement perturbateur et sanctionne toute la classe.': {
            'Arab': 'اتق شر الحليم إذا غضب',
            'French': 'Méfie-toi de l\'eau qui dort',
            'English': 'Beware of the fury of a patient man.',
            'Moroccan(Darija)': '10'
        },
        
        'كنت أنا، الذي يتسم بالهدوء والصبر والتسامح، أعيش حياتي بسلام في إحدى الأماكن. وفجأة، تعرّضت لموقف مؤلم عندما تصرف أحد أقربائي بشكل ظالم وجارح تجاهي، دون سبب واضح. بالرغم من هدوءي الدائم، إلا أن هذا الظلم المتواصل دفعني إلى غضب شديد، كان كالعاصفة الهادئة التي اندلعت فجأة.':{
            'Arab': 'اتق شر الحليم إذا غضب',
            'French': 'Méfie-toi de l\'eau qui dort',
            'English': 'Beware of the fury of a patient man.',
            'Moroccan(Darija)': '10'
        }
   }

def get_proverb_from_context():
        input_text = proverb_entry.get().strip()
        selected_language = language_menu.get()
        result_text.delete(1.0, tk.END)
        
        found_proverb = False
        
        if input_text in contexts:
            langues = contexts[input_text]
            if selected_language in langues:
                proverepossible = langues[selected_language]
                result_text.insert(tk.END, f"The right proverb for your situation in {selected_language} Culture :\n\n{proverepossible}\n")
                found_proverb = True
        
        if not found_proverb:
            result_text.insert(tk.END, f"Unfortunately ! \n\nI couldn't find any proverbs for your situation\n")
                
        result_text.grid(row=4, column=0, columnspan=2, pady=10)

def submit_context():
        get_proverb_from_context()
submit_img = Image.open("submitF.png")
submit_button = CTkButton(master=window, text="Submit",fg_color="transparent",hover_color="#4b81ab", image=CTkImage(dark_image=submit_img),
                            border_width=2, border_color="#485188" ,command=submit_context, text_color="black", width=90
                            )
submit_button.grid(row=2, column=1, pady=10)

result_text = CTkTextbox(master=window, scrollbar_button_color="#FFCC70", corner_radius=16,
                            border_color="#5c5757", border_width=2, height=100, width=200)
result_text.grid(row=4, column=2, columnspan=3, pady=10, sticky="nsew")
result_text.grid_remove()

window.mainloop()