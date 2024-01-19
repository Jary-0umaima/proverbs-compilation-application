import ply.lex as lex
import re
global resultLexer;global positionLexerError

positionLexerError = dict(),

tokens = [ 'FI3L1','ISSM1','ISSM2','HARF1','HARF2','FI3L2','ISSM3','FI3L3','ISSM4','ISSM5','MODAF1','HARF3','ISSM6','MODAF2','ISSM7','MODAF3','FI3L4','ISSM8','FI3L5','MAF3OLBIH1','FA','MAF3OLBIH2','FI3L6','HARFNAFY','FI3L7','MAF3OLBIH3','WAW','FI3L8','MAF3OLBIH4','ISSM9','KHABAR1','ISSM10','ISSM11','ISSM12','MODAF4','FI3L9','MAF3OLBIH5','FI3L10','FI3L11','MAF3OLBIH6','ISSM13','FI3L12','DELIMITER']
#PROVERB 1
t_ISSM1=r'الأفعال'
t_HARF1=r' من'
t_FI3L1=r' أبلغ'
t_ISSM2=r'الأقوال'
#nombre de proverb
#PROVERB2
t_HARF2 = r'إذا'
t_FI3L2 = r'تم'
t_ISSM3= r'العقل'
t_FI3L3 = r'نقص'
t_ISSM4 = r'الكلام'
#PROVERB3
t_ISSM5 = r'سلامة'
t_MODAF1 = r'الإنسان'
t_HARF3  = r'في'
t_ISSM6 = r'حلاوة'
t_MODAF2 = r'اللسان'
#PRIVERB4
t_ISSM7 = r'عثرة'
t_MODAF3 = r'القدم'
t_FI3L4 = r'أسلم'
#t_HARF1 = r'من'#DEJA SAISAIR 
t_ISSM8 = r'عثرة'
#t_MODAF2 = r'اللسان' #DEJA SASIR 

#PROVERB 5
t_FI3L5  = r'أساء'
t_MAF3OLBIH1 = r'سمعا'
t_FA = r'ف'
#t_FI3L5  = r'أساء'
t_MAF3OLBIH2 = r'إجابة'
 
#PROVERB6
t_FI3L6 = r'احذروا'
#t_HARF1 = r'من'
t_HARFNAFY = r'لا'
t_FI3L7 = r'يرجى'
t_MAF3OLBIH3  = r'خيره'
t_WAW = r'و'
#t_HARFNAFY = r'لا'
t_FI3L8 = r'يؤمن'
t_MAF3OLBIH4  = r'شره'
#PROVERB7
t_ISSM9 = r'العتاب'
t_KHABAR1 = r'خير'
#t_HARF1 = r'من'
t_ISSM10 = r'الحقد'
#PROVERB8
t_ISSM11 = r'الجزاء'
#t_HARF1 = r'من'
t_ISSM12 = r'جنس'
t_MODAF4 = r'العمل'
#
#PROVERB9
t_FI3L9 = r'خالف'
t_MAF3OLBIH5 = r'هواك'
t_FI3L10 = r'ترشد'
#PROVERB10
t_FI3L11  = r'اتق'
t_MAF3OLBIH6 = r'شر'
t_ISSM13= r'الحليم'
#t_HARF2 = r'اذا'
t_FI3L12 = r'غضب'

t_DELIMITER=r'\d+'
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
   # t.lexer.lexpos += len(t.value)
 #lexer = lex.lex()
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at index {t.lexpos}")
    t.lexer.skip(1)
    
""""""
# Construction du lexer
lexer = lex.lex()

# Reading input text from a file
file_name = "program.txt"
with open(file_name, "r", encoding="utf-8") as file:
    data = file.read().strip()

# Using the lexer to tokenize the input

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)